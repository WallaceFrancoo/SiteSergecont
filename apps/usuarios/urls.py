from django.urls import path
from apps.usuarios.views import login, cadastro, inicio, logout

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('inicio', inicio , name='inicio'),
    path('logout', logout , name='logout')
]

