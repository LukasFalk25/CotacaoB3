from django.contrib import admin
from .models import Ativo
from .models import Cotacao

@admin.register(Ativo)
class AtivoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Ativo._meta.fields]
    
admin.site.register(Cotacao)
