Redirecciones en Linux
######################
:date: 2010-05-10 13:00
:author: aesptux
:category: Linux
:tags: ficheros, Linux, redirecciones, stderr, stdin, stdout
:slug: redirecciones-en-linux

En Linux se utilizan muchísimo las redirecciones.

Siguiendo la filosofía de Unix “todo es un archivo”, cualquier programa
puede generar una salida, que puede ser redireccionada a un archivo
(Standard output, o stdout) en vez de sacarlo por pantalla.

Los mensajes de estado se envían a través de la Standard error (stderr).

Por defecto, ambos están enlazados a la pantalla y no a un archivo.

Para hacer una redirección de la salida de un comando es muy sencillo:

    ls /etc > salida-etc

El operador ‘>’ crea un archivo nuevo con la salida del comando
indicado, en el caso de que ya exista, se sobrescribe.

Si queremos unir varias salidas, tenemos que utilizar el operador ‘>>’
que provocará que se vaya añadiendo al final del archivo, y si no
existe, lo creará.

Con las redirecciones, existe un pequeño truco para truncar archivos
existentes o crear archivos vacios:

    >salida.txt

Con esa orden estamos redireccionando nada a el archivo salida.txt.

Si intentamos redireccionar algo que no existe, nos mostrará el error en
pantalla y no en el archivo. Esto es debido a que los errores, habría
que redireccionarlos por la Standard error.

Para redireccionar errores, no hay ningún operador específico, así que
deberemos utilizar el descriptor.

-  0 – stdin
-  1- stdout
-  2 –stderr

Para redireccionar errores utilizaremos el descriptor 2, por ejemplo:

    tar –xzvf archivo.tar.gz 2>> extrac.log

Si queremos redireccionar la stdout y stderr al mismo archivo, deberemos
hacerlo de la siguiente manera

    ……… 2>&1 > salida.txt

En las últimas versiones de bash se incluyó el siguiente método:

    ……. &> salida.txt

En otras ocasiones, no nos interesa conservar ninguna salida, ni por
pantalla ni por fichero, entonces deberemos redireccionarlo a
‘/dev/null’

    ……………… 2>&1> /dev/null
