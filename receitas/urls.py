from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:receita_id>', views.receita, name='receita'),
    path('buscar', views.buscar, name='buscar'),
    path('cria/receita', views.criaReceita, name='criaReceita'),
    path('deleta/<int:receita_id>', views.deletaReceita, name='deletaReceita'),
    path('edita/<int:receita_id>', views.editaReceita, name='editaReceita'),
    path('atualiza', views.atualizaReceita, name='atualizaReceita'),
]