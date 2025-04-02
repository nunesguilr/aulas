from django.db import models
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    cidade = models.CharField(max_length=100, null=False, default="Guanambi")
    estado = models.CharField(max_length=100, default="Bahia")
    data = models.DateField(default='2023-01-01', null=False)
    