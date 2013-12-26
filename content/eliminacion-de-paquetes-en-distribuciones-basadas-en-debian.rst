Eliminación de paquetes en distribuciones basadas en Debian.
############################################################
:date: 2010-01-18 13:00
:author: aesptux
:category: Linux
:tags: debian, eliminacion, paquetes
:slug: eliminacion-de-paquetes-en-distribuciones-basadas-en-debian

Para eliminar:

    apt-get remove paquete

Para probar el comando antes de ejecutarlo:

    apt-get remove paquete --dry-run

Para eliminar todo el rastro del paquete, incluyendo archivos de
configuración:

    apt-get remove --purge paquete

Para eliminar varios paquetes, proporcione una lista separada por
espacios:

    apt-get remove paquete1 paquete2 paquete3
