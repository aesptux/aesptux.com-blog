Manual SSH
##########
:date: 2009-06-13 11:23
:author: aesptux
:category: Linux, Networking, Tutorial
:tags: ssh, Tutorial
:slug: manual-ssh

SSH son las siglas de **S**\ ecure **SH**\ ell. Lo que te ofrece es una
consola en un ordenador remoto con los privilegios que tenga la cuenta
con la que conectes. Es decir, si en tu PC tienes varias cuentas, puedes
conectar desde otro ordenador al tuyo con cualquiera de esas cuentas y
sus respectivos privilegios, como pudiera ser la cuenta root, la de tu
administrador sudo o la de un usuario normal sin poder de
administración. Y todo esto con encriptación de datos.

Mola ¿No?

También cabe decir que tener un servidor SSH en funcionamiento, tiene un
cierto riesgo, pero vamos configurarlo para que el riesgo sea muy
reducido.

Lo primero es instalarlo

.. raw:: html

   <div id="content_view">

.. raw:: html

   </p>

::

    $ sudo aptitude install ssh

Ahora una vez instalado, vamos a configurarlo:

::

    $ sudo gedit /etc/ssh/sshd_config

Si alguna de las opciones que diga no os aparece, podeis añadirlo
libremente al final del documento de configuración.
 La primera opción a modificar es el puerto por defecto.
 Podemos poner por ejemplo el puerto:

::

    port 2413

Más abajo está la opcion Protocol, que debe estar a 2. Si no es así,
ponedlo a 2.

LoginGraceTime es el tiempo que tendrá el usuario para escribir su
login, si sabemos la contraseña y usuario, no tardaremos mucho en poner
el login así que este valor debe ser de pocos segundos por ejemplo 20

::

    LoginGraceTime 20

Justo debajo, está una de las opciones más importantes PermitRootLogin.
Esta opción permitirá loguearse como root, pero esto es muy inseguro
porque si alguien quiere entrar en nuestro ordenador ya tendría el
usuario (que siempre es root) y sólo le faltaría la contraseña, por eso
debemos deshabilitarlo, nosotros podremos usar sudo para tareas
administrativas.

::

    PermitRootLogin no

también podremos establecer una "dedocracia" y seleccionar que usuarios
queremos que se conecten

::

    AllowUsers mortuus amigo@83.45.258.21

*Donde mortuus es nuestro usuario (al que permitimos que se conecte) y
amigo el usuario de la persona que damos permiso.*

Otra interesantísima opcion es MaxAuthTries, que es el número máximo de
intentos que tendrá el usuario para introducir su login o será
desconectado. En mi opinión con un valor de 2, es suficiente. Así
evitamos posibles crackeos por fuerza bruta.

::

    MaxAuthTries 2

Podemos establecer el número de conexiones paralelas. Este valor
dependerá de nuestro interés y de la función que vaya a tener el
ordenador, si es personal con un valor de 1 o 2 vamos bien

::

    MaxStartups 1

Ahora ya podemos cerrar el editor y reiniciar el servidor ssh

::

    $ sudo /etc/init.d/ssh restart

Para añadir más seguridad, la contraseña debe ser segura. Es decir
contraseñas como "1", "123456", "god", "contraseña", "hola"... etc son
inseguras.
 Se recomienda usar un mínimo de 6 caracteres y no usar palabras que
aparezcan en el diccionario (imaginad porque xD)
 Una contraseña realmente segura podría ser algo así:
\*$M0rT[]Us\*-\*rUl3s$\*

**Uso de SSH**

Para conectar:

::

    $ ssh -p puerto tu_cuenta@ip_del_ordenador_remoto

Para copiar archivos:

::

    $ scp ruta/archivo cuenta_en_ordenador_presente@ip_ordenador_presente:ruta/fichero

Un poco lioso, vamos a verlo con un ejemplo

::

    $ scp /home/casa/Desktop/xxx.jpg familia@192.168.1.6:/home/familia/pokemon.jpg

Como estamos conectados a casa, queremos copiar el archivo xxx.jpg, pues
tendremos que indicar cual es nuestra ubicación "real", estamos en la
cuenta familia, en la ip 192.168.1.6 y lo vamos a copiar a /home/familia
y de paso lo renombramos a pokemon.jpg

.. raw:: html

   </div>

