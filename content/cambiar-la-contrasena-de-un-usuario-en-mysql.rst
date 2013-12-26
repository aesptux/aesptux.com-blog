Cambiar la contraseña de un usuario en MySQL.
#############################################
:date: 2011-07-25 17:16
:author: aesptux
:category: Databases, MySQL
:tags: bases, cambiar, contraseña, datos, flush, mysql, otros, root, usuario
:slug: cambiar-la-contrasena-de-un-usuario-en-mysql

Para cambiar la contraseña de root, podemos hacer:

    # mysqladmin -u root -p'contraseñaantigua' password
    'nuevacontraseña'

También podemos cambiar con una sentencia SQL:

    $ mysql -u root -p

    mysql> use mysql;

    mysql>UPDATE user SET password=PASSWORD("nuevacontraseña" ) WHERE
    user='adrian';

    flush privileges;

Utilizamos la base de datos mysql, y actualizamos el usuario que
queramos. Después el comando flush privileges sirve para recargar los
privilegios.
