from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if not nome.strip():
            print('O campo nome não pode ficar em branco.')
            return redirect('cadastro')

        if not email.strip():
            print('O campo email não pode ficar em branco.')
            return redirect('cadastro')

        if senha != senha2:
            print('As senhas não são iguais.')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            print('Usuário já cadastrado.')
        else:
            user = User.objects.create_user(username=nome, email=email, password=senha)
            user.save()
            print('Usuário cadastrado com sucesso!')

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
    return render(request, 'usuarios/dashboard.html')

def logout(request):
    pass