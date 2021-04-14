from django.db import models


class Puesto(models.Model):
    nombre = models.CharField(max_length=200)

