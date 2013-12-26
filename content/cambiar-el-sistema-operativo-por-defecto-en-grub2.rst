Cambiar el sistema operativo por defecto en GRUB2
#################################################
:date: 2011-07-19 12:54
:author: aesptux
:category: Linux
:tags: cambiar, como, default, defecto, diferente, grub, grub2, Linux, orden, sistema
:slug: cambiar-el-sistema-operativo-por-defecto-en-grub2

Por defecto arranca siempre el sistema operativo numero 0, es decir el
primero.

Si queremos cambiar esto, tenemos que editar el fichero
**/etc/default/grub.**\ En este archivo encontraremos una línea que
pondrá:

    GRUB\_DEFAULT=0

Pues simplemente cambiamos ese número por la entrada que queramos,
teniendo en cuenta que el orden empieza en 0. Por ejemplo para poner que
arranque el tercer sistema, haríamos lo siguiente:

    $ sudo /etc/default/grub

    GRUB\_DEFAULT=2

Tras eso, hay que actualizar el grub, con el comando:

    $ sudo update-grub

Reiniciamos si queremos para ver los cambios.
