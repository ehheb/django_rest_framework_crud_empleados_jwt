from django.db import models
from puestos.models import Puesto

class Empleado(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

    puesto = models.ForeignKey(
        Puesto,
        related_name='empleados',
        on_delete=models.SET_NULL,
        null=True
    )


