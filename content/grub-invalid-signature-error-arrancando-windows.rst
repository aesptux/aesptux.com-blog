Grub: Invalid Signature. Error arrancando Windows
#################################################
:date: 2009-11-17 10:21
:author: aesptux
:category: Linux
:tags: arrancando, booting, error, grub, invalid, signature, Windows
:slug: grub-invalid-signature-error-arrancando-windows

Hoy he vuelto a instalar Windows en una pequeña partición. Como siempre
que tienes instalado Linux antes, Windows machaca el grub. Así que hice
el proceso de `recuperación del grub`_.

Pero a mi sorpresa el grub al arrancar Windows me daba un error que
nunca antes me había dado: **Invalid Signature.**

 Así que decidido, fui a editar */boot/grub/menu.lst* y tachán! No está.
No recordaba que Ubuntu 9.10 utiliza Grub2 y ese archivo ya no existe,
ahora en su lugar nos encontramos con */boot/grub/grub.cfg*. Lo que hace
"especial" a este archivo esque es exclusivamente de lectura, y bajo
ningún concepto se puede editar, ni siquiera desde un Live CD.

Yo tengo los SS.OO en el segundo disco duro (/dev/sdb), así que comprobé
el siguiente archivo: */boot/grub/device.map*

 Y aquí estaba el error en mi caso. El archivo apuntaba a /dev/sda, así
que lo edité por /dev/sdb y guardé los cambios y después actualicé el
grub:

*sudo os-prober*

*sudo update-grub*

*sudo reboot*

Con eso conseguí arreglarlo todo y ahora funciona perfectamente, de
momento ;).

.. _recuperación del grub: http://mortuux.wordpress.com/2009/04/14/maneras-de-recuperar-el-grub/
