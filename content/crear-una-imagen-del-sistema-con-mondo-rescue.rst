Crear una imagen del sistema con Mondo Rescue.
##############################################
:date: 2010-01-20 13:46
:author: aesptux
:category: Linux
:tags: crear, imagen, mondo rescue, sistema
:slug: crear-una-imagen-del-sistema-con-mondo-rescue

Mondo Rescue es una rápida y sencilla herramienta para crear imágenes de
nuestro sistema. Para instalarlo:

    sudo apt-get install mondo

**Nota:**\ *Mondo tiene sus propias ideas sobre el GRUB xD así que
necesitaremos el siguiente enlace para que mondo funcione:*

    *ln -s /boot/grub/menu.lst /etc/grub.conf* *Con grub2: ln -s
    /boot/grub/grub.cfg /etc/grub.conf*

 Una vez lo tengamos instalado, nos logueamos como root y lo ejecutamos
escribiendo en la terminal:

    mondoarchive

`|Ejecutando Mondo Rescue|`_

En el menú principal de Mondo Rescue, podremos elegir en que medio
queremos archivar la imagen. En mi caso elegiré en el disco duro

`|Menú|`_

Ahora nos pide indicar el lugar donde se almacenará la iso, por defecto
en */var/cache/mondo.*

A continuación nos pide indicar el nivel de compresión, yo voy a elegir
compresión máxima.

Bien, ahora nos pide que introduzcamos el tamaño en **MB**\ de la(s)
imágenes iso. Si creemos que en un futuro podremos grabarla en algún cd,
será mejor que indiquemos un tamaño adecuado para un CD, como por
ejemplo 650 mb.

Ahora nos pide el nombre de la(s) imagen(es). Como indica, el formato
será el siguiente: nombre1.iso, nombre2.iso... Es decir, que si la
imagen, supera el tamaño máximo que hemos establecido, creará otras.

Lo siguiente es indicar que queremos copiar. Si indicamos **'/'**
copiará todo. En este caso yo elegiré copiar /etc sólo.

Si queremos que nos copie alguna de nuestras particiones NTFS,
comprobaremos que estén correctamente indicadas, en caso contrario, lo
dejamos en blanco.

En este paso, podemos indicar que directorios **no**\ queremos copiar...
por ejemplo si es una copia de configuración del sistema, podemos
evitarnos copiar nuestro /home.

Confirmamos que sí compruebe la copia después.

Para recuperar nuestra copia, escribiremos, también como root lo
siguiente en la terminal:

    mondorestore

.. _|image2|: http://farm5.static.flickr.com/4059/4287893404_3740da747e_o.png
.. _|image3|: http://farm3.static.flickr.com/2771/4287901592_2c849fdc24_o.png

.. |Ejecutando Mondo
Rescue| image:: http://farm5.static.flickr.com/4059/4287893404_3740da747e_o.png
.. |Menú| image:: http://farm3.static.flickr.com/2771/4287901592_2c849fdc24_o.png
.. |image2| image:: http://farm5.static.flickr.com/4059/4287893404_3740da747e_o.png
.. |image3| image:: http://farm3.static.flickr.com/2771/4287901592_2c849fdc24_o.png
