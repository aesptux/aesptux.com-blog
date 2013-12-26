Familias de protocolos
######################
:date: 2009-07-21 12:45
:author: aesptux
:category: Networking, Notes
:tags: familias, protocolos
:slug: familias-de-protocolos

Un **protocolo** es un conjunto de reglas perfectamente organizadas y
convenidas de mutuo acuerdo entre los participantes en una comunicación,
cuya misión principal es regular algún aspecto de ésta.

Con el fin de simplificar la complejidad de cualquier red, los
diseñadores de redes han convenido estructurar las diferentes funciones
que realizan y los servicios que proveen en una serie de niveles o
capas.

Las capas están jerarquizadas. De esta manera, cada capa debe ocuparase
exclusivamente de su nivel inmediatamente inferior, a quién solicita
servicios, y del nivel inmediatamente superior, a quien devuelve
resultados.

Llamamos **interfaz**\ o\ **interface** de capa a las normas de
intercomunicación entre capas.

El interfaz, entendido como la definición de los servicios y operaciones
que la capa inferior ofrece a la superior, se gestiona como una
estructura de primitivas. Las primitivas son llamadas entrantes o
salientes en cada una de las capas que sirven para solicitar servicios,
devolver resultados, confirmar las peticionesa, etcétera.

-  **Familia SNA**

**SNA** *(Systems Network Architecture)* es el nombre de la arquitectura
de redes propia de IBM. El modelo OSI se configuró apartir de SNA; de
esta arquitectura toma el número y funciones aproximadas para sus capas.

Una red SNA está constituida por un conjunto de máquinas conectables a
la red que se denominan **nodos**. SNA define cuatro tipos de nodos:
terminales, controladores, procesadores frontales y hosts.

Cada uno de estos nodos tiene al menos una **NAU** *(Network Adress
Unit)* que es el software por el que un proceso puede utilizar la red,
es decir, un punto lógico de lared por el que alguien puede utilizar un
servicio. Para poder utilizar la red, un proceso debe conectarse
directamente a una NAU; a partir de aquí podrá utilizar los recursos de
la red.

-  **Familia NetWare**

**NetWare**, fabricado por Novell, ha sido el sistema operativo de red
más utilizado del mundo. Los servidores NetWare han sido
tradicionalmente dedicados. El resto de las estaciones son
exclusivamente clientes de estos servidores. Otro factor que influye en
el alto rendimiento de la red es el protocolo propietario desarrollado
por Novell, denominado **IPX/SPX** (*Internetwork Packet
eXchange/Sequenced Packed eXchange)* derivado de la red de Xerox **XNS**
*(Xerox Network Service)*.

-  **Familia AppleTalk**

**AppleTalk** es el nombre de la red entre iguales, diseñada por Apple
Computer Corporation, para su utilización en ordenadores Macintosh.
Apple siempre ha tratado de consevar la facilidad de instalación y
configuración en sus desarrollos. Los sistemas de red AppleTalk pueden
ser clasificados según su capa física del modo siguiente:

#. **Red LocalTalk**. Es una red AppleTalk sobre cable serie que
   proporciona unas prestaciones de flujo moderadas. El sistema de
   cableado consiste en un bus lineal.
#. **Red EtherTalk**. Cuando AppleTalk tiene una Ethernet en la capa
   física, recibe el nombre de EtherTalk.
#. **Red TokenTalk**. Es una red AppleTalk sobre una red en anillo del
   tipo Token Ring.

Además las tecnologías Bluetooth y Wi-Fi.

-  **Familia NetBeui**

**NetBeui** es un protocolo desarrollado por IBM en 1985. NetBeui es un
protocolo que controla tanto a los datos como a los mensajes entre
aplicaciones. Cuando un sistema operativo de red implementa el protocolo
NetBeui, los servicios son alcanzados a través del interfaz NetBIOS

-  **Familia TCP/IP**

La tecnología **TCP/IP** *(Transmission Control Protocol/Internet
Protocol)* está definida en un conjunto de documentos denominados
**RFC**\ *(Request For Comments)*. La importancia de TCP/IP es tan
grande que la mayor parte de las redes hablan TCP/IP.
