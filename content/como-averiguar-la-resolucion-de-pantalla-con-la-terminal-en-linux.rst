Cómo averiguar la resolución de pantalla con la terminal en Linux.
##################################################################
:date: 2011-07-21 11:36
:author: aesptux
:category: Linux
:tags: averiguar, con, consola, encontrar, Linux, monitor, pantalla, resolucion, saber . como, terminal
:slug: como-averiguar-la-resolucion-de-pantalla-con-la-terminal-en-linux

Podemos utilizar dos comandos:

    $ xdpyinfo \| grep 'dimensions'

O bien este otro:

    $ xrandr \| grep '\*'

`|image0|`_

.. _|image1|: http://aesptux.com/wp-content/uploads/2011/07/Selection_010.png

.. |image0| image:: http://aesptux.com/wp-content/uploads/2011/07/Selection_010.png
.. |image1| image:: http://aesptux.com/wp-content/uploads/2011/07/Selection_010.png
