from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError

def validar_arquivo_excel(value):
    if not value.name.endswith(('.xlsx','xls')):
        raise ValidationError('Apenas arquivos .xlsx são permitidos.')
# Create your models here.
class Empresas(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(null=False, blank=False)
    numero = models.CharField(null=False, blank=False)
    ativo = models.BooleanField(default=True)
    dataCriacao = models.DateTimeField(default=datetime.now, blank=False)
    PlanoDeContas = models.FileField(upload_to='planoDeContas/', null=True, blank=True, validators=[validar_arquivo_excel])

    def __str__(self):
        return self.nome


class Programas(models.Model):
    nome = models.CharField(max_length=100,null=False, blank=False)
    info = models.TextField(null=False, blank=False)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    ativo = models.BooleanField(default=False)
    dataCriacao = models.DateTimeField(default=datetime.now, blank=False)
    
    def __str__(self):
        return self.nome


