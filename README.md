# Ejercicios Fundamentos - Directorio SIMPSONS
***
## Ejercicio 1 (MAGGIE LEVEL)
***
### Pasos (Maggie Level)

_1. Usando google colab crear un notebook que consuma la api de los simpsons y haga una consulta cada 30seg a la API_

_2. El código debe guardar cada quote en un csv dentro de una carpeta con el nombre del personaje (Lisa y Homer) y en un fichero que llamaremos general (Todos)._

_3. Generar un fichero Docker que copie el código dentro del contenedor y se ejecute de manera autónoma. El Docker debe tener el código en una carpeta app_

_4. El fichero docker debe crear al menos las carpetas Lisa y Homer e inicialmente solo coger citas de ellos dos._


Tenemos 3 directorios: 
 - General
 - Homer
 - Lisa

 en los cuales se guardan los correspondientes archivos .csv con las frases de Lisa, Homer y en el archivo general las frases de todos los personajes.
 En la raiz aparecen los ficheros:
  - Dockerfile
  - main.py
  - requirements.txt

***
## Ejercicio 2 (LISA LEVEL)
***
### Pasos (Lisa Level)
_1. Mejorad el código para descargar la imagen del personaje y guardadla en la carpeta del mismo_

_2. El código debe mantener un diccionario de palabras y escribir en cada iteración en un fichero el conteo de palabras que lleva_

_a. The;1_

_b. Great;2_

_3. El código debe crear de manera dinámica las carpetas con nuevos personajes_

  En este ejercicio aparecen los directorios de todos los personajes de la API de los Simpsons en cada uno de los cuales se incluye un archivo con la imagen del personaje en formato .png y un archivo .csv con las frases de dicho personaje.
  En la raiz aparecen los ficheros:
  - Dockerfile 
  - main.py
  - requirements.txt
  - ConteoPalabras.csv

  siendo en este ultimo el archivo donde se guardan el conteo de palabras que se genera en cada iteracion.


