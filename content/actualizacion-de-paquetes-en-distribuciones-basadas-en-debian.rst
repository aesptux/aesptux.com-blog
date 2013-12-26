Actualización de paquetes en distribuciones basadas en Debian
#############################################################
:date: 2010-01-19 13:26
:author: aesptux
:category: Linux
:tags: actualizar, debian, distribuciones, Linux, paquetes
:slug: actualizacion-de-paquetes-en-distribuciones-basadas-en-debian

Lo más esencial, actualizar la lista de paquetes:

    apt-get update

Actualizar todos los paquetes instalados, pero sin eliminar paquetes
para resolver dependencias:

    apt-get -u upgrade

Actualizar todos los paquetes que hay instalados, eliminando o bien
instalando paquetes nuevos según se necesite para satisfacer todas las
dependencias:

    apt-get -u dist-upgrade

El parámetro -u le da una oportunidad de revisar todos los cambios antes
de que se produzcan.
