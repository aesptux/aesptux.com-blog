El encaminador
##############
:date: 2009-07-25 16:15
:author: aesptux
:category: Networking, Notes
:tags: encaminador, router
:slug: el-encaminador

Los encaminadores, enrutadores o routers son dispositivos software o
hardware que se pueden configurar para encaminar paquetes entre sus
distintos puertos de red utilizando la dirección lógica correspondiente
a la internet.

El encaminador interconecta redes de área local operando en el nivel 3
de OSI, por tanto su funcionalidad está fuertemente condicionada por el
protocolo de red.  Esto hace que su rendimiento sea menor, ya que gasta
menos tiempo de proceso en analizar los paquetes de nivel de red que
llegan.

Los routers confeccionan una tabla de encaminamientoen donde registran
qué nodos y redes son alcanzables por cada uno de sus puertos de salida.

-  **Algoritmos de encaminamiento estático.** Requiren que la tabla de
   encaminamiento sea programada por el administrador de red.
-  **Algoritmos de encaminamiento adaptativo.**\ Son capaces de aprender
   por sí mismos la topología de la red. Son mucho más flexibles que los
   estáticos, aunque su rendimiento es menor.

**Protocolos de encaminamiento**

-  **RIP**\ *(Routing Information Protocol)*\ es un algoritmo  de tipo
   vector basado en la RFC 1058 apropiado para encaminamiento en redes
   IP pequeñas. RIP utiliza el puerto UDP número 520 para el intercambio
   de la información de encaminamiento con otros enrutadores, que se
   calcula como el cómputo de saltos de red necesarios para que un
   paquete dado alcance su destino.
-  **OSPF**\ *(Open Shortest Path First)*\ es otro algoritmo
   caracterizado por que el envío de paquetes siempre se realiza por la
   ruta más corta entre las disponibles.
-  **BGP**\ *(Border Gateway Protocol)*\ es un protocolo de frontera
   exterior, es decir, se ejecuta en los encaminadores que forman el
   perímetro de la red y facilitan extraodinariamente el interambio de
   rutas con los encaminadores exteriores.

**Características fundamentales de los encaminadores**

-  Interpretan las direcciones lógicas de capa 3
-  Son capaces de cambiar el formato de la trama, ya que operan a un
   nivel superior a ésta
-  Poseen un elevado nivel de inteligencia y pueden manejar distintos
   protocolos
-  Proporcionan seguridad a la red puesto que se pueden configurar para
   restringir accesos a la red.
-  Reducen la congestión de la red aislando de tráfico las distintas
   subredes que interconectan.

