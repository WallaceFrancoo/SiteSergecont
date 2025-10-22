from django.shortcuts import render, get_object_or_404
from galeria.models import Empresas, Programas

def index(request):
    programas = Programas.objects.order_by('-dataCriacao').filter(ativo=True)
    return render(request, 'galeria/index.html',{"cards": programas})

def imagem(request,foto_id):
    programas = get_object_or_404(Programas, pk=foto_id)
    return render(request, 'galeria/imagem.html',{"programas": programas})

def aplicativos(request,foto_id):
    programas = get_object_or_404(Programas, pk=foto_id)
    return render(request, 'galeria/aplicativos.html',{"programas": programas})

def AbaAplicativos(request):
    programas = Programas.objects.order_by('-dataCriacao').filter(ativo=True)
    return render(request, 'galeria/aplicativos.html',{"cards": programas})


def buscar(request):
    programas = Programas.objects.order_by('-dataCriacao').filter(ativo=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            programas = programas.filter(nome__icontains=nome_a_buscar)
    return render(request, 'galeria/buscar.html', {"cards": programas})

def FaleConosco(request):
    return render(request, 'galeria/FaleConosco.html')