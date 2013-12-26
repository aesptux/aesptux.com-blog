Mover /home a su propia partición.
##################################
:date: 2011-07-18 11:15
:author: aesptux
:category: Linux
:tags: /etc/fstab, /home, blkid, boot, cambiar, comando, cpio, cualquier, Linux, mount, mover, particion, uuid
:slug: mover-home-a-su-propia-particion

Crear una partición para /home desde la instalación es bastante
sencillo, pero ¿Y si queremos hacerlo cuando ya tenemos instalado todo
el sistema en una sola partición?

El siguiente método sirve tanto para /home como para cualquier otra
partición que queramos hacer (con sus respectivos cambios, por
supuesto). Es algo más largo de hacer, pero sigue siendo muy sencillo:

Parto de la base de que ya tenéis vuestra partición en ext4 con el
tamaño que queráis. (Si no, éste paso podéis realizarlo con GParted)

Lo primero que tenemos que hacer es montar la partición nueva:

    $ sudo /mnt/home

    $ sudo mount -t ext4 /dev/sdXY/ /mnt/home

(Sustituimos XY por nuestros datos, por ejemplo /dev/sda6)

A continuación copiaremos los archivos, pero no con un simple **cp:**

    $ cd /home

    $ find . -depth -print0 \| cpio --null --sparse --pvd /mnt/home

Una vez haya terminado, **revisamos que todo esté correctamente
copiado** y acto seguido, podemos desmontar la partición nueva:

    $ sudo umount /dev/sdXY

Cambiamos el nombre de /home a otro:

    $ sudo mv /home /home\_orig

Como no existe, /home, tenemos que volver a crear la carpeta, y montamos
la nueva partición:

    $ sudo mkdir /home

    $ sudo mount /dev/sdXY /home

Y ya está hecho, ahora queda, indicar que se monte automáticamente en
cada inicio del sistema, para ello tenemos que editar el archivo
**/etc/fstab**, pero antes debemos saber cual es **UUID** de nuestro
disco, para ello escribimos lo siguiente:

    $ sudo blkid

Y buscar cual es nuestro UUID, después editamos el fichero:

    $ sudo /etc/fstab

Copiamos la siguiente línea:

    UUID=uuid-de-nuestro-disco /home ext4 defaults,user\_xattr 0 2

Una vez hecho todo esto, estará todo listo. Podemos reiniciar y
comprobar que efectivamente, todo está correcto.
