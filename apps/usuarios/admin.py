from django.contrib import admin
from apps.usuarios.models import cadastroCodigoOmni

class listandoCodigoOmni(admin.ModelAdmin):
    list_display = ("numero", "descricao" , "codigo", "acesso")
    list_display_links = ("numero", "descricao")
    search_fields = ("numero", "descricao", "codigo")
    list_per_page = 15

admin.site.register(cadastroCodigoOmni, listandoCodigoOmni)