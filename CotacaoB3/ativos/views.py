from django.shortcuts import render, redirect
from .models import Ativo
from .forms import FormularioAtivo

def listar_ativos(request):
    ativos = Ativo.objects.all()
    return render(request, 'ativos/listar_ativos.html', {'ativos': ativos})

def cadastrar_ativos(request):
    if request.method == 'POST':
        form = FormularioAtivo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_ativos')
    else:
        form = FormularioAtivo()
    return render(request, 'ativos/cadastrar_ativo.html', {'form': form})
