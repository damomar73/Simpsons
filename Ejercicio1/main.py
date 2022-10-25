import time
import json
import requests
import csv

#definimos la funcion y creamos 3 listas en blanco, una para Homer, otra para Lisa y una General
def obtenerFrase():
    listaLisa = list()
    listaHomer = list()
    listaGeneral = list()

    while True:
        time.sleep(30)
        URL_API=f'https://thesimpsonsquoteapi.glitch.me/quotes'
        respuesta=requests.get(URL_API)
        fraseSimpsons=respuesta.json()

#ejecutamos un bucle donde primero creamos el fichero general.csv, a continuacion lisa.csv y finalmemte homer.csv
#en estos ficheros se almacena la frases de los personajes, en general todas y en lisa y homer las de cada uno de ellos
        for i in fraseSimpsons:
            listaGeneral.append(fraseSimpsons)
            generalFile = open(r'General/general.csv','a')
            general = csv.writer(generalFile)
            general.writerows(listaGeneral)

            if i['character'] == 'Lisa Simpson':
                listaLisa.append(fraseSimpsons)
                lisaFile = open(r'Lisa/lisa.csv','a')
                lisa = csv.writer(lisaFile)
                lisa.writerows(listaLisa)

            elif i['character'] == 'Homer Simpson':
                listaHomer.append(fraseSimpsons)
                homerFile = open(r'Homer/homer.csv','a')
                homer = csv.writer(homerFile)
                homer.writerows(listaHomer)
                     
obtenerFrase()