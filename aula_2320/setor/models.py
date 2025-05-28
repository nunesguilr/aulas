from django.db import models
from filial.models import Filial

class Setor(models.Model):
    nome = models.CharField(max_length=100)
    filiais = models.ManyToManyField(Filial, related_name='setores') 

    def __str__(self):
        return self.nome