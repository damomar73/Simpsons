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
            if i['character'] == 'Lisa Simpson':
                listaLisa.append(fraseSimpsons)
                with open('Lisa/lisa.csv','a') as lisaFile:
                    lisa = csv.writer(lisaFile, listaLisa.keys())
                    lisa.writerows(listaLisa)
            elif i['character'] == 'Homer Simpson':
                listaHomer.append(fraseSimpsons)
                with open('Homer/homer.csv','a') as homerFile:
                    homer = csv.writer(homerFile, listaHomer.keys())
                    homer.writerows(listaHomer)
            else:
                listaGeneral.append(fraseSimpsons)
                with open('General/general.csv','a') as generalFile:
                    general = csv.writer(generalFile, listaGeneral.keys())
                    general.writerows(listaGeneral)
                
#if __name__ == '__main__':
obtenerFrase()