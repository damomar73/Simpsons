import time
import json
import requests
import csv
import os
from pathlib import Path

def obtenerImagen():
     while True:
        time.sleep(1)
        URL_API=f'https://thesimpsonsquoteapi.glitch.me/quotes'
        respuesta=requests.get(URL_API)
        fraseSimpsons=respuesta.json()
        datos = {"Nombre": fraseSimpsons[0]['character'],"Frase":fraseSimpsons[0]['quote'],"Imagen":fraseSimpsons[0]['image']}
        datos_csv = {"Nombre": fraseSimpsons[0]['character'],"Frase":fraseSimpsons[0]['quote']}

        #comprobamos que la impresion es correcta
        #print (datos)  
        personaje = datos['Nombre']
        
        #comprobamos que imprime el nombre del personaje
        #print(personaje)

        personaUnida = personaje.replace(" ", "")        
        #comprobamos que eliminan los caracteres en blanco y une las palabras del personaje
        #print(personaUnida)
    
        #creamos la ruta personaje/personaje
        #join = "/".join([personaje,personaje])
        #creamos la ruta personaje.csv
        joincsv = ''.join([personaje,".csv"])
        #eliminanos los espacios en blanco del nombre del archivo csv
        unioncsv = joincsv.replace(" ", "")
        joinpng = ''.join([personaje,".png"])
        #eliminanos los espacios en blanco del nombre del archivo png
        unionpng = joinpng.replace(" ", "")
        #print(unioncsv)
        #print(unionpng)

            #image = ''.join([join,".png"])
            #unionimagen = image.replace(" ", "")
            #filecsv = ''.join([join,".csv"])
            #unionruta = filecsv.replace(" ", "")
        #comprobamos que se imprime correctamente la ruta del archivo csv y png
        #print(unionimagen)
        #print(unionruta)
        

        #creamos las carpetas de los distintos personajes y evitamos los errores al detectar que ya existe 
        os.makedirs(personaUnida,exist_ok=True)

        #creamos la ruta desde la carpeta actual
        ruta = Path(personaUnida)
        #print(ruta)


        ruta_con_csv = ruta.joinpath(unioncsv).resolve()
        ruta_con_png = ruta.joinpath(unionpng).resolve()


        #comprobamos las rutas  tanto del archivo csv como png
        print(ruta_con_csv)
        #print(ruta_con_png)

        #creamos los archivos csv en las carpetas de cada personaje
        with open(ruta_con_csv,'a') as l:
            #personaUnida = csv.DictWriter(l, datos.keys())
            personaUnida = csv.DictWriter(l, datos_csv.keys())
            #personaUnida.writerow(datos)
            personaUnida.writerow(datos_csv)

        #creamos los archivos png en las carpetas de cada personaje
        with open(ruta_con_png,'wb') as g:
            g.write(requests.get(datos['Imagen']).content)
                
obtenerImagen()

'''
listaPalabras = cadenaPalabras.split()

frecuenciaPalab = []
for w in listaPalabras:
    frecuenciaPalab.append(listaPalabras.count(w))

print("Cadena\n" + cadenaPalabras +"\n")
print("Lista\n" + str(listaPalabras) + "\n")
print("Frecuencias\n" + str(frecuenciaPalab) + "\n")
print("Pares\n" + str(list(zip(listaPalabras, frecuenciaPalab))))

'''


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

