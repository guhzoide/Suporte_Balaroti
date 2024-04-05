from django.contrib import admin
from apps.programas.models import status

class listandoStatus(admin.ModelAdmin):
    list_display = ("id", "titulo" ,"status_atual",)
    list_display_links = ("id", "titulo",)

admin.site.register(status, listandoStatus)