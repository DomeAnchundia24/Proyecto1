import requests
from bs4 import BeautifulSoup
import pandas as pd


nombres = list()
apellidos = list()
especialidad = list()
rango = list()
url = 'http://127.0.0.1:8000/'
html_doc = requests.get(url)
print(html_doc)
soup = BeautifulSoup(html_doc.text, 'html.parser')
# data = soup.find_all('td',attrs={"class": "table-primary"})
# i=0
# # print(data)
#
# while(i+2<len(data)):
#     nombres.append(data[i].text)
#     apellidos.append(data[i+1].text)
#     especialidad.append(data[i+2].text)
#     rango.append(data[i+2].text)
#     i+=3

# for d in data:
#     nombres.append(data[i])
#     apellidos.append(data[i])
#     especialidad.append(data[i])
#     rango.append(data[i])
#     i+=1

tabla = soup.find('table')
# print(tabla)
# Obtener las filas de la tabla
filas = tabla.find_all('tr')
# print(filas)
# Iterar sobre las filas e imprimir los datos
for fila in filas:
    # # Obtener las celdas de la fila
    celdas = fila.find_all('td')
    print(celdas)
    if len(celdas)>0:
        nombres.append(celdas[0].string)
        apellidos.append(celdas[1].string)
        especialidad.append(celdas[5].string)
        rango.append(celdas[4].string)

print(apellidos)
print(nombres)
print(especialidad)
print(rango)

df = pd.DataFrame({'Nombres':nombres,'Apellidos':apellidos,'Especialidad':especialidad,'Rango':rango})
df.to_csv('policias.csv', index=False, encoding='utf-8')
