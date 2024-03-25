from django.contrib import admin
from links.models import cadastroLinks

class listandoLinks(admin.ModelAdmin):
    list_display = ("nome", "link", "publicada",)
    list_display_links = ("nome", "publicada",)
    search_fields = ("nome",)
    list_filter = ("publicada",)
    list_per_page = 15

admin.site.register(cadastroLinks, listandoLinks)
