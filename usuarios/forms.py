from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    login = forms.CharField(max_length=150, label='E-mail', required=True, widget=forms.EmailInput(attrs={
            'class': 'form-control',  # mantém sua classe bonita
            'placeholder': 'Digite seu e-mail'
        }))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha',
            'autocomplete': 'new-password'
        }), label='Senha', required=True)

class CadastroForm(forms.Form):
    nome = forms.CharField(max_length=150, label='Nome', required=True, widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu nome'
        }))
    cnpj = forms.CharField(max_length=18, label='CNPJ', required=True, widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu CNPJ'
        }))
    email = forms.EmailField(label='E-mail', required=True, widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu e-mail'
        }))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha',
            'autocomplete': 'new-password'
        }), label='Senha', required=True)
    confirmar_senha = forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirme sua senha',
            'autocomplete': 'new-password'
        }), label='Confirmar Senha', required=True)