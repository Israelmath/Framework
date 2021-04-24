from django.db import models
from datetime import datetime


class Receita(models.Model):
    nomeReceita = models.CharField(max_length=40)
    ingredientes = models.TextField()
    modoPreparo = models.TextField()
    tempoPreparo = models.IntegerField()
    rendimento = models.CharField(max_length=40)
    categoria = models.CharField(max_length=30)
    dataCadastro = models.DateTimeField(default=datetime.now(), blank=True)


