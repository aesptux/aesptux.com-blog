Habilitar USB's en Virtualbox para Windows en Debian
####################################################
:date: 2010-09-10 13:15
:author: aesptux
:category: Linux, Tutorial, Windows
:tags: debian, habilitar, usb, virtualbox, Windows
:slug: habilitar-usbs-en-virtualbox-debian

Antes de empezar, asegúrate de que tienes la máquina virtual Windows
correctamente instalada con los Guest Additions instalados también

Primero, hay que añadir nuestro usuario actual (no root) al grupo
vboxusers

    # adduser usuario vboxusers

Si no sabes cuál es tu usuario puedes hacer:

    $ whoami

En el siguiente paso, tenemos que cambiar el grupo el cual tiene
permisos para montar USB's, que por defecto es root.

Nos vamos al siguiente archivo:

    # vim /etc/udev/rules.d/10-vboxdrv.rules

Buscamos la siguiente línea:

    KERNEL=="vboxdrv", NAME="vboxdrv", OWNER="root", GROUP="**root**\ ",
    MODE="0600"

Y ahora hay que cambiar el atributo de GROUP a vboxusers, quedando así:

    KERNEL=="vboxdrv", NAME="vboxdrv", OWNER="root",
    GROUP="**vboxusers**\ ", MODE="0600"

Ya entramos en la recta final de la configuración, el siguiente paso es
en Virtualbox hacer  click en Settings y en USB, activar los que sea
necesario y ya está!

Al encender nuestra máquina virtual, tendremos en funcionamiento los
USB's.

Vía \| `Wiki esdebian`_

.. _Wiki esdebian: http://www.esdebian.org/wiki/habilitar-puertos-usb-virtualbox-3010-windows-debian
