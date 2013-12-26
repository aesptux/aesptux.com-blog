Comunicación a través de la red.
################################
:date: 2010-11-12 12:30
:author: aesptux
:category: Cisco, Networking, Notes
:tags: capitulo 2, Cisco, comunicacion, internetworking, lan, modelo, osi, protocolos, red, tcp/ip, temario, wan
:slug: comunicacion-a-traves-de-la-red

\ **2. Comunicación a través de la red**\ 

\ **2.1. Plataforma para las comunicaciones**

**2.1.1. Elementos de la comunicación**

La comunicación comienza con un mensaje o información que se debe enviar
de una persona o dispositivo a otro. Existen varios elementos

El primero de estos elementos es el origen del mensaje, o emisor. El
segundo elemento de la comunicación es el destino o receptor del
mensaje. Y el tercer elemento, es el canal, que está formado por los
medios que proporcionan el camino por el que el mensaje viaja desde el
origen hasta el destino.

\ *Canal: Medio utilizado para transportar información de un emisor a un
receptor*\ 

 

El término red en este curso se refiere a las redes de datos o
información capaces de transmitir muchos tipos diferentes de
comunicaciones, incluyendo datos computacionales tradicionales, voz
interactiva, vídeo y productos de entretenimiento.

 \ **2.1.2.Comunicación de mensajes**

Los mensajes no pueden mandarse como grandes streams, porque generarían
retrasos, ya que todo sería secuencial.

 

Un método mejor es dividir los datos en partes ?más pequeñas y
manejables para enviarlas por la red. La división del stream de datos en
partes más pequeñas se denomina segmentación. La segmentación de
mensajes tiene dos beneficios principales.

Primero, al enviar partes individuales más pequeñas del origen al
destino, se pueden intercalar diversas conversaciones en la red. El
proceso que se utiliza para intercalar las piezas de conversaciones
separadas en la red se denomina multiplexación.

\ *Multiplexación: Proceso en el que se combinan múltiples corrientes de
datos digitales en una señal.*\ 

Segundo, la segmentación puede aumentar la confiabilidad de las
comunicaciones de red. No es necesario que las partes separadas de cada
mensajes sigan el mismo recorrido a través de la red desde el origen
hasta el destino. Si una ruta de satura con el tráfico de datos, se
pueden direccionar mediante recorridos alternativos.

La desventaja de utilizar segmentación y multiplexación para transmitir
mensajes a través de la red es el nivel de complejidad que se agrega al
proceso.

 \ **2.1.3. Componentes de la red**

Los dispositivos y los medios son los elementos físicos o hardware de la
red. El hardware es generalmente el componente visible de la plataforma
de red, como una computadora portátil o personal, un switch, o el
cableado que se usa conectar estos dispositivos. También existen los
medios inalámbricos, que se transmiten a través del aire mediante radio
frecuencias.

\ *Switch: Dispositivo de red que filtra, reenvía o inunda frames
basándose en*\ \ *la dirección destino de cada frame. Opera en la capa
data-link (Nivel 2)*\ 

Los servicios y procesos son los programas de comunicación, que se
ejecutan en dispositivos conectados a la red. Como por ejemplo
servidores de correo, web hosting, etc.

 \ **2.1.4. Dispositivos finales y su función en la red**

Algunos ejemplos de dispositivos finales son:

-  Máquinas ( estaciones de trabajo, portátiles, servidores, etc)

-  Impresoras de red

-  Teléfonos VoIP

-  Cámaras de seguridad

-  Dispositivos portátiles móviles

 

Dispositivos finales ? Hosts

Un host puede ser el origen o el destino.

 \ **2.1.5. Dispositivos intermediarios y su función en la red**

Algunos dispositivos dependen de dispositivos intermediarios.

\ *Dispositivo intermediario: Dispositivo que conecta*\ \ *de forma
directa con los dispositivos de usuario final o brinda enrutamiento de
usuario final a otras redes. Como el router.*\ 

Ejemplos de dispositivos de red intermediarios:

-  Dispositivos de acceso a la red (hubs, switches y puntos de acceso
   inalámbricos)

-  Dispositivos de internetwork (routers)

-  Servidores y módems de comunicación

-  Dispositivos de seguridad (firewalls)

 

Estos dispositivos utilizan la dirección de host de destino
conjuntamente con información sobre las interconexiones de la red, para
determinar la ruta que deben tomar los mensajes a través de la red.
Realizan las siguientes funciones:

-  Volver a generar y transmitir las señales de datos

-  Conservar información acerca de las rutas que existen a través de red
   y de internetwork

-  Notificar a otros dispositivos los errores y las fallas de
   comunicación

-  Dirigir los datos a lo largo de rutas alternativas cuando hay una
   falla en el enlace

-  Clasificar y dirigir mensajes de acuerdo a las prioridades de QoS

-  Permitir o denegar el flujo de datos de acuerdo a los parámetros de
   seguridad

    \ **2.1.6. Medios de red**

El medio proporciona el canal por el cual viaje el mensaje desde el
origen hasta el destino.

Los medios más comunes son:

-  Hilos metálicos dentro de cables

-  Fibras de vidrio y plástico (cable de fibra óptica)

-  Transmisión inalámbrica

 

\ *Codificación: El proceso de transformación de datos de una forma a
otra.*\ 

 

Tienen diferentes características y beneficios. Los criterios para
elegir un medio de red son:

-  La distancia en la cual el medio puede transportar exitosamente una
   señal

-  El ambiente en el cual se instalará el medio

-  La cantidad de datos y la velocidad a la que se deben transmitir

-  El costo del medio y de la instalación

    \ **2.2.LAN, WAN e Internetworks**

   **2.2.1. Redes de área local**

Las infraestructuras de red pueden variar en gran medida en términos de:

-  El tamaño del área cubierta

-  El número de usuarios conectados

-  El número y los tipos de servicios disponibles

 

Una red individual generalmente cubre una única área geográfica y
proporciona servicios y aplicaciones a personas dentro de una estructura
organizacional común.

Este tipo de red se denomina LAN. Una LAN por lo general está
administrada por una organización única.

\ *Red de área local (LAN): Red local o grupo de redes locales
interconectadas que están bajo el mismo control administrativo.*\ 

\ **2.2.2. Redes de área amplia**

Estas redes conectan las LAN separadas geográficamente.

Las WAN está utilizan dispositivos de red diseñados específicamente para
realizar las interconexiones entre las LAN.

 \ **2.2.3. Internet: una red de redes**

\ **Internetwork**\ 

Una malla mundial de redes interconectadas que cumple estas necesidades
de comunicación humana. Internet se crea por la interconexión de redes
que pertenecen a los proveedores de servicios de internet (ISP)

Estas redes ISP se conectan entre sí para proporcionar acceso.

\ **Intranet**\ 

El término intranet con frecuencia se utiliza para hacer referencia a
una conexión privada de LAN y WAN que pertenece a una organización y
está diseñada para que accedan a ella sólo los miembros y los empleados.

\ *Intranet: Sistema interno de una organización, como un sitio web,
expresamente utilizado por empleados internos o estudiantes. También se
puede acceder de forma remota.*\ 

\ **2.2.4. Representaciones de red**

Términos importantes para recordar son:

-  \ **Tarjeta de interfaz de red(NIC):**\  Una NIC, o adaptador de LAN,
   proporciona la conexión física a la red en la computadora personal u
   otra dispositivo host.

-  \ **Puerto físico:**\  Un conector o conexión en un dispositivo de
   networking donde se conectan los medios a un host u otro dispositivo
   de networking

-  \ **Interfaz:**\  Puertos especializados en un dispositivo de
   internetworking que se conecta a redes individuales. Puesto que los
   routers se utilizan para interconectar redes, los puertos de un
   router se conocen como interfaces de red.

    \ **2.3. Protocolos**

   **2.3.1. Reglas que rigen las comunicaciones**

Son reglas que rigen la comunicación.

La comunicación exitosa entre los hosts de una red requiere la
interacción de gran cantidad de protocolos diferentes. Un grupo de
protocolos interrelacionados que son necesarios para realizar una
función de comunicación se denomina suite de protocolos. Estos
protocolos se implementan en el software y hardware que está cargado en
cada host y dispositivo de red.

 \ **2.3.2. Protocolos de red**

Para que los dispositivos se puedan comunicar en forma exitosa, un nuevo
conjunto de aplicaciones de protocolos debe describir los requerimientos
e interacciones precisos.

\ *Conjunto de aplicaciones: Grupo de componentes que trabajan de forma
cooperativa. TCP/IP es un ejemplo de una suite de protocolos.*\ 

 

Las suites de protocolos de networking describen procesos como los
siguientes:

-  El formato o estructura del mensaje

-  El método por el cual los dispositivos de networking comparten
   información sobre las rutas con otras redes.

-  Cómo y cuándo se transmiten mensajes de error y del sistema entre los
   dispositivos

-  La configuración y la terminación de sesiones de transferencia de
   datos.

    \ **2.3.3. Interacción de los protocolos**

Un ejemplo del uso de una suite de protocolos en comunicaciones de red
es la interacción entre un servidor web y un explorador web. Algunos
ejemplos de protocolos son:

\ **Protocolo de aplicación:**\ 

El protocolo de transferencia de hipertexto (HTTP) es un protocolo común
que rige la forma en que interactúan un servidor web y un cliente web.
Define el contenido y el formato de las solicitudes web

\ **Protocolo de transporte:**\ 

El protocolo de control de transmisión (TCP) es el protocolo de
transporte que administra las conversaciones individuales entre
servidores web y clientes web. TCP divide los mensajes HTTP en pequeñas
partes, denominadas segmentos.

\ **Protocolo de internetwork:**\ 

El protocolo de internetwork más común es el protocolo de internet (IP).
El IP es responsable de tomar los segmentos formateados del TCP,
encapsularlos en paquetes y asignar las direcciones apropiadas y
seleccionar la mejor ruta al host de destino.

\ **Protocolos de acceso a la red:**\ 

Los protocolos de acceso a la red describen dos funciones principales,
la administración de enlace de datos y la transmisión física de datos en
los medios. Los protocolos de administración de enlace de datos toman
los paquetes IP y los formatean para transmitirlos por los medios.

 \ **2.3.4. Protocolos independientes de la tecnología**

Los protocolos describen que funciones se requieren en una regla de
comunicación, pero no se describe cómo realizarlas, es posible que la
implementación de un protocolo sea independiente de la tecnología. Por
ejemplo, http no especifica en que lenguaje debe estar escrito una
página, ni el software de servidor web, ni el sistema operativo.
Significa que se puede acceder a un servidor desde cualquier dispositivo
con cualquier sistema operativo, mientras tenga soporte http.

 

\ **2.4. Uso de modelos en capas**\ 

\ **2.4.1.**\ \ **Beneficios del uso de un modelo en capas**\ 

Beneficios:

Ayuda en el diseño de protocolos, ya que los protocolos que operan en
una capa específica tienen información definida según la cual actúan.

Fomenta competencia, ya que los productos de distintos proveedores
pueden trabajar en conjunto

Evita que los cambios en la tecnología o en las capacidades de una capa
afecten otras capas

Proporciona un lenguaje común para describir las funciones y capacidades
de networking

 

\ **2.4.2.**\ \ **Modelos de protocolo y referencia**\ 

El modelo de interconexión de sistema abierto (OSI) es el modelo de
referencia de internetwork más conocido. Se usa para diseño de redes de
datos, especificaciones y resolución de problemas.

 

TCP/IP es un protocolo modelo porque describe las funciones que ocurren
en cada capa de protocolos dentro de una suite de TCP/IP

Equivalencia entre ambos:

 

\ **2.4.3 Modelo TCP/IP**\ 

 

.. raw:: html

   <div>

El modelo TCP/IP (modelo de Internet ) se creó a principios de la década
de los setenta y se conoce con el nombre de modelo de Internet.
Define cuatro categorías de funciones, 4 capas.
El modelo TCP/IP es un estándar abierto, ninguna compañía controla la
definición del modelo.
Las definiciones del estándar y los protocolos TCP/IP se explican en un
foro público y se definen en un conjunto de documentos disponibles al
público, denominados Solicitudes de comentarios (RFC, Request For
Comments).

.. raw:: html

   </p>

.. raw:: html

   <p>

Capa Aplicación: datos del usuario, control de codificación y de
diálogo.
Capa Transporte: comunicación entre dispositivos de distintas redes
(distintas LAN).
Capa Internet: determina la mejor ruta a través de la red.
Capa Acceso a red: dispositivos y medios de la red (comunicación dentro
de LAN).

.. raw:: html

   </div>

 

\ **2.4.4. Proceso de comunicación**\ 

El modelo TCP/IP describe la funcionalidad de los protocolos que forman
la suite.

Un proceso de comunicación completo incluye estos pasos:

#. Creación de datos en la capa de aplicación del dispositivo final de
   origen

#. Segmentación y encapsulación de datos a medida que pasan por el stack
   de protocolos en el dispositivo final de origen

#. Generación de datos en los medios en la capa de acceso a la red del
   stack

#. Transportación de los datos a través de internetwork, la cual está
   compuesta por medios y por cualquier dispositivo intermediario

#. Recepción de los datos en la capa de acceso en la red del dispositivo
   final de destino

#. Desencapsulación y reensamblaje de los datos a medida que pasan por
   el stack en el dispositivo final de destino

#. Transmisión de estos datos a la aplicación de destino en la capa de
   aplicación del dispositivo final de destino

 

\ **2.4.5.**\ \ **Unidad de datos del protocolo y encapsulación**\ 

Proceso de encapsulación.

La forma que adopta una sección de datos en cualquier capa se denomina
Unidad de datos del protocolo (PDU). En cada etapa del proceso, una PDU
tiene un nombre distinto para reflejar su nuevo aspecto. Se denominan:

Datos: Término general que se utiliza en la capa de aplicación para la
PDU

Segmento: PDU de la capa de transporte

Paquete: PDU de la capa de internetwork

Trama: PDU de la capa de acceso de red

Bits: PDU que se utiliza cuando se transmiten datos físicamente por el
medio

 

\ **2.4.6.**\ \ **Proceso de envío y recepción**\ 

En el ejemplo de la aplicación http:

El protocolo de la capa aplicación, HTTP, comienza el proceso entregando
los datos de la página Web con formato HTML a la capa de transporte.
Allí, los datos de aplicación se dividen en segmentos de TCP. A cada
segmento de TCP se le otorga una etiqueta, denominada encabezado, que
contiene información sobre qué procesos que se ejecutan en la
computadora de destino deben recibir el mensaje.

La capa de transporte encapsula los datos HTML de la página Web dentro
del segmento y los envía a la capa de Internet, donde se implementa el
protocolo IP. Aquí, el segmento de TCP se encapsula en su totalidad
dentro de un paquete IP que agrega otro rótulo denominado encabezado IP.
El encabezado IP contiene las direcciones IP de host de origen y de
destino

Luego el paquete IP se envía al protocolo Ethernet de la capa de acceso
a la red, donde se encapsula en un encabezado de trama. Cada encabezado
de trama contiene una dirección física de origen y de destino. La
dirección física identifica de forma exclusiva los dispositivos en la
red local. Finalmente, los bits se codifican en el medio Ethernet
mediante la NIC del servidor.

Este proceso se invierte en el host receptor. Los datos se desencapsulan
mientras suben al stack hacia la aplicación del usuario final.

 

 

\ **2.4.7.**\ \ **Modelo OSI**\ 

Es un modelo de referencia. Describe cada interacción entre cada capa.

7. Aplicación: Proporciona los medios para la conectividad de extremo a
extremo entre individuos de la red humana que usan redes de datos

6. Presentación: Proporciona una representación común de los datos
transferidos entre los servicios de la capa de aplicación

5. Sesión: Proporciona servicios a la capa de presentación para
organizar su diálogo y administrar el intercambio de datos.

4. Transporte: Define los servicios para segmentar, transferir y
reensamblar los datos para las comunicaciones individuales entre
dispositivos finales. (extremo a extremo)

3. Red: Proporciona servicios para intercambiar datos individuales en la
red entre dispositivos finales identificados.

2. Enlace de datos: Los protocolos de la capa de enlace de datos
describen los métodos para intercambiar tramas de datos entre
dispositivos en un medio común.

1. Física: Describen los medios mecánicos, eléctricos, funcionales y de
procedimiento para activar, mantener y desactivar conexiones físicas
para la transmisión de bits.

 

 

\ **
**\ 

\ **2.5 Direccionamiento de red**\ 

\ **2.5.1 Direccionamiento en la red**\ 

El modelo OSI describe los procesos de codificación, formateo,
segmentación y encapsulación de datos para transmitir por la red. Un
flujo de datos que se envía desde un origen hasta un destino se puede
dividir en partes y entrelazar con los mensajes que viajan desde otros
hosts hacia otros destinos.

 

\ **2.5.2 Envío de datos al dispositivo final**\ 

El primer identificador, la dirección física del host, se incluye en el
encabezado de la PDU de Capa 2 llamada trama. La Capa 2 está relacionada
con la entrega de los mensajes en una red local única. La dirección de
la Capa 2 es exclusiva en la red local y representa la dirección del
dispositivo final en el medio físico. En una LAN que utiliza Ethernet,
esta dirección se denomina dirección de Control de acceso a los medios
(MAC). Cuando dos dispositivos se comunican en la red Ethernet local,
las tramas que se intercambian entre ellos contienen las direcciones MAC
de origen y de destino. Una vez que una trama se recibe
satisfactoriamente por el host de destino, la información de la
dirección de la Capa 2 se elimina mientras los datos se desencapsulan y
suben el stack de protocolos a la Capa 3.

\ **2.5.3 Transporte de datos a través de Internetwork**\ 

Los protocolos de Capa 3 están diseñados principalmente pata mover datos
desde una red local a otra red local dentro de una internetwork.
Mientras las direcciones de Capa 2 sólo se utilizan para comunicar entre
dispositivos de una red local única, las direcciones de Capa 3 deben
incluir identificadores que permitan a dispositivos de red
intermediarios ubicar hosts en diferentes redes

Un dispositivo de red intermediario, por lo general un router,
desencapsula la trama para leer la dirección host de destino contenida
en el encabezado del paquete, la PDU de Capa 3. Los routers utilizan la
porción del identificador de red de esta dirección para determinar qué
ruta utilizar para llegar al host de destino. Una vez que se determina
la ruta, el router encapsula el paquete en una nueva trama y lo envía
por su trayecto hacia el dispositivo final de destino.

\ **2.5.4 Envío de datos a la aplicación correcta**\ 

En la Capa 4, la información contenida en el encabezado de la PDU no
identifica un host de destino o una red de destino. Lo que sí identifica
es el proceso o servicio específico que se ejecuta en el dispositivo
host de destino que actuará en los datos que se entregan. Los hosts,
sean clientes o servidores en Internet, pueden ejecutar múltiples
aplicaciones de red simultáneamente. Cuando los datos se reciben en el
host, se examina el número de puerto para determinar qué aplicación o
proceso es el destino correcto de los datos.

 

 
