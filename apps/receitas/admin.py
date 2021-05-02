from django.contrib import admin
from .models import Receita


class Listandoreceitas(admin.ModelAdmin):
    list_display = ('id', 'nomeReceita', 'tempoPreparo', 'publicada')
    list_display_links = ('id', 'nomeReceita',)
    search_fields = (['nomeReceita'])
    list_filter = (['categoria'])
    list_per_page = 15

    list_editable = (['publicada'])


admin.site.register(Receita, Listandoreceitas)