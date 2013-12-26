Detectar intrusos en nuestra red privada.
#########################################
:date: 2009-12-15 10:29
:author: aesptux
:category: Linux, Networking
:tags: casa, detectar, intrusos, netdiscover, nmap, privada, red, wifi
:slug: detectar-intrusos-en-nuestra-red-privada

Todos nos hemos preguntado alguna vez si alguien se conectará sin
nuestro permiso a nuestra red... Pues para averiguar si hay algún
intruso es bastante simple:

    nmap -sP x.x.x.x/xx

o

    nmap -sP x.x.x.x-xx

Donde -sP indica que es un simple escaneo por ping, para determinar si
un host está online o no. Por ejemplo:

    nmap -sP 172.26.0.0/24

Para este caso deberemos conocer los bits que se utilizan para construir
la subred.

    nmap -sP 172.26.0.1-255

En este caso basta con indicar un rango de direcciones ip.

[caption id="" align="alignnone" width="655"
caption="Resultado."]\ `|nmap|`_\ [/caption]

También podemos usar netdiscover:

    netdiscover -i interfaz -r x.x.x.x/xx -s tiempo

Por ejemplo, en mi caso:

    netdiscover -i wlan0 -r 172.26.0.0/24 -s 0.5

-  -i => Indica el interfaz de red que estamos usando
-  -r => rango a escanear
-  -s => tiempo de espera entre cada petición ARP

Y sólo con eso podremos estar informados de las conexiones que se
produzcan a nuestra red.

.. _|image1|: http://farm3.static.flickr.com/2607/4185691095_383933128e_o.png

.. |nmap| image:: http://farm3.static.flickr.com/2607/4185691095_383933128e_o.png
.. |image1| image:: http://farm3.static.flickr.com/2607/4185691095_383933128e_o.png
