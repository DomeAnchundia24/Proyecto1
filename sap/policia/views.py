import pandas as pd
from bs4 import BeautifulSoup
import requests
from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404, render
from django.template import loader
from rest_framework import viewsets, permissions

from policia.models import policia, rango, especialidad
from policia.forms import PoliciaFormulario
from policia.serializers import PoliciaSerializer, RangoSerializer, EspecialidadSerializer

PoliciaFormulario = modelform_factory(policia, exclude=['activo', ])


def agregar_policia(request):
    pagina = loader.get_template('agregar.html')
    if request.method == 'GET':
        formulario = PoliciaFormulario
    elif request.method == 'POST':
        formulario = PoliciaFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    datos = {'formulario': formulario}
    return HttpResponse(pagina.render(datos, request))


def modificar_policia(request, id):
    pagina = loader.get_template('modificar.html')
    policia_instance = get_object_or_404(policia, pk=id)  # Cambia la referencia a la clase Policia
    if request.method == 'GET':
        formulario = PoliciaFormulario(instance=policia_instance)
    elif request.method == 'POST':
        formulario = PoliciaFormulario(request.POST, instance=policia_instance)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    datos = {'formulario': formulario}
    return HttpResponse(pagina.render(datos, request))


def ver_policia(request, id):
    policia_instance = get_object_or_404(policia, pk=id)  # Cambia la referencia a la clase Policia
    datos = {'policia': policia_instance}
    pagina = loader.get_template('ver.html')
    return HttpResponse(pagina.render(datos, request))


def eliminar_policia(request, id):
    policia_instance = get_object_or_404(policia, pk=id)  # Cambia la referencia a la clase Policia
    if policia_instance:  # Reemplaza "if policia:" por "if policia_instance:"
        policia_instance.delete()
        return redirect('inicio')

'''
def descargar_registro(request):
    nombres = list()
    apellidos = list()
    especialidad = list()
    rango = list()
    url = 'http://127.0.0.1:8000/'
    html_doc = requests.get(url)
    print(html_doc)
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    tabla = soup.find('table')
    filas = tabla.find_all('tr')
    for fila in filas:
        celdas = fila.find_all('td')
        print(celdas)
        if len(celdas) > 0:
            nombres.append(celdas[0].string)
            apellidos.append(celdas[1].string)
            especialidad.append(celdas[5].string)
            rango.append(celdas[4].string)
    df = pd.DataFrame({'Nombres': nombres, 'Apellidos': apellidos, 'Especialidad': especialidad, 'Rango': rango})
    df.to_csv('policias.csv', index=False, encoding='utf-8')
'''

from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import pandas as pd


def descargar_registro(request):
    nombres = []
    apellidos = []
    especialidad = []
    rango = []
    url = 'http://127.0.0.1:8000/'
    html_doc = requests.get(url)
    soup = BeautifulSoup(html_doc.text, 'html.parser')

    tabla = soup.find('table')
    filas = tabla.find_all('tr')

    for fila in filas:
        celdas = fila.find_all('td')
        if len(celdas) > 0:
            nombres.append(celdas[0].string)
            apellidos.append(celdas[1].string)
            especialidad.append(celdas[5].string)
            rango.append(celdas[4].string)
    df = pd.DataFrame({
        'Nombres': nombres,
        'Apellidos': apellidos,
        'Especialidad': especialidad,
        'Rango': rango
    })
    csv_data = df.to_csv(index=False, encoding='utf-8')
    response = HttpResponse(csv_data, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="policias.csv"'

    return response
class PoliciaViewSet(viewsets.ModelViewSet):
    queryset = policia.objects.all().order_by('-apellidos')
    serializer_class = PoliciaSerializer
    permission_classes = [permissions.IsAuthenticated]
class RangoViewSet(viewsets.ModelViewSet):
    queryset = rango.objects.all()
    serializer_class = RangoSerializer
    permission_classes = [permissions.IsAuthenticated]
class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = especialidad.objects.all()
    serializer_class = EspecialidadSerializer
    permission_classes = [permissions.IsAuthenticated]
