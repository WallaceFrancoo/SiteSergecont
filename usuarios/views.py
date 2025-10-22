from django.shortcuts import render, redirect
from usuarios.forms import LoginForm, CadastroForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages

# Create your views here.
def login(request):
    form = LoginForm()
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

def inicio(request):
    return render(request, 'usuarios/inicio.html')