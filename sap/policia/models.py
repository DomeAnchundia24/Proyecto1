from django.db import models


class rango(models.Model):
    cargo = models.CharField(max_length=20, null=True)
    area = models.CharField(max_length=50, null=True)
    tiempo = models.IntegerField(max_length=20, null=True)
    sector = models.CharField(max_length=150, null=True)

    def __str__(self):
        return f'{self.cargo} '


class especialidad(models.Model):
    nombre = models.CharField(max_length=20, null=True)
    descripcion = models.CharField(max_length=20, null=True)
    nivel_academico = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.nombre}'


class policia(models.Model):
    nombres = models.CharField(max_length=20, null=True)
    apellidos = models.CharField(max_length=20, null=True)
    edad = models.CharField(max_length=20, null=True)
    cedula = models.CharField(max_length=20, null=True)
    puesto = models.ForeignKey(rango, on_delete=models.SET_NULL, null=True)
    especialista = models.ForeignKey(especialidad, on_delete=models.SET_NULL, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id} - {self.apellidos} {self.nombres}'
