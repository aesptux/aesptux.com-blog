Cambiar la shell por defecto
############################
:date: 2010-04-20 13:00
:author: aesptux
:category: Linux
:tags: bash, cambiar, defecto, Linux, shell
:slug: cambiar-la-shell-por-defecto

El comando *chsh*, permite cambiar la shell que tenemos por defecto.

Es práctico, si nuestro administrador nos ha asignado una shell con la
que no estamos cómodos, o simplemente, que queremos probar otras shells.

La sintaxis básica del comando es

    Chsh usuario nueva\_shell

El parámetro de la shell, debe ser la ruta completa a la shell, como por
ejemplo */bin/bash*

Si no sabes que shell tienes, puedes escribir:

    Echo $SHELL
