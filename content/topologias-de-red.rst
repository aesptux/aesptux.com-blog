Topologías de red
#################
:date: 2009-07-17 13:16
:author: aesptux
:category: Networking, Notes
:tags: red, topologías
:slug: topologias-de-red

La **topología** de una red es la propiedad que indica la forma física
de la red, es decir, el modo en que se disponen los equipos y el sistema
de cableado  que los interconecta para cumplir su función.

-  Topologías en estrella.

Las estaciones se conectan entre sí a través de un nodo especialmente
privilegiado que ocupa la posición central de la red, formando con el
resto de las estaciones una estrella. A este nodo se le denomina
**estación concentradora de la estrella**.

La ventaja pricipal de una red en estrella reside en la seguridad. El
concentrador tiene las funciones tanto de intercomunicador entre
cualesquiera dos estaciones, como de aislador de los problemas que
pudieran surgir en cualquiera de los segmentos, de modo que si un
segmento se deteriora, sólo él se queda sin servicio de red.

Sin embargo, el problema de la topología en estrella se presenta en el
entorno del concentrador, ya que todos los segmentos deben terminar en
él, lo que conlleva una importante madeja de cables.

-  Topología en anillo

Una red en anillo conecta todos sus equipos en torno a un anillo físico.
Sin embargo, una rotura en el anillo produce el fallo general de la red.
Un ejemplo de red en anillo es la red **Token Ring**, que sigue el
estándar IEEE 802.5.

Las redes de anillo utilizan protocolos libres de colisiones. Las
señales recorren el anillo a la velocidad de la luz en el medio de
transporte y requieren retardadores para evitar que unos bits se
superpongan a otros, no hay que olvidar que la transmisión en una red en
anillo, es secuencial, y es posible que cuando una estación quiera poner
en la red el bit siguiente, todavía no se haya terminado de transmitir
por el anillo anterior. También son necesarios elementos
bidireccionalmente selectivos para  conseguir que la trasmisión se
produzca en un sólo sentido en el anillo. Podemos deducir que un anillo
no es simplemente un bus cerrado por sus extremos, sino que requiere una
tecnología electrónica avanzada.

El dispositivo encargado de realizar físicamente el anillo se
llama\ **MAU** (Multistation Access Unit), que no es má que un tipo de
concentrador especializado al que se conectan las estaciones. Este
hardware tiene una serie de componentes de conmutación que crean un
nuevo anillo cada vez que sae conecta una nueva estación como segmento
de la estrella.

-  Topología en bus

Los puestos  de una red en bus se conectan a una única  línea de
transmisión (bus) que recorre la ubicación física de todos los
ordenadores. Esta red es muy simple en su funcionamiento, pero es muy
sensible a problemas de tráfico o a las roturas de los cables.

El medio de transmisión que forma la red es un único bus multiacceso
compartido por todos los nodos, y se debe establecer una contienda para
determinar quién tiene derechos de acceso a los recursos de comunicación
en cada instante. Este sistema de contienda determina el tipo de red. El
bus tiene una estructura lineal. Con el fin de evitar ecos o reflexiones
no deseadas que perjudiquen las condiciones eléctricas de transmisión,
los extremos de este bus deben estar terminados con unos acopladores de
impedancia eléctrica o terminadores, específicos para el tipo de cable
que se trate. Son típicos los cables coaxiales RG-58. La ruptura del bus
impide totalmente la comunicación entre cualesquiera dos nodos de la
red.

-  Topología en malla

Se trata de construir una malla de cableado situando los nodos de la red
en las intersecciones de la malla. De este modo, cada nodo está a
siempre conectado con líneas punto a punto con cualquier otro nodo
adyacente.

-  Topología en árbol

Es una extensión de la topología en bus. Consiste en la conexión de
distintos buses lineales (ramas) a un nuevo bus troncal del que reparte
la señal hacia las ramas.

-  Topología de interconexión total

Consiste en conectar todos los ordenadores, de una red entre sí a través
de líneas punto a punto.

-  Topologías mixtas

En este caso, la topología de la red es una mezcla de las topologías
básicas describidas anteriormente.
