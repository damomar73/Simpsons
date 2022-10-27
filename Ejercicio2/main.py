import time
import requests
import csv
import os
import re
from pathlib import Path

frequency = {}

def obtenerImagen():
     while True:
        time.sleep(30)
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
    
        #creamos la ruta personaje.csv y personaje.png
        joincsv = ''.join([personaje,".csv"])
        joinpng = ''.join([personaje,".png"])

        #eliminanos los espacios en blanco del nombre del archivo csv
        unioncsv = joincsv.replace(" ", "")
        
        #eliminanos los espacios en blanco del nombre del archivo png
        unionpng = joinpng.replace(" ", "")
        #print(unioncsv)
        #print(unionpng)

        #creamos las carpetas de los distintos personajes y evitamos los errores al detectar que ya existe 
        os.makedirs(personaUnida,exist_ok=True)

        #creamos la ruta desde la carpeta actual
        ruta = Path(personaUnida)
        #print(ruta)

        ruta_con_csv = ruta.joinpath(unioncsv).resolve()
        ruta_con_png = ruta.joinpath(unionpng).resolve()

        #comprobamos las rutas  tanto del archivo csv como png
        #print(ruta_con_csv)
        #print(ruta_con_png)

        #creamos los archivos .csv en las carpetas de cada personaje
        with open(ruta_con_csv,'a') as l:
            personaUnida = csv.DictWriter(l, datos_csv.keys())
            personaUnida.writerow(datos_csv)

        #creamos los archivos .png en las carpetas de cada personaje
        with open(ruta_con_png,'wb') as g:
            g.write(requests.get(datos['Imagen']).content)

        documento_datos = datos['Frase']
        print(documento_datos)
        #convertimos las letras en mayusculas
        text_upper = documento_datos.upper()
        #eliminamos los caracteres no necesarios para poder distinguir correctamente las palabras
        textUpper = re.sub(r'[.,"\-?:!;&]', '', text_upper)
        #separamos las palabras de las frases
        document_text=textUpper.split()
        #print(document_text)  

        #creamos contador de frecuencia de palabras
        for word in document_text:
            count = frequency.get(word,0)
            frequency[word] = count + 1
        
        #comprobamos las keys del diccionario "frequency"
        #frequency_list = frequency.keys()
        #print (frequency_list)

        #comprobamos que se imprime la palabra y su frecuencia en cada quote
        #for words in frequency_list:
            #print (words, frequency[words])

        #creamos el archivo csv de conteo de palabras
        with open('ConteoPalabras.csv', 'w', newline='') as cp:
            writer = csv.writer(cp,delimiter=';')
            for k, v in frequency.items():
                writer.writerow([k,v])

if __name__ == "__main__":   
    obtenerImagen()

