from django.db import models

# Create your models here.


class Ventas(models.Model):
    fecha       = models.DateField()
    comentarios = models.TextField()


