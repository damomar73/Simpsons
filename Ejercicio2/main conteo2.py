import time
import requests
import csv
import os
import re
import pandas as pd
from pathlib import Path


def obtenerImagen():
    listaPalabras = list()
    listaFrecuencia = list()
    frequency = {}
    dicc = {}
    diccionario = dict()

    while True:
        time.sleep(5)
        URL_API=f'https://thesimpsonsquoteapi.glitch.me/quotes'
        respuesta=requests.get(URL_API)
        fraseSimpsons=respuesta.json()
        datos = {"Nombre": fraseSimpsons[0]['character'],"Frase":fraseSimpsons[0]['quote'],"Imagen":fraseSimpsons[0]['image']}
        datos_csv = {"Frase":fraseSimpsons[0]['quote']}
        #comprobamos la impresion correcta de la frase
        #print (datos_csv)
        
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

        #comprobamos las rutas tanto del archivo .csv como .png
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
        text_upper = documento_datos.upper()
        textUpper = re.sub(r'[.,"\-?:!;]', '', text_upper)
        document_text=textUpper.split()
        print(document_text)  
        #       
        #match_pattern = re.findall(r'\w+', document_text)
        #print(match_pattern)

        #for word in match_pattern:
        '''
        for word in document_text:
            count = frequency.get(word,0)
            frequency[word] = count + 1
            frequency_list = frequency.keys()
            #print (frequency_list)
'''

        items = pd.Series(document_text).value_counts().sort_values(ascending=False).reset_index()
        items.columns = ['items', '#counts']
        #df.to_csv(r'ConteoPalabras.csv',header=True,index=False)
        df = items.to_frame(name = 'Cantidad')
        df.index.name = 'Palabra'
        df.to_csv('ConteoPalabras.csv', index=False)

'''     
        for p in document_text:
            diccionario[p] = diccionario.get(p, 0) + 1
            print(p,diccionario[p])
        print(diccionario)
        


        for words in frequency_list:
            if words in dicc:
                dicc[words] = frequency[word] + 1
            else:                
                dicc[words] = frequency[word]
                #print (words, dicc[words])
                #print (words, frequency[word])         

        #listaConteo.append(frequency_list)
        listaPalabras.append(words)
        listaFrecuencia.append(dicc[words])
        conteoFile = open(r'ConteoPalabras.csv','a')
        conteo = csv.writer(conteoFile)
        conteo.writerows(listaPalabras)
        #conteo.writerows(listaFrecuencia)
    '''

obtenerImagen()



# Use counter most_common to get most popular 50
#print(cnts.most_common(50)) 