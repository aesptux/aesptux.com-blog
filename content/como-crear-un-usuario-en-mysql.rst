Cómo crear un usuario en MySQL.
###############################
:date: 2011-07-20 10:59
:author: aesptux
:category: Databases, MySQL
:tags: all, como, crear, en, grant, Linux, mysql, nuevos, privileges, usuarios, Windows
:slug: como-crear-un-usuario-en-mysql

Cuando trabajamos con bases de datos para algún cliente, o incluso
trabajando desde PHP, necesitamos crear un usuario para la base de datos
que vayamos a utilizar.

Primero tenemos que loguearnos como root:

    $ mysql -u root -p

Creamos una base de datos nueva (si no la tenemos ya)

    mysql> CREATE DATABASE prueba;

Ahora creamos el usuario, y le asignamos todos los permisos sólo a la
base de datos que hemos creado, no podrá acceder a ninguna otra

    mysql> GRANT ALL ON prueba.\* TO usuarioprueba@localhost IDENTIFIED
    BY 'supassword';

Con eso indicamos que el usuario 'usuarioprueba' podrá acceder con la
contraseña 'supassword' únicamente a la base de datos llamada prueba.

.. raw:: html

   <div class="mceTemp mceIEcenter" style="text-align: justify;">

`|image0|`_
    Creación de un usuario en MySQL. Click para aumentar

.. raw:: html

   </div>

.. _|image1|: http://aesptux.com/wp-content/uploads/2011/07/Selection_009.png

.. |image0| image:: http://aesptux.com/wp-content/uploads/2011/07/Selection_009-300x255.png
.. |image1| image:: http://aesptux.com/wp-content/uploads/2011/07/Selection_009-300x255.png
