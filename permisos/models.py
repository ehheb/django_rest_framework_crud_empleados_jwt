from django.db import models
from empleados.models import Empleado


class Permiso(models.Model):
    nombre = models.CharField(max_length=200)

    empleado = models.ForeignKey(
        Empleado,
        related_name='permisos',
        on_delete=models.SET_NULL,
        null=True
    )
