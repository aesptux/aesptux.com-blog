PHP Deprecated:  Comments starting with '#' are deprecated
##########################################################
:date: 2011-07-12 12:38
:author: aesptux
:category: Php
:tags: #, /etc/php5/cli/conf.d/ming.ini, are, arreglar, comments, configuration, deprecated, error, fixear, help. ayuda, in, line, ming, on, php, php5, solventar, starting, unknown, warning, with
:slug: php-deprecated-comments-starting-with-are-deprecated

Si estáis tratando de ejecutar algún script php desde la terminal de
linux o crontab, y os sale algún error como este:

::

    PHP Deprecated:  Comments starting with '#' are deprecated in /etc/php5/cli/conf.d/ming.ini on line 1 in Unknown on line 0

Debemos ir al archivo o archivos (en algunos foros los usuarios
comentaban que podían ser varios) y hacer los siguientes cambios:

Contenido de ming.ini inicial:

::

    # configuration for php MING module
    extension=ming.so

Como vemos, el comentario se hace con "#", lo que ya está en desuso,
pues la solución es tan simple como cambiar '#' por '//' que es como se
hacen los comentarios en php.

::

    //configuration for php MING module
    extension=ming.so

Una vez hecho esto, debería funcionar correctamente.
