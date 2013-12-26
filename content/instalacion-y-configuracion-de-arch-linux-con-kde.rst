Instalación y configuración de Arch Linux con KDE.
##################################################
:date: 2010-01-15 13:43
:author: aesptux
:category: Linux
:tags: alsa, arch linux, configuracion, instalacion, kde, Tutorial, xorg
:slug: instalacion-y-configuracion-de-arch-linux-con-kde

Arch Linux es una distribución simple (que no fácil de instalar ni
configurar) y que da total libertad al usuario para configurarlo a sus
necesidades. También predomina la precisión de código ante la comodidad.
Una vez tengamos el archivo iso con la arquitectura que queramos, en mi
caso la i686, procederemos a instalarlo. Como bien nos indica, debemos
loguearnos como root para iniciar la instalación `|image0|`_ Para
configurar el teclado y elegir tipo de fuente, escribimos:

    km

`|image1|`_ Para iniciar la instalación:

    /arch/setup

Este es el menú principal de la instalación: `|image2|`_\ El primer paso
es bien sencillo, debemos elegir en **Select Sources -> CD**. Para
utilizar el CD como repositorio en la instalación. En **Set Clock**
elegimos nuestra zona horaria adecuada `|image3|`_ El tercer paso es
preparar el disco duro. Yo voy a hacer una instalación limpia, sin
ningún otro sistema operativo, así que lo más fácil es elegir
Auto-Prepare. **Pero mucho ojo, no seleccionar ésta opción si se tienen
otros sistemas operativos, ya que formatea todo** `|image4|`_ La opción
Auto-Prepare nos da a elegir el tamaño para una partición de /boot,
swap, / y /home `|image5|`_ En el siguiente paso, debemos elegir los
paquetes a instalar. Si no queremos complicarnos demasiado, o si estamos
seguros de que no vamos a necesitar más paquetes, bastará con los que
vienen ya seleccionados. `|image6|`_ Una vez seleccionados, procedemos a
instalarlos. `|image7|`_ Una vez esté todo instalado `|image8|`_ Ahora
nos toca la parte más "crítica": La configuración del sistema Entramos
en la opción de configuración del sistema y elegimos nuestro editor
favorito, en mi caso voy a usar *vi* *`|image9|`_* Menú de
configuración: `|image10|`_ Editamos primeramente **/etc/rc.conf**

-  Debemos cambiar *LOCALE="en\_US.utf8"* por lo siguiente:
   *LOCALE="es\_ES.utf8".*
-  Cambiar *HOSTNAME="myhost"* por el nombre que queramos poner a
   nuestra máquina
-  También tendremos que configurar la red en caso de que sea necesario,
   en mi caso solo cambiaré el gateway, usaré dhcp con la interfaz eth0

**/etc/fstab** Aquí sólo debemos miar que esté todo bien configurado por
el instalador. **/etc/resolv.conf** Aquí escribimos las ips de los dns
Los archivos de configuración **/etc/pacman.conf**\ y
**/etc/pacman.d/mirrorlist** los configuraremos más adelante. Ahora
debemos establecer nuestra contraseña de root. Una vez configurado todo,
sólo nos queda instalar el Bootloader. Lo instalamos en la partición
adecuada. `|image11|`_ ¡Ya tenemos Arch Linux instalado! Ahora queda
reiniciar. `|image12|`_ Como vemos, no tenemos ningún entorno gráfico.
Nos logueamos como root, que es la única cuenta que tenemos activa.
Ahora vamos a añadir algunos repositorios bastante conocidos. Editamos
**/etc/pacman.conf** Repositorio Archlinuxfr, agregamos el de nuestra
arquitectura correspondiente:

::

    [archlinuxfr]
    Server = http://repo.archlinux.fr/i686

    [archlinuxfr]
    Server = http://repo.archlinux.fr/x86_64

KDE Mod, agregar el de nuestra arquitectura:

::

    [kdemod-core]
    Server = http://chakra-project.org/repo/core/i686/
    [kdemod-core]
    Server = http://chakra-project.org/repo/core/x86_64/
    [kdemod-extragear]
    Server = http://chakra-project.org/repo/extragear/i686/
    [kdemod-extragear]
    Server = http://chakra-project.org/repo/extragear/x86_64/

`|image13|`_ Ahora debemos establecer los mirrors. En el archivo
**/etc/pacman.d/mirrors**\ hay un montón de mirrors y nos llevaría mucho
tiempo saber cuáles son los más recomendados para nuestro Arch, por
suerte hay un script llamado rankmirrors que nos elige los mejores
mirrors. Para utilizar rankmirrors debemos instalar python, por lo que
si no  lo tenemos instalado, tenemos que activar al menos un mirror para
poder poder descargarlo. Muy sencillo, del archivo anteriormente
nombrado, descomentamos (quitar #) un mirror de Francia por ejemplo,
después:

    pacman -Syu pacman -S python

**Volvemos a comentar el mirror anterior.** Nos movemos a la carpeta
**/etc/pacman.d/**

    cd /etc/pacman.d/ cp mirrorlist mirrorlist.bak

Y hacemos una copia del archivo. Ahora ejecutamos:

    rankmirrors -n 5 mirrorlist.bak > mirrorlist

Donde -n 5 indica el número de mirrors. Ahora procedemos a instalar
yaourt

    pacman -S yaourt

Bien, como trabajar como root es un tanto... peligroso, vamos a crear un
nuevo usuario:

    adduser

Después hay que añadirlo a ciertos grupos :

    gpasswd -a ***usuario*** audio gpasswd -a ***usuario*** wheel
    gpasswd -a ***usuario*** storage gpasswd -a ***usuario*** video
    gpasswd -a ***usuario*** optical gpasswd -a ***usuario*** floppy
    gpasswd -a ***usuario*** lp

Ahora instalamos y configuramos SUDO

    pacman -S sudo

Para configurar, ejecutamos:

    visudo

Y añadimos:

    usuario ALL = (ALL) ALL

Y guardamos. Ahora procedemos a instalar ALSA, para el sonido:

    pacman -S alsa-utils alsa-oss

Para configurarlo ejecutamos:

    alsaconf

Y seguimos los pasos. Es turno de instalar el servidor gráfico XORG.

    pacman -S xorg

(Nota: Si da conflicto con el paquete e2fsprogs, instalar éste primero
mediante pacman -S e2fsprogs) Ahora instalamos kde:

    pacman -S kde

`|image14|`_ Instalar idioma español:

    pacman -S kde-l10n-es

`|image15|`_ Ahora editamos el archivo **/etc/inittab/**\ para cambiar
los niveles de ejecución. Por defecto el sistema entra en el nivel de
ejecución (runlevel) 3, que es el de monousuario. Debemos comentar esta
línea, y descomentar la línea de nivel 5 que es el nivel que utiliza
X11. Con el cambio realizado quedaría así:

::

    #id:3:initdefault:
    # Boot to X11
    id:5:initdefault:

Más abajo debemos especificar que utilizaremos una pantalla de login
KDM, por lo tanto comentamos XDM y descomentamos la de KDM. Con el
cambio realizado quedaría así:

::

    #x:5:respawn:/usr/bin/xdm -nodaemon
    #x:5:respawn:/usr/sbin/gdm -nodaemon
    x:5:respawn:/usr/bin/kdm -nodaemon
    #x:5:respawn:/usr/bin/slim >& /dev/null

`|image16|`_ Importante: En el archivo **/etc/rc.conf**\ debemos añadir
el daemon ***hal.***

**Traducir completamente al español:**

Aparte de lo que modificamos en rc.conf, debemos hacer lo siguiente:

en **/etc/locale.gen**\ debemos descomentar las dos líneas es\_ES.

Después regenaramos los locales:

    locale-gen

Y lo comprobamos:

    locale -a

Para traducir KDE hace falta instalar los siguientes paquetes:

    ***``language-pack-eslanguage-pack-es-base language-pack-kde-es language-pack-kde-es-base language-support-es language-support-translations-es language-support-writing-es``
     ``kde-l10n-es``***

Y eso es todo! Ya tenemos nuestro Arch Linux instalado!

.. _|image17|: http://farm5.static.flickr.com/4068/4270788341_d27c2eaa27_o.png
.. _|image18|: http://farm5.static.flickr.com/4057/4270801259_6c44b88299_o.png
.. _|image19|: http://farm3.static.flickr.com/2727/4270801263_c488341ddf_o.png
.. _|image20|: http://farm5.static.flickr.com/4033/4270809413_07af24b775_o.png
.. _|image21|: http://farm5.static.flickr.com/4051/4270816007_0a91ac6a85_o.png
.. _|image22|: http://farm3.static.flickr.com/2730/4270822547_31e9a995d8_o.png
.. _|image23|: http://farm5.static.flickr.com/4044/4271580686_55dc751c59_o.png
.. _|image24|: http://farm3.static.flickr.com/2740/4271585496_4e3598febd_o.png
.. _|image25|: http://farm3.static.flickr.com/2710/4270853165_d8d898a792_o.png
.. _|image26|: http://farm3.static.flickr.com/2716/4271628352_a132facbbe_o.png
.. _|image27|: http://farm5.static.flickr.com/4063/4271628358_be1121dcfd_o.png
.. _|image28|: http://farm5.static.flickr.com/4031/4271751588_ca254c2792_o.png
.. _|image29|: http://farm5.static.flickr.com/4019/4271011881_882df169b3_o.png
.. _|image30|: http://farm5.static.flickr.com/4024/4271772990_332769f37b_o.png
.. _|image31|: http://farm3.static.flickr.com/2737/4271979493_c0f9f4aeee_o.png
.. _|image32|: http://farm3.static.flickr.com/2782/4271979499_9aff55080d_o.png
.. _|image33|: http://farm5.static.flickr.com/4027/4271979501_7c21f2726f_o.png

.. |image0| image:: http://farm5.static.flickr.com/4068/4270788341_d27c2eaa27_o.png
.. |image1| image:: http://farm5.static.flickr.com/4057/4270801259_6c44b88299_o.png
.. |image2| image:: http://farm3.static.flickr.com/2727/4270801263_c488341ddf_o.png
.. |image3| image:: http://farm5.static.flickr.com/4033/4270809413_07af24b775_o.png
.. |image4| image:: http://farm5.static.flickr.com/4051/4270816007_0a91ac6a85_o.png
.. |image5| image:: http://farm3.static.flickr.com/2730/4270822547_31e9a995d8_o.png
.. |image6| image:: http://farm5.static.flickr.com/4044/4271580686_55dc751c59_o.png
.. |image7| image:: http://farm3.static.flickr.com/2740/4271585496_4e3598febd_o.png
.. |image8| image:: http://farm3.static.flickr.com/2710/4270853165_d8d898a792_o.png
.. |image9| image:: http://farm3.static.flickr.com/2716/4271628352_a132facbbe_o.png
.. |image10| image:: http://farm5.static.flickr.com/4063/4271628358_be1121dcfd_o.png
.. |image11| image:: http://farm5.static.flickr.com/4031/4271751588_ca254c2792_o.png
.. |image12| image:: http://farm5.static.flickr.com/4019/4271011881_882df169b3_o.png
.. |image13| image:: http://farm5.static.flickr.com/4024/4271772990_332769f37b_o.png
.. |image14| image:: http://farm3.static.flickr.com/2737/4271979493_c0f9f4aeee_o.png
.. |image15| image:: http://farm3.static.flickr.com/2782/4271979499_9aff55080d_o.png
.. |image16| image:: http://farm5.static.flickr.com/4027/4271979501_7c21f2726f_o.png
.. |image17| image:: http://farm5.static.flickr.com/4068/4270788341_d27c2eaa27_o.png
.. |image18| image:: http://farm5.static.flickr.com/4057/4270801259_6c44b88299_o.png
.. |image19| image:: http://farm3.static.flickr.com/2727/4270801263_c488341ddf_o.png
.. |image20| image:: http://farm5.static.flickr.com/4033/4270809413_07af24b775_o.png
.. |image21| image:: http://farm5.static.flickr.com/4051/4270816007_0a91ac6a85_o.png
.. |image22| image:: http://farm3.static.flickr.com/2730/4270822547_31e9a995d8_o.png
.. |image23| image:: http://farm5.static.flickr.com/4044/4271580686_55dc751c59_o.png
.. |image24| image:: http://farm3.static.flickr.com/2740/4271585496_4e3598febd_o.png
.. |image25| image:: http://farm3.static.flickr.com/2710/4270853165_d8d898a792_o.png
.. |image26| image:: http://farm3.static.flickr.com/2716/4271628352_a132facbbe_o.png
.. |image27| image:: http://farm5.static.flickr.com/4063/4271628358_be1121dcfd_o.png
.. |image28| image:: http://farm5.static.flickr.com/4031/4271751588_ca254c2792_o.png
.. |image29| image:: http://farm5.static.flickr.com/4019/4271011881_882df169b3_o.png
.. |image30| image:: http://farm5.static.flickr.com/4024/4271772990_332769f37b_o.png
.. |image31| image:: http://farm3.static.flickr.com/2737/4271979493_c0f9f4aeee_o.png
.. |image32| image:: http://farm3.static.flickr.com/2782/4271979499_9aff55080d_o.png
.. |image33| image:: http://farm5.static.flickr.com/4027/4271979501_7c21f2726f_o.png
