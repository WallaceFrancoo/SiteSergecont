from django.contrib import admin
from apps.galeria.models import Empresas, Programas

class ListandoEmpresas(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'numero','ativo') 
    list_display_links = ('nome','numero')
    search_fields = ('numero','cnpj','nome')
    list_editable = ('ativo',)
    list_filter = ('ativo',)

class ListandoProgramas(admin.ModelAdmin):
    list_display = ('nome', 'info','ativo') 
    list_display_links = ('nome',)
    search_fields = ('nome','ativo')
    list_editable = ('ativo',)
    list_filter = ('ativo',)
# O correto:
admin.site.register(Empresas, ListandoEmpresas)
admin.site.register(Programas, ListandoProgramas)

  