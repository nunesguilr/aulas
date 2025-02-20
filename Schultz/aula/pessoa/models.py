from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=120)
    idade = models.IntegerField()