Recuperar contraseña de root
############################
:date: 2009-07-28 23:00
:author: aesptux
:category: Linux
:tags: contraseña, recuperar, root
:slug: recuperar-contrasena-de-root

No es algo habitual, pero puede que alguna vez se nos olvide nuestra
amada contraseña de root.

Lo que podemos hacer es restablecer la contraseña, para luego establecer
una nueva contraseña.

Tendremos que arrancar en modo “\ ***single***\ ” nuestra distribución.
Para ello **cuando se presente GRUB** editamos la entrada
correspondiente a nuestra distribución con la tecla “\ **e**\ ” y luego
editamos la primera línea para que al final ponga “\ ***linux
single***\ “. Luego basta con pulsar la tecla “\ **b**\ ” para iniciar
la distribución con ese ligero cambio (que no se mantendrá para futuros
inicios).

Con eso tendremos acceso a la consola, a partir de la cual **iremos
haciendo lo siguiente**:

.. raw:: html

   <div>

.. raw:: html

   <div>

::

    cd /etc
    nano passwd

.. raw:: html

   </div>

.. raw:: html

   </div>

Y **buscaremos la línea** (probablemente arriba) que ponga algo como
esto:

.. raw:: html

   <div>

.. raw:: html

   <div>

::

    root:x:0:0:root:/root:/bin/bash

.. raw:: html

   </div>

.. raw:: html

   </div>

Tenemos que **eliminar la “x**\ ” de esa línea de forma que quede así:

.. raw:: html

   <div>

.. raw:: html

   <div>

::

    root::0:0:root:/root:/bin/bash

.. raw:: html

   </div>

.. raw:: html

   </div>

Y **salvamos**\ el fichero,

Ahora hacemos algo similar **con el fichero /etc/shadow**

.. raw:: html

   <div>

.. raw:: html

   <div>

::

    nano shadow

.. raw:: html

   </div>

.. raw:: html

   </div>

Tendremos que **editar la línea que comienza con “root”** para que todo
quede con 4 símbolos de dos puntos (”:”) a continuación. La línea debe
quedar así:

.. raw:: html

   <div>

.. raw:: html

   <div>

::

    root::::

.. raw:: html

   </div>

.. raw:: html

   </div>

Y salvamos el fichero

Ahora ya solo hace falta reiniciar el sistema **como un usuario
normal**, y ya podremos establecer la nueva contraseña de superusuario
con el siguiente comando:

.. raw:: html

   <div>

.. raw:: html

   <div>

::

    su
    passwd

    Vía | MuyLinux

.. raw:: html

   </div>

.. raw:: html

   </div>

