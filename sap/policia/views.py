from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404, render
from django.template import loader
from policia.models import policia
from policia.forms import PoliciaFormulario

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
