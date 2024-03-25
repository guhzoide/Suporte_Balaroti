from django.contrib import admin
from tutoriais.models import cadastroTutoriais

class listandoTutoriais(admin.ModelAdmin):
    list_display = ("id", "titulo", "publicada",)
    list_display_links = ("titulo",)
    search_fields = ("titulo",)
    list_filter = ("publicada",)
    list_per_page = 15
    
admin.site.register(cadastroTutoriais, listandoTutoriais)
