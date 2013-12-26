Dividir un archivo de texto grande en varios pequeños
#####################################################
:date: 2010-01-22 14:06
:author: aesptux
:category: Linux
:tags: archivo, dividir, grande, Linux
:slug: dividir-un-archivo-de-texto-grande-en-varios-pequenos

Cuando trabajamos con archivos de texto muy grandes, se dispara el
consumo de memoria, lo que puede llegar a mermar nuestra productividad.

Para dividir un archivo en varios, existe una orden en linux y es
*split*

    split [parametros opcionales] [archivo entrada] [archivos de salida]

Parámetros más importantes:

-  -l: Numero de líneas en las que se va a dividir el archivo. Por
   defecto son 1000
-  -b: Divide por tamaño expresado en bits

El archivo de salida siempre quedará identificado de la siguiente forma:

Si nosotros especificamos que el nombre del archivo de salida sea
"hola-", las diferentes partes quedarán como: hola-a, hola-b, hola-c,
etc

Ejemplo:

    split -l 2500 archivo archivo\_part-
