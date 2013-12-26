Túnel para el tráfico web. Proxy socks
######################################
:date: 2011-01-03 11:55
:author: aesptux
:category: Linux, Networking
:tags: datos, encriptar, firefox, proxy, socks, ssh, trafico, túnel, tunneling, web
:slug: tunel-para-el-trafico-web-proxy-socks

A través de un compañero de clase, descubrí esta forma de tunelizar
nuestro tráfico web de una red insegura. Este túnel encripta cualquier
dato, por lo que estaría fuera del alcance de cualquier sniffer también.

Necesitaremos dos máquinas: Una será el servidor SSH que hará el
forwarding de puertos, y otro será la máquina que creará el túnel hacia
el servidor

En el servidor debe estar instalado openssh.

    # apt-get install openssh

En el servidor, editamos el archivo **/etc/ssh/sshd\_config**\ y al
final añadimos las siguientes líneas:

    AllowTcpForwarding yes

    GatewayPorts yes

Y guardamos el archivo.

Ahora tenemos activado el forwarding de puertos en el servidor.

Ahora en la máquina que creará el túnel y en la cuál queremos que el
tráfico sea seguro, hacemos lo siguiente

     

    .. raw:: html

       <div>

    ssh -N -p PORT user@sshserver -D 2080 -v

    .. raw:: html

       </div>

     

 

.. raw:: html

   <div>

Donde:

.. raw:: html

   </div>

.. raw:: html

   <div>

-  - N -> Impide que se ejecuten comandos
-  -p -> Indica el puerto SSH a usar en caso que no sea el 22
-  -D -> Indica un puerto dinámico. He puesto 2080 sin ningún motivo en
   especial
-  -v -> Verbose mode.

.. raw:: html

   </div>

.. raw:: html

   <div>

Y ahora en Mozilla Firefox, establecemos el proxy socks v5 a "localhost"
y el puerto "2080"

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Y con eso tendríamos nuestro tráfico web protegido.

.. raw:: html

   </div>

 

     
