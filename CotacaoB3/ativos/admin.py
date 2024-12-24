from django.contrib import admin
from .models import Ativo

@admin.register(Ativo)
class AtivoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Ativo._meta.fields]