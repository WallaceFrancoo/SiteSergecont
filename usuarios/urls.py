from django.urls import path
from usuarios.views import login, cadastro, inicio

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('inicio', inicio , name='inicio')
]

