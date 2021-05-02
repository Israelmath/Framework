from .receitas import Receita, index
from django.shortcuts import render


def buscar(request):
    listaReceitas = Receita.objects.order_by('-dataCadastro').filter(publicada=True)

    if 'buscar' in request.GET:
        nomeABuscar = request.GET['buscar']
        listaReceitas = listaReceitas.filter(nomeReceita__icontains=nomeABuscar)

    dados = {
        'receitas': listaReceitas
    }
    if len(dados) == 0:
        index(request)
    else:
        return render(request, 'receitas/buscar.html', context=dados)
