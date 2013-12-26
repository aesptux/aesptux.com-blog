Montar una partición al inicio del sistema en Linux.
####################################################
:date: 2010-03-09 13:15
:author: aesptux
:category: Linux
:tags: inicio, Linux, montar, particiones
:slug: montar-una-particion-al-inicio-del-sistema-en-linux

A veces nos interesa montar una partición al inicio del sistema, ya sea
porque contiene archivos multimedia, o porque realizamos backups. Lo
primero que tenemos que hacer es crear la carpeta donde se montará:

    sudo mkdir /media/carpeta

Una vez tenemos la carpeta creada, tenemos que saber que partición
queremos montar:

    sudo fdisk -l

Con fdisk -l  nos mostrará todas las particiones, montadas o no. Cuando
ya tengamos identificada la partición, tenemos que editar el archivo
/etc/fstab (filesystem tab):

    sudo vi /etc/fstab

El formato estándar  es: <sistema de archivos> <punto de montaje> <tipo>
<opciones> Por ejemplo para una partición NTFS escribiremos algo así:

    /dev/sda2 /media/Multimedia ntfs-3g defaults,nls=utf8 0 0

Guardamos y listo! Ahora para comprobar que funciona correctamente:

    sudo mount -a
