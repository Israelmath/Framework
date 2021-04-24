from django.shortcuts import render

# Create your views here.


def index(request):
    receitas = {
        1: 'Lasanha',
        2: 'Feijoada',
        3: 'Panqueca',
        4: 'Receita'
    }

    dados = {
        'nomeReceitas': receitas
    }
    return render(request, 'index.html', context=dados)

def receita(request):
    return render(request, 'receita.html')