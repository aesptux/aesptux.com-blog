Automatizar la actualización de paquetes
########################################
:date: 2010-01-25 12:29
:author: aesptux
:category: Linux
:tags: actualizacion, automatizar, Linux, paquetes
:slug: automatizar-la-actualizacion-de-paquetes

Muy sencillo. Vamos a usar crontab y apt-get

Primero abrir el editor de crontab:

    crontab -e

Este ejemplo se ejecutará cada hora:

    0 \* \* \* \* root (apt-get update && apt-get -y upgrade) >
    /dev/null

La opción -y hace que responda a cualquier pregunta con *yes*

También podemos hacer que se descargue los paquetes, pero que no los
instale, por si no nos interesa, pero en el caso de querer actualizar,
nos ahorramos el tiempo de descarga:

    0 \* \* \* \* root (apt-get update && apt-get -y -d upgrade)
