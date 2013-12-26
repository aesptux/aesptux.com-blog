Cómo montar imágenes .iso en Debian
###################################
:date: 2010-09-08 13:00
:author: aesptux
:category: Linux
:tags: .iso, debian, imágenes, Linux, montar, mount
:slug: como-montar-imagenes-iso-en-debian

Montar una imagen .iso en Debian, es muy sencillito, basta con un par de
líneas:

Primero creamos el directorio donde vamos a montar la imagen .iso:

    # mkdir /mnt/directorio

Y luego simplemente montar el archivo:

    # mount -t iso9660 -o loop archivo.iso /mnt/directorio

Donde -t indica el tipo y -o indica el pseudo dispositivo loop.


