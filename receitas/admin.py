from django.contrib import admin
from .models import Receita

class Listandoreceitas(admin.ModelAdmin):
    list_display = ('id', 'nomeReceita', 'tempoPreparo')
    list_display_links = ('id', 'nomeReceita',)


admin.site.register(Receita, Listandoreceitas)