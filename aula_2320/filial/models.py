from django.db import models


class Filial(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome
