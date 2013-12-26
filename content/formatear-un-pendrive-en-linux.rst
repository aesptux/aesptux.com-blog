Formatear un pendrive en Linux.
###############################
:date: 2009-06-05 15:00
:author: aesptux
:category: Linux
:tags: como, formatear, pendrive
:slug: formatear-un-pendrive-en-linux

Primero, hay que saber cual es nuestro pendrive para ello hacemos:

*mount*

y veremos algo así:

*/dev/sda1 on / type ext4 (rw,relatime,errors=remount-ro)*

*/dev/sdc1 on /media/MORTUUS type vfat
(rw,nosuid,nodev,uhelper=hal,shortname=mixed,uid=1000,utf8,umask=077,flush)*

En mi caso, mi pendrive es */dev/sdc1*. Ahora procederemos a desmontarlo
y formatearlo:

*umount /dev/sdc1*

*sudo mkfs -t vfat /dev/sdc1*

Y eso es todo, con eso tendremos nuestro pendrive formateado.
