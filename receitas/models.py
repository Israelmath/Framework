from django.db import models
from datetime import datetime
from pessoas.models import Pessoa
from django.contrib.auth.models import User


class Receita(models.Model):
    autor = models.ForeignKey(User, models.CASCADE)
    nomeReceita = models.CharField(max_length=40)
    ingredientes = models.TextField()
    modoPreparo = models.TextField()
    tempoPreparo = models.IntegerField()
    rendimento = models.CharField(max_length=40)
    categoria = models.CharField(max_length=30)
    publicada = models.BooleanField(default=False)
    img = models.ImageField(upload_to='thumbnails/%d/%m/%Y', blank=True)
    dataCadastro = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.nomeReceita


