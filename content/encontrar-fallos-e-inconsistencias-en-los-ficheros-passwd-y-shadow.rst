Encontrar fallos e inconsistencias en los ficheros passwd y shadow
##################################################################
:date: 2011-07-15 12:21
:author: aesptux
:category: Linux
:tags: /etc/passwd, /etc/shadow, archivos, comando, comprobar, error, Linux, passwd, pwck, shadow, valido, warning
:slug: encontrar-fallos-e-inconsistencias-en-los-ficheros-passwd-y-shadow

Con el comando **pwck**\ podremos verificar que la información existente
en **/etc/passwd**\ y en **/etc/shadow** es **correcta.** Para poder
ejecutarlo debemos ser root.

Este comando verifica la integridad de los usuarios y la información de
autenticación. Comprueba que todas las entradas en /etc/passwd y
/etc/shadow tengan el formato apropiado y los datos sean válidos. Se
preguntará al usuario si desea borrar las entradas que tienen un formato
incorrecto o las que tengan errores incorregibles.

Comprueba que cada entrada tenga:

.. raw:: html

   <ul style="text-align: justify;">

-  El número correcto de campos
-  Un nombre de usuario válido y único
-  Identificador de grupo único y válido
-  Un grupo primario único
-  Un directorio home válido
-  Una shell válida

.. raw:: html

   </ul>

Con respecto a /etc/shadow las comprobaciones son las siguientes:

.. raw:: html

   <ul style="text-align: justify;">

-  Cada entrada en /etc/passwd tiene su correspondiente en /etc/shadow,
   y viceversa
-  Las contraseñas están especificadas en el archivo
-  Tienen el número correcto de campos
-  Son únicas

.. raw:: html

   </ul>

.. raw:: html

   <div style="text-align: justify;">

Tiene los siguientes parámetros:

.. raw:: html

   </div>

.. raw:: html

   <ul style="text-align: justify;">

-  **-q:** Reportar sólo errores. No se mostrarán los warning.
-  **-s:**\ Ordenar por UID.

.. raw:: html

   </ul>

Nos dirigimos a la terminal y ejecutamos el comando:

    # pwck

La salida en mi caso es esta:

::

    user 'lp': directory '/var/spool/lpd' does not exist
    user 'news': directory '/var/spool/news' does not exist
    user 'uucp': directory '/var/spool/uucp' does not exist
    user 'list': directory '/var/list' does not exist
    user 'irc': directory '/var/run/ircd' does not exist
    user 'gnats': directory '/var/lib/gnats' does not exist
    user 'nobody': directory '/nonexistent' does not exist
    user 'syslog': directory '/home/syslog' does not exist
    user 'usbmux': directory '/home/usbmux' does not exist
    user 'speech-dispatcher': directory '/var/run/speech-dispatcher' does not exist
    user 'pulse': directory '/var/run/pulse' does not exist
    user 'hplip': directory '/var/run/hplip' does not exist
    user 'saned': directory '/home/saned' does not exist
    user 'haldaemon': directory '/var/run/hald' does not exist
    user 'mysql': directory '/nonexistent' does not exist
    pwck: no changes

Via \| `rm-rf.es`_

.. _rm-rf.es: http://rm-rf.es/como-encontrar-fallos-e-inconsistencias-en-los-ficheros-passwd-y-shadow/
