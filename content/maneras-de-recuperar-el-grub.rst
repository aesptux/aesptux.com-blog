Maneras de recuperar el grub
############################
:date: 2009-04-14 21:06
:author: aesptux
:category: Linux
:tags: boot, Linux, recuperar
:slug: maneras-de-recuperar-el-grub

La primera manera es con "Super Grub Disk" que es un restaurador del
grub muy sencillo, que incluye un manual.
 Pueden descargarlo desde `aquí`_

Otra manera es con una distribución livecd.

Una vez iniciado el livecd, abrimos una consola o terminal. Lo primero
que debemos hacer es montar la partición, para ello:
 sudo mount /dev/sda# /media/carpetaX
 Donde # equivale al número de la partición y la carpetaX a la carpeta
donde queremos montarlo, que debe existir antes de ejecutar este
comando, ejemplo:
 sudo mkdir /media/ubuntu
 mount /dev/sda5 /media/ubuntu

Una vez montada la partición, se pueden hacer dos cosas:
 1)
 sudo grub //Para iniciar el intérprete del grub
 root (hdX,Y) // Marcamos donde está la partición de ubuntu. X
corresponde al numero del disco. Y corresponde al numero de partición
 setup (hdX) // Instalamos el grub
 quit // salimos del intérprete

2)
 sudo grub
 find /boot/grub/stage1 // encuentra donde está instalado el grub
 root(hdX,Y)
 setup(hdX)
 quit

Bien, a mi las dos maneras anteriores no me han funcionado, hay a gente
que sí. Yo solucioné mi problema con lo siguiente:

sudo su
 mkdir /media/ubuntu
 mount /dev/sda5 /media/ubuntu
 mount --bind /dev /media/ubuntu/dev
 mount --bind /proc /media/ubuntu/proc
 mount --bind /sys /media/ubuntu/sys
 chroot /media/ubuntu/
 grub-install /dev/sda

Es un poquito más largo, pero a mi me funcionó. ;)

Un saludo,

Mortuus.

.. _aquí: http://forjamari.linex.org/frs/download.php/605/sgd_0.9598.iso.bz2
