from datetime import datetime

from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Receita
from django.contrib.auth.models import User


def index(request):

    receitas = Receita.objects.order_by('-dataCadastro').filter(publicada=True)

    dados = {
        'receitas': receitas
    }
    return render(request, 'receitas/index.html', context=dados)

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

def criaReceita(request):
    if request.method == 'POST':
        nomeReceita = request.POST['nomeReceita']
        ingredientes = request.POST['ingredientes']
        modoPreparo = request.POST['modoPreparo']
        tempoPreparo = request.POST['tempoPreparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        img = request.FILES['img']

        user = get_object_or_404(User, pk=request.user.id)

        receita = Receita.objects.create(
            autor=user,
            nomeReceita=nomeReceita,
            ingredientes=ingredientes,
            modoPreparo=modoPreparo,
            tempoPreparo=tempoPreparo,
            rendimento=rendimento,
            categoria=categoria,
            img=img,
            dataCadastro=datetime.now()
            )
        receita.save()

        return redirect('dashboard')
    else:
        return render(request, 'receitas/criaReceita.html')

def deletaReceita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')

def editaReceita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receitaAEditar = {'receita': receita}
    return render(request, 'receitas/editareceita.html', receitaAEditar)

def atualizaReceita(request):
    if request.method == 'POST':
        receitaId = request.POST['receita_id']
        receita = Receita.objects.get(pk=receitaId)
        receita.nomeReceita = request.POST['nomeReceita']
        receita.ingredientes = request.POST['ingredientes']
        receita.modoPreparo = request.POST['modoPreparo']
        receita.tempoPreparo = request.POST['tempoPreparo']
        receita.rendimento = request.POST['rendimento']
        receita.categoria = request.POST['categoria']
        if 'img' in request.FILES:
            receita.img = request.FILES['img']
        receita.save()

    return redirect('dashboard')