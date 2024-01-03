from rest_framework import serializers

from policia.models import policia, rango, especialidad


class PoliciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = policia
        fields = ('id', 'url', 'nombres', 'apellidos', 'edad', 'cedula', 'puesto', 'especialista', 'activo')


class RangoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = rango
        fields = ('id', 'url', 'cargo', 'area', 'tiempo', 'sector')


class EspecialidadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = especialidad
        fields = ('id', 'url', 'nombre', 'descripcion', 'nivel_academico')
