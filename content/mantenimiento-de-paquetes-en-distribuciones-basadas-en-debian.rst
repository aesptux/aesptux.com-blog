Mantenimiento de paquetes en distribuciones basadas en Debian.
##############################################################
:date: 2010-01-26 12:46
:author: aesptux
:category: Linux
:tags: debian, distribuciones, Linux, mantenimiento, paquetes
:slug: mantenimiento-de-paquetes-en-distribuciones-basadas-en-debian

Buscar paquetes descargados sin instalar:

    dpkg --yet-to-unpack

Comprobar dependencias rotas:

    apt-get check

Eliminar paquetes de la caché:

    apt-cache clean

Ver qué paquetes hay instalados parcialmente:

    dpkg --audit
