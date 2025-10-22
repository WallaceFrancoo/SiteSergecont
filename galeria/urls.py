from django.urls import path
from galeria.views import index, imagem, aplicativos, buscar, AbaAplicativos, FaleConosco

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('aplicativos/<int:foto_id>', aplicativos, name='aplicativos'),
    path("buscar", buscar, name="buscar"),
    path("AbaAplicativos", AbaAplicativos, name="AbaAplicativos"),
    path("FaleConosco", FaleConosco, name="FaleConosco"),
]
