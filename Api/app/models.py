from django.db import models


class Contato(models.Model):
    nome = models.CharField(max_length=150, blank=False, default='')
    idade = models.CharField(max_length=3, blank=False, default='')
    telefone = models.CharField(max_length=15, blank=False, default='')
    ativo = models.BooleanField(default=False)
