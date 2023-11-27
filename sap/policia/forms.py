from django.forms import ModelForm

from policia.models import policia


class PoliciaFormulario(ModelForm):
    class meta:
        model = policia
        fields = ('nombres', 'apellidos', 'edad', 'cedula', 'puesto' 'especialista', 'activo')
