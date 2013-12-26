Instalación de paquetes en distribuciones basadas en Debian.
############################################################
:date: 2010-01-14 12:43
:author: aesptux
:category: Linux
:tags: debian, instalacion, paquetes
:slug: instalacion-de-paquetes-en-distribuciones-basadas-en-debian

Para instalar un paquete:

    apt-get install paquete

Para reinstalar un paquete, sobreescribiendo los archivos, haga esto:

    apt-get install --reinstall paquete

También puede instalar varios paquetes a la vez, separados por un
espacio:

    apt-get install paquete1 paquete2 paquete3 paquete4

Para descargar sin instalar o desempaquetar:

    apt-get -d install paquete

Para probar el comando antes de ejecutarlo:

    apt-get install paquete1 paquete2 --dry-run

Para instalar desde fuentes:

-  Lo primero descargar las dependencias del paquete

    apt-get build-dep paquete

-  A continuación se construye el paquete:

    apt-get -b source paquete

-  Y ahora se instala:

    dpkg -i paquete.deb
