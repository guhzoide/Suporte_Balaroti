from django.contrib import admin
from apps.lojas.models import cadastroLojas, cadastroCameras, cadastroEtiquetas

class listandoLojas(admin.ModelAdmin):
    list_display = ("id", "numero", "loja", "regiao", "cd", "cnpj" , "tronco", "categoria", "publicada")
    list_display_links = ("numero", "loja")
    search_fields = ("numero", "loja", "cnpj", "regiao")
    list_filter = ("categoria", "publicada")
    list_per_page = 15

class listandoCameras(admin.ModelAdmin):
    list_display = ("id", "numero", "loja", "ip", "publicada")
    list_display_links = ("numero", "loja")
    search_fields = ("numero", "loja")
    list_filter = ("publicada",)
    list_per_page = 15

class listandoEtiquetas(admin.ModelAdmin):
    list_display = ("id", "numero", "loja", "ip_etiqueta", "publicada")
    list_display_links = ("numero", "loja")
    search_fields = ("numero", "loja")
    list_filter = ("publicada",)
    list_per_page = 15

admin.site.register(cadastroLojas, listandoLojas)
admin.site.register(cadastroCameras, listandoCameras)
admin.site.register(cadastroEtiquetas, listandoEtiquetas)