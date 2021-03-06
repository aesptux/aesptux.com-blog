Jerarquía de directorios en Linux
#################################
:date: 2009-09-02 10:26
:author: aesptux
:category: Linux
:tags: directorios, jerarquía, Linux
:slug: jerarquia-de-directorios-en-linux

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/ (raíz): Es el nivel más alto dentro de la jerarquía de directorios. De
aquí cuelgan el resto de carpetas, particiones y otros dispositivos. Es
por esto que donde se instala el sistema, se selecciona la partición
deseada y se le indica que el punto de montaje es justamente /.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/bin (binarios): Los binarios son los ejecutables de Linux. Aquí
tendremos los ejecutables de los programas propios del sistema
operativo, entre ellos comandos como cp, mv, cat, chown, etc. No es el
único directorio que contiene ejecutables como veremos más adelante.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/boot (arranque): Aquí nos encontramos los archivos necesarios para el
inicio del sistema, desde los archivos de configuración de Grub Lilo,
hasta el propio kernel del sistema.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/dev (dispositivos): Linux se basa en la simpleza y en el tratamiento
homogéneo de la información. Linux trata los dispositivos como si fueran
un fichero más para facilitar el flujo de la información. En esta
carpeta tenéis los dispositivos del sistema, por ejemplo los usb, sda (o
hda) con sus respectivos números que indican las particiones, etc.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/etc (etcétera): Aquí se guardan los ficheros de configuración de los
programas instalados, así como ciertos scripts que se ejecutan en el
inicio del sistema. Los valores de estos ficheros de configuración
pueden ser complementados o sustituidos por los ficheros de
configuración de usuario que cada uno tiene en su respectivo “home”
(carpeta personal).

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/home (hogar): Este hogar no es más que un directorio que a su vez
contiene otros, uno por cada usuario dado de alta en el sistema. Dentro
de dichos directorios es donde el usuario tiene su carpeta personal,
donde están los ficheros de configuración de usuario, así como los
archivos personales del mismo que puede crear, modificar y eliminar bajo
su propio criterio.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/lib (bibliotecas): Contiene las bibliotecas (tambien mal conocidas como
librerías) del sistema, así como módulos y controladores (drivers).

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/lost+found (perdido y encontrado): Es una carpeta que nos podemos
encontrar en todas las particiones. Cuando por cualquier circunstancia
se cierra mal el sistema (un apagón por ejemplo), cuando éste se
reinicie comprobaréis que se llamará al programa fsck para restaurar la
integridad del sistema de ficheros. En esta carpeta encontraremos la
información que se mal-guardó debido a la incidencia.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/media (media/medios): Es donde se montan las unidades extraíbles como
los dispositivos USB, disqueteras, unidades de CD/DVD y en algunas
distros, como Ubuntu, las particiones adicionales.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/mnt (montajes): Es un directorio que se suele usar para montajes
temporales de unidades.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/opt (opcionales): Destinado para guardar paquetes adicionales de
aplicaciones.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/proc: Información para la virtualización del sistema de ficheros de
Linux.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/root: Es el /home del administrador. Es el único /home que no está
incluido -por defecto- en el directorio anteriormente mencionado.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/sbin (binarios de sistema): Son los ejecutables de administración,
tales como mount, umount, shutdown…

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/srv (servicios): Información del sistema sobre ciertos servicios que
ofrece (FTP, HTTP…).

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/sys (sistema): Información sobre los dispositivos tal y como los ve el
kernel Linux.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/tmp (temporales): Es un directorio donde se almacenan ficheros
temporales. Cada vez que se inicia el sistema este directorio se limpia.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/usr: Es el directorio padre de otros subdirectorios de importancia:

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/usr/bin: Conjunto de ejecutables de la mayoría de aplicaciones de
escritorio entre otras (por ejemplo firefox).

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/usr/include: Los ficheros cabeceras para C y C++.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/usr/lib: Las bibliotecas para C y C++.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/usr/local: Es otro nivel dentro que ofrece una jerarquía parecida al
propio diretorio /usr.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/usr/sbin: Otra serie de comandos administrativos para el sistema.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/usr/share: Archivos compartidos como ficheros de configuración,
imágenes, iconos, etc.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/usr/src: Tiene en su interior el código fuente para el kernel LInux.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

var: Ficheros de sistema como el buffer de impresión, logs…

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/var/cache: Se almacenan datos cacheados para las aplicaciones.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/var/lib: Información sobre el estado actual de las aplicaciones,
modificable por las propias aplicaciones.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/var/lock: Ficheros que se encargan de que un recurso sólo sea usado por
una aplicación determinada que ha pedido su exclusividad, hasta que ésta
lo libere.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/var/log: Es uno de los subdirectorios más importantes ya que aquí se
guardan todo tipo de logs del sistema.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/var/mail: Los correos de los usuarios.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/var/opt: Datos usados por los paquetes almacenados en /opt.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/var/run: Información sobre el sistema desde que se inició.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/var/spool: Datos esperando a que sean tratados por algún tipo de
proceso.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste" style="position:absolute;left:-10000px;top:0;width:1px;height:1px;">

/var/tmp: Otro fichero temporal.

.. raw:: html

   </div>

**/ (raíz)**: Es el nivel más alto dentro de la jerarquía de
directorios. De aquí cuelgan el resto de carpetas, particiones y otros
dispositivos. Es por esto que donde se instala el sistema, se selecciona
la partición deseada y se le indica que el punto de montaje es
justamente /. Por eso nunca debemos ejecutar el comando *rm -rf /*

**/bin (binarios)**: Los binarios son los ejecutables de Linux. Aquí
tendremos los ejecutables de los programas propios del sistema
operativo, entre ellos comandos como cp, mv, cat, chown, etc. No es el
único directorio que contiene ejecutables como veremos más adelante.

**/boot (arranque)**: Aquí nos encontramos los archivos necesarios para
el inicio del sistema, desde los archivos de configuración de Grub Lilo,
hasta el propio kernel del sistema.

**/dev (dispositivos)**: Linux se basa en la simpleza y en el
tratamiento homogéneo de la información. Linux trata los dispositivos
como si fueran un fichero más para facilitar el flujo de la información.
En esta carpeta tenéis los dispositivos del sistema, por ejemplo los
usb, sda (o hda) con sus respectivos números que indican las
particiones, etc.

**/etc (etcétera)**: Aquí se guardan los ficheros de configuración de
los programas instalados, así como ciertos scripts que se ejecutan en el
inicio del sistema. Los valores de estos ficheros de configuración
pueden ser complementados o sustituidos por los ficheros de
configuración de usuario que cada uno tiene en su respectivo “home”
(carpeta personal).

**/home (hogar, carpeta personal)**: Este hogar no es más que un
directorio que a su vez contiene otros, uno por cada usuario dado de
alta en el sistema. Dentro de dichos directorios es donde el usuario
tiene su carpeta personal, donde están los ficheros de configuración de
usuario, así como los archivos personales del mismo que puede crear,
modificar y eliminar bajo su propio criterio.

**/lib (bibliotecas)**: Contiene las bibliotecas (tambien mal conocidas
como librerías) del sistema, así como módulos y controladores (drivers).

**/lost+found (perdido y encontrado)**: Es una carpeta que nos podemos
encontrar en todas las particiones. Cuando por cualquier circunstancia
se cierra mal el sistema (un apagón por ejemplo), cuando éste se
reinicie comprobaréis que se llamará al programa fsck para restaurar la
integridad del sistema de ficheros. En esta carpeta encontraremos la
información que se mal-guardó debido a la incidencia.

**/media (media/medios)**: Es donde se montan las unidades extraíbles
como los dispositivos USB, disqueteras, unidades de CD/DVD y en algunas
distros, como Ubuntu, las particiones adicionales.

**/mnt (montajes)**: Es un directorio que se suele usar para montajes
temporales de unidades.

**/opt (opcionales)**: Destinado para guardar paquetes adicionales de
aplicaciones.

**/proc**: Información para la virtualización del sistema de ficheros de
Linux.

**/root**: Es el /home del administrador. Es el único /home que no está
incluido -por defecto- en el directorio anteriormente mencionado.

**/sbin (binarios de sistema)**: Son los ejecutables de administración,
tales como mount, umount, shutdown…

**/srv (servicios)**: Información del sistema sobre ciertos servicios
que ofrece (FTP, HTTP…).

**/sys (sistema)**: Información sobre los dispositivos tal y como los ve
el kernel Linux.

**/tmp (temporales)**: Es un directorio donde se almacenan ficheros
temporales. Cada vez que se inicia el sistema este directorio se limpia.

**/usr**: Es el directorio padre de otros subdirectorios de importancia:

**/usr/bin**: Conjunto de ejecutables de la mayoría de aplicaciones de
escritorio entre otras (por ejemplo firefox).

**/usr/include**: Los ficheros cabeceras para C y C++.

**/usr/lib**: Las bibliotecas para C y C++.

**/usr/local**: Es otro nivel dentro que ofrece una jerarquía parecida
al propio diretorio /usr.

**/usr/sbin**: Otra serie de comandos administrativos para el sistema.

**/usr/share**: Archivos compartidos como ficheros de configuración,
imágenes, iconos, etc.

**/usr/src**: Tiene en su interior el código fuente para el kernel
LInux.

**/var:** Ficheros de sistema como el buffer de impresión, logs…

**/var/cache**: Se almacenan datos cacheados para las aplicaciones.

**/var/lib**: Información sobre el estado actual de las aplicaciones,
modificable por las propias aplicaciones.

**/var/lock**: Ficheros que se encargan de que un recurso sólo sea usado
por una aplicación determinada que ha pedido su exclusividad, hasta que
ésta lo libere.

**/var/log**: Es uno de los subdirectorios más importantes ya que aquí
se guardan todo tipo de logs del sistema.

**/var/mail**: Los correos de los usuarios.

**/var/opt**: Datos usados por los paquetes almacenados en /opt.

**/var/run**: Información sobre el sistema desde que se inició.

**/var/spool**: Datos esperando a que sean tratados por algún tipo de
proceso.

**/var/tmp**: Otro fichero temporal.
