import time
import json
import requests
import csv

def obtenerFrase():
    listaLisa = list()
    listaHomer = list()
    listaGeneral = list ()

    while True:
        time.sleep(1)
        URL_API=f'https://thesimpsonsquoteapi.glitch.me/quotes'
        respuesta=requests.get(URL_API)
        fraseSimpsons=respuesta.json()
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