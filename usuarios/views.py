from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if not nome.strip():
            messages.error(request, 'O campo nome não pode ficar em branco.')
            return redirect('cadastro')

        if not email.strip():
            messages.error('O campo email não pode ficar em branco.')
            return redirect('cadastro')

        if senha != senha2:
            messages.error(request, 'As senhas não são iguais.')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado.')
        else:
            user = User.objects.create_user(username=nome, email=email, password=senha)
            user.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')

        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if email.strip() == '' or senha.strip() == '':
            print('Campos email e senha não podem estar em branco.')
            return redirect('login')
        else:
            if User.objects.filter(email=email).exists():
                nome = User.objects.filter(email=email).values_list('username', flat=True).get()
                user = auth.authenticate(request, username=nome, password=senha)
                if user is not None:
                    auth.login(request, user=user)
                    print('Login efetuado com sucesso.')
                    return redirect('dashboard')
                else:
                    print('Usuário não cadastrado.')
                    return redirect('login')

    return render(request, 'usuarios/login.html')

def dashboard(request):
    if request.user.is_authenticated:
        userId = request.user.id
        receitas = Receita.objects.order_by('-dataCadastro').filter(autor=userId)

        dados = {
            'receitas': receitas
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def logout(request):
    auth.logout(request)
    return redirect('index')

def criaReceita(request):
    if request.method == 'POST':
        nomeReceita = request.POST['nomeReceita']
        ingredientes = request.POST['ingredientes']
        modoPreparo = request.POST['modoPreparo']
        tempoPreparo = request.POST['tempoPreparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        img = request.FILES['img']

        user = get_object_or_404(User, pk=request.user.id)

        receita = Receita.objects.create(
            autor=user,
            nomeReceita=nomeReceita,
            ingredientes=ingredientes,
            modoPreparo=modoPreparo,
            tempoPreparo=tempoPreparo,
            rendimento=rendimento,
            categoria=categoria,
            img=img,
            dataCadastro=datetime.now()
            )
        receita.save()

        return redirect('dashboard')
    else:
        return render(request, 'usuarios/criaReceita.html')

def deletaReceita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')

def editaReceita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receitaAEditar = {'receita': receita}
    return render(request, 'usuarios/editareceita.html', receitaAEditar)