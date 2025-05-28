from django.db import models
from setor.models import Setor


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    data = models.DateTimeField(auto_now_add=True)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
