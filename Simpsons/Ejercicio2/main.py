import time
import json
import requests
import csv

def obtenerImagen():
     while True:
        time.sleep(1)
        URL_API=f'https://thesimpsonsquoteapi.glitch.me/quotes'
        respuesta=requests.get(URL_API)
        fraseSimpsons=respuesta.json()
        datos = {"Nombre": fraseSimpsons[0]['character'],"Frase":fraseSimpsons[0]['quote'],"Imagen":fraseSimpsons[0]['image']}
        print (datos)
        if 'Lisa' in datos['Nombre']:
            with open(r'Lisa/lisa.csv','a') as l:
                lisa = csv.DictWriter(l,datos.keys())
                lisa.writerow(datos)
            with open('Lisa/lisa.png', 'wb') as l:
                l.write(requests.get(datos['Imagen']).content)
        elif 'Homer' in datos['Nombre']:
            with open(r'Homer/homer.csv','a') as l:
                homer = csv.DictWriter(l, datos.keys())
                homer.writerow(datos)
            with open('Homer/homer.png', 'wb') as h:
                    h.write(requests.get(datos['Imagen']).content)
        else:
            
            name = datos['Nombre']
            print(name)
            join = '/'.join([name,name])
            image = ''.join(["'",join,".png'"])
            unionimagen = image.replace(" ", "")
            ruta = ''.join(["'",join,".csv'"])
            unionruta = ruta.replace(" ", "")
            print(unionimagen)
            print(unionruta)
            #with open (r'datos['Nombre']')
            #with open(unionruta,'a') as l:
             #   general = csv.DictWriter(l, datos.keys())
              #  general.writerow(datos)
            #with open(unionimagen,'wb') as g:
             #   g.write(requests.get(datos['Imagen']).content)
                
obtenerImagen()

'''
import re

contador = {}
patron = re.compile(r"(\w+)")
with open("quijote.txt", "r") as texto:
    for linea in texto.readlines():
        m = patron.findall(linea)
        for palabra in m:
            palabra = palabra.lower()
            if palabra in contador:
                contador[palabra] += 1
            else:
                contador[palabra] = 1
print(contador)
'''

