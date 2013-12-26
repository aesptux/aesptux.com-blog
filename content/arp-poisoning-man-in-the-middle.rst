ARP Poisoning - Man in the Middle
#################################
:date: 2009-11-28 16:08
:author: aesptux
:category: Networking
:tags: arp, ataque, man in the middle, mitm, poisoning
:slug: arp-poisoning-man-in-the-middle

Ahora aprenderemos a hacer y como funciona (básicamente) un ataque MITM.

Necesitamos ips y macs de los equipos implicados y de la gateway, en mi
caso:

-  Atacante

   -  IP: 172.26.0.34
   -  MAC: 00:80:5a:38:3f:ed
   -  S.O: GNU/Linux Ubuntu 9.10

-  Victima

   -  IP: 172.26.0.33
   -  S.O: Windows 7

-  Gateway

   -  IP: 172.26.0.1
   -  MAC: 00:60:b3:fb:43:b2

Bien ahora desde el atacante, abriremos una sesión del sniffer Wireshark
con el comando *wireshark &*

Si no lo tienes instalado, en distribuciones basadas en Debian basta con
un simple:

    *sudo apt-get install* *wireshark*

[caption id="" align="aligncenter" width="500"
caption="Wireshark"]\ *`|Wireshark|`_*\ [/caption]

Ahora en la víctima comprobaremos como está la tabla ARP, mediante el
comando *arp -a:*

[caption id="" align="aligncenter" width="658" caption="Tabla
Arp"]\ *`|tabla arp|`_*\ [/caption]

Y ahí podemos observar la IP y MAC del atacante y de la gateway.

 

Volvemos al equipo atacante y comenzamos el ataque con Ettercap:

[caption id="" align="aligncenter" width="736"
caption="Ettercap"]\ `|ettercap|`_\ [/caption]

-  -T => Ataque desde consola
-  -q => "Quiet Mode"... Es decir no mostrará nada.
-  -i => Especificamos nuestra interfaz de red
-  -M => Selección de MITM
-  /172.26.0.33/ y /172.26.0.1/ son las víctimas.

[caption id="" align="aligncenter" width="711" caption="Replays Falsos.
Click para ampliar"]\ `|Replays Falsos|`_\ [/caption]

 

Vemos como se envían Replays Falsos.

Ahora comprobemos la tabla ARP de la víctima:

[caption id="" align="aligncenter" width="669" caption="Equipo
envenenado."]\ `|Envenenado.|`_\ [/caption]

La tabla está envenenada. La MAC del gateway queda cambiada a nuestra
dirección MAC, por lo que podremos interceptar el tráfico de la víctima.

Desde la víctima, por ejemplo abrimos una página web.

[caption id="" align="aligncenter" width="500" caption="La victima en
Internet"]\ `|La victima en Internet|`_\ [/caption]

Ahora desde el atacante vamos a mirar si Wireshark a interceptado algo:

[caption id="" align="aligncenter" width="664" caption="Tráfico
interceptado. Click para ampliar"]\ `|Tráfico
interceptado|`_\ [/caption]

Y efectivamente, estamos interceptando el tráfico de la víctima.

Ahora sólo nos queda terminar el ataque:

[caption id="" align="aligncenter" width="692" caption="Terminando el
ataque"]\ `|Terminando el ataque|`_\ [/caption]

Como vemos, Ettercap se encarga de restablecer los parámetros originales
de la víctima.

[caption id="" align="aligncenter" width="669" caption="Todo
restablecido."]\ `|Restablecido|`_\ [/caption]

Una vez finalizado el ataque, las MACs se reestablecen.

.. _|image9|: http://farm3.static.flickr.com/2686/4140832476_9d7b216bdd.jpg
.. _|image10|: http://farm3.static.flickr.com/2780/4140074113_16dc133d44_o.png
.. _|image11|: http://farm3.static.flickr.com/2545/4140072665_fe02b56239_o.png
.. _|image12|: http://farm3.static.flickr.com/2774/4140073275_719731c31c_o.png
.. _|image13|: http://farm3.static.flickr.com/2766/4140833364_16acb05ab4_o.png
.. _|image14|: http://farm3.static.flickr.com/2667/4140833842_e3861ed015.jpg
.. _|image15|: http://farm3.static.flickr.com/2675/4140072861_32043426dc_o.png
.. _|image16|: http://farm3.static.flickr.com/2487/4140073447_0900002436_o.png
.. _|image17|: http://farm3.static.flickr.com/2661/4140833438_450bb001dc_o.png

.. |Wireshark| image:: http://farm3.static.flickr.com/2686/4140832476_9d7b216bdd.jpg
.. |tabla
arp| image:: http://farm3.static.flickr.com/2780/4140074113_16dc133d44_o.png
.. |ettercap| image:: http://farm3.static.flickr.com/2545/4140072665_fe02b56239_o.png
.. |Replays
Falsos| image:: http://farm3.static.flickr.com/2774/4140073275_719731c31c_o.png
.. |Envenenado.| image:: http://farm3.static.flickr.com/2766/4140833364_16acb05ab4_o.png
.. |La victima en
Internet| image:: http://farm3.static.flickr.com/2667/4140833842_e3861ed015.jpg
.. |Tráfico
interceptado| image:: http://farm3.static.flickr.com/2675/4140072861_32043426dc_o.png
.. |Terminando el
ataque| image:: http://farm3.static.flickr.com/2487/4140073447_0900002436_o.png
.. |Restablecido| image:: http://farm3.static.flickr.com/2661/4140833438_450bb001dc_o.png
.. |image9| image:: http://farm3.static.flickr.com/2686/4140832476_9d7b216bdd.jpg
.. |image10| image:: http://farm3.static.flickr.com/2780/4140074113_16dc133d44_o.png
.. |image11| image:: http://farm3.static.flickr.com/2545/4140072665_fe02b56239_o.png
.. |image12| image:: http://farm3.static.flickr.com/2774/4140073275_719731c31c_o.png
.. |image13| image:: http://farm3.static.flickr.com/2766/4140833364_16acb05ab4_o.png
.. |image14| image:: http://farm3.static.flickr.com/2667/4140833842_e3861ed015.jpg
.. |image15| image:: http://farm3.static.flickr.com/2675/4140072861_32043426dc_o.png
.. |image16| image:: http://farm3.static.flickr.com/2487/4140073447_0900002436_o.png
.. |image17| image:: http://farm3.static.flickr.com/2661/4140833438_450bb001dc_o.png
