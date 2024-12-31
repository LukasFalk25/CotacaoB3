from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_ativos, name='listar_ativos'),
    path('cadastrar/', views.cadastrar_ativos, name='cadastrar_ativo'), 
]