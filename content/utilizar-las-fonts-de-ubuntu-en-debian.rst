Utilizar las fonts de Ubuntu en Debian.
#######################################
:date: 2010-10-26 12:30
:author: aesptux
:category: Linux
:tags: bonito, debian, desktop, escritorio, fonts, ubuntu, utilizar
:slug: utilizar-las-fonts-de-ubuntu-en-debian

Las fonts que utiliza Ubuntu son bastante bonitas en mi opinión,
instalarlas en Debian es bastante sencillo:

Nos descargamos las fonts de
aquí: \ `http://dl.dropbox.com/u/1301915/ubuntu-font-family.tar.gz`_

Ahora extraemos:

    tar -xvzf ubuntu-font-family.tar.gz -C /usr/share/fonts/truetype

Ahora tenemos que ir a Sistema -> Preferencias -> Apariencia.

Y en tipografía ponemos esta configuración:

`|image0|`_

No se ve, pero antes del paso siguiente, debemos tener marcada la opción
Suavizado subpixel (LCDs)

En el siguiente paso, hacemos click en detalles y ponemos la siguiente
configuración:

.. figure:: http://farm2.static.flickr.com/1183/5098147028_2399ff4967.jpg
   :align: center
   :alt: Detalles

Y eso es todo, ahora debería parecerse bastante al estilo de fonts que
tiene Ubuntu.

.. _`http://dl.dropbox.com/u/1301915/ubuntu-font-family.tar.gz`: http://dl.dropbox.com/u/1301915/ubuntu-font-family.tar.gz
.. _|image1|: http://farm2.static.flickr.com/1405/5098147026_057037da6b.jpg

.. |image0| image:: http://farm2.static.flickr.com/1405/5098147026_057037da6b.jpg
.. |image1| image:: http://farm2.static.flickr.com/1405/5098147026_057037da6b.jpg
