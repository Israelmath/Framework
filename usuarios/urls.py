from django.urls import path
from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('cria/receita', views.criaReceita, name='criaReceita'),
    path('deleta/<int:receita_id>', views.deletaReceita, name='deletaReceita'),
    path('edita/<int:receita_id>', views.editaReceita, name='editaReceita'),
]