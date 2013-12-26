Un poco más sobre redirecciones y pipes.
########################################
:date: 2011-07-09 12:37
:author: aesptux
:category: Linux, Unix
:tags: and, apache, canal, comandos, comunicacion, find, Linux, lógicos, mail, operador, operadores, or, pipes, ps, redirecciones, stderr, stdin, stdout, tuberías, unix
:slug: un-poco-mas-sobre-redirecciones-y-pipes

Cada proceso tiene al menos tres canales de comunicación disponibles:

.. raw:: html

   <ul style="text-align: justify;">

-  Standard input (STDIN)
-  Standard output (STDOUT)
-  Standard error (STDERR)

.. raw:: html

   </ul>

.. raw:: html

   <div style="text-align: justify;">

El kernel establece estos canales en nombre del proceso. Como ya comenté
en una `entrada anterior`_ tenemos varios descriptores que identificar a
cada canal de comunicación:

.. raw:: html

   </div>

.. raw:: html

   <ul style="text-align: justify;">

-  STDIN: 0
-  STDOUT: 1
-  STDERR: 2

.. raw:: html

   </ul>

.. raw:: html

   <div style="text-align: justify;">

La shell interpreta\ **'<'**, **'>'** y **'>>'** como instrucciones para
redirigir la entrada o salida de un comando a o desde un archivo.

.. raw:: html

   </div>

.. raw:: html

   <ul style="text-align: justify;">

-  '<' redirecciona STDIN
-  '>' redirecciona STDOUT (Reemplazando el contenido existente)
-  '>>' redirecciona STDOUT (Añade al final del contenido existente)

.. raw:: html

   </ul>

    .. raw:: html

       <div>

    $ echo "Mensaje de prueba" > /tmp/mensaje

    .. raw:: html

       </div>

Este comando almacena el texto en el archivo indicado, creando el
archivo si no existiese. Ahora podemos utilizar ese archivo para enviar
un correo.

    $ mail -s "Probando" usuario < /tmp/mensaje

En el comando anterior, indicamos que la entrada de datos sea el
archivo.

Para redireccionar STDOUT y STDERR al mismo sitio, utilizamos **'&>'**.
Para redireccionar sólo STDERR, utilizaremos su descriptor, es decir
**'2>'**

Para probar cómodamente éstas salidas, podemos utilizar el comando
\ **find**, ya que produce salidas en varios canales. Si ejecutamos:

    $ find / -name core

Nos devolverá varios "Permission denied" por falta de permisos. Para
 descartar estos errores, haríamos lo siguiente:

    $ find / -name core 2> /dev/null

Ahora, sólo nos mostrará la STDOUT, es decir, los resultados favorables.

También podemos redireccionar la STDOUT a un archivo para que sea más
cómodo revisarlo.

    $ find / -name core > /tmp/archivoscore 2> /dev/null

En el ejemplo anterior, redireccionamos STDOUT a un archivo para su
posterior revisión, y seguimos descartando los errores enviándolos a
/dev/null.

Para conectar la STDOUT de un comando con la STDIN de otro, utilizamos
el símbolo **'\|'**\ conocido como "Pipe".

    $ ps -ef \| grep apache

El comando **ps**\ nos muestra una lista de todos los procesos activos,
y redirecciona su salida al comando **grep**\ que lo que hace es
seleccionar las líneas que contengan la palabra apache.

Para ejecutar dos comandos ordenadamente en la misma línea, utilizamos
el operador **'&&'.** El segundo comando se ejecutará **sólo** si la
STDOUT del primero ha sido satisfactoria.

    $ mail -s "Mail importante" jefe < /tmp/contenido && echo "Correo
    enviado"

Sin embargo, si nos interesa que el segundo comando se ejecute sólo si
el primero ha fallado (STDOUT != 0), utilizaremos el operador **'\|\|'**

    $ mail -s "Mail importante" jefe < /tmp/contenido \|\| echo
    "Atención: El correo NO se ha enviado"

.. _entrada anterior: http://aesptux.com/2010/05/10/redirecciones-en-linux/
