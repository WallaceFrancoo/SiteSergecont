from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginForm, CadastroForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages, auth
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form["email"].value()
            senha = form["senha"].value()

            try:
                usuario = User.objects.get(email=email)
                user = auth.authenticate(username=usuario.username, password=senha)

                if user is not None:
                    auth.login(request, user)
                    return redirect('inicio')
                else:
                    messages.error(request, "Senha incorreta.")
                    return redirect('login')

            except User.DoesNotExist:
                messages.error(request, "Usuário não encontrado.")
                return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForm()
    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            if form["senha"].value() != form["confirmar_senha"].value():
                messages.error(request, "As senhas não coincidem.")
                return redirect('cadastro')
            
            nome = form["nome"].value()
            cnpj = form["cnpj"].value()
            email = form["email"].value()  
            senha = form["senha"].value()

            # Verifica se já existe e-mail
            if User.objects.filter(email=email).exists():
                messages.error(request, "Este e-mail já está cadastrado.")
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha,
            )
            usuario.save()

            Profile.objects.get_or_create(user=usuario, defaults={'cnpj': cnpj})
            messages.success(request, "Cadastro realizado com sucesso! Faça login.")
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('login')

def inicio(request):



    return render(request, 'usuarios/inicio.html')

@login_required
def perfil(request):
    # Pega todos os logins sociais do usuário
    social_accounts = SocialAccount.objects.filter(user=request.user)

    dados = {}
    for conta in social_accounts:
        provider = conta.provider  # 'facebook' ou 'slack'
        extra_data = conta.extra_data  # dados recebidos do provedor
        dados[provider] = extra_data

    return render(request, 'perfil.html', {'dados': dados})