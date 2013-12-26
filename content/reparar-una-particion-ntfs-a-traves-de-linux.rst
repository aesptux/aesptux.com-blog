Reparar una partición NTFS a través de Linux
############################################
:date: 2010-04-20 20:00
:author: aesptux
:category: Linux
:tags: con, Linux, ntfsfix, ntfsprogs, particion, reparar, Windows
:slug: reparar-una-particion-ntfs-a-traves-de-linux

Podemos reparar una partición NTFS dañada con la utilidad *ntfsfix*

Hay que aclarar que **no** tiene nada que ver con *chdsk*. Ntfsfix sólo
repara algunas inconsistencias y resetea el journal de NTFS.

Para utilizar ntfsfix, debemos instalar:

    sudo apt-get install ntfsprogs

Y ahora sólo debemos ejecutar la utilidad apuntando a la partición
adecuada:

    ntfsfix /dev/sd**XY**
