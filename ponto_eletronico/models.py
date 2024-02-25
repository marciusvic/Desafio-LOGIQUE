from django.db import models
from django.contrib.auth.models import AbstractUser

class Empresa(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)

class CustomUser(AbstractUser):
    nome = models.CharField(max_length=100, blank=False, null=False)
    cpf = models.CharField(max_length=11, unique=True, blank=False, null=False)
    date_nascimento = models.DateField(blank=False, null=False)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, blank=False, null=False)
    regime_horas = models.IntegerField(blank=False, null=False, default=8)

class PontoEletronico(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False, null=False)
    data = models.DateField(blank=False, null=False)
    hora = models.TimeField(blank=False, null=False)