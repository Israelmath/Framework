from django.db import models
from datetime import datetime
from pessoas.models import Pessoa


class Receita(models.Model):
    autor = models.ForeignKey(Pessoa, models.CASCADE)
    nomeReceita = models.CharField(max_length=40)
    ingredientes = models.TextField()
    modoPreparo = models.TextField()
    tempoPreparo = models.IntegerField()
    rendimento = models.CharField(max_length=40)
    categoria = models.CharField(max_length=30)
    publicada = models.BooleanField(default=False)
    dataCadastro = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.nomeReceita


