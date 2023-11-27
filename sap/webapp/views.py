from django.http import HttpResponse
#from django.shortcuts import render
from django.template import loader

from policia.models import policia


#from policia.models import policia


# Create your views here.
def bienvenida(request):
    return HttpResponse ('Saludos')
'''''
def despedida(request):
    return HttpResponse ('<!DOCTYPE html>'
                         '<html><head></head><body><h1>Chao</h1></body>'
                         '</html>')


def mostrar_edad(request, edad):
    calculo_edad = 20 + edad
    return HttpResponse(f'Tu edad despues de 20 años será: {calculo_edad}')
'''''


def bienvenida2(request):
    cantidad_policias = policia.objects.count()
    policias = policia.objects.all()
    #print(f'Cantidad policias: {cantidad_policias}')
    #print(policias)

    dict_datos = {'cantidad_policias':cantidad_policias, 'policias':policias}
    pagina = loader.get_template('bienvenida.html')
    return HttpResponse(pagina.render(dict_datos,request))
