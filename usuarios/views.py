from django.shortcuts import render, redirect
from django.contrib.auth.models import User

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
        print(f'\n\nemail: {email} -- senha {senha}')

        if email.strip() == '' or senha.strip() == '':
            print('Campos email e senha não podem estar em branco.')
            return redirect('login')
        else:
            print('Login efetuado com sucesso.')
            return redirect('dashboard')

    return render(request, 'usuarios/login.html')

def dashboard(request):
    return render(request, 'usuarios/dashboard.html')

def logout(request):
    pass