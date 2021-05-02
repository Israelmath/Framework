from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Receita


def index(request):

    receitas = Receita.objects.order_by('-dataCadastro').filter(publicada=True)

    dados = {
        'receitas': receitas
    }
    return render(request, 'index.html', context=dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receitaAExibir = {
        'receita': receita
    }
    return render(request, 'receita.html', receitaAExibir)

def buscar(request):
    listaReceitas = Receita.objects.order_by('-dataCadastro').filter(publicada=True)

    if 'buscar' in request.GET:
        nomeABuscar = request.GET['buscar']
        if buscar:
            listaReceitas = listaReceitas.filter(nomeReceita__icontains=nomeABuscar)

    dados = {
        'receitas': listaReceitas
    }
    if len(dados) == 0:
        index(request)
    else:
        return render(request, 'buscar.html', context=dados)
