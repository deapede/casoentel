from django.db import models

# Create your models here.


class Vendedores(models.Model):
    nombreCompleto  = models.TextField()
    fechaNacimiento = models.DateTimeField()
