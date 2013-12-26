Servidor DNS
############
:date: 2010-03-17 11:49
:author: aesptux
:category: Linux, Networking, Tutorial
:tags: dns, montar, que es, servidor, teoria
:slug: servidor-dns

7 SERVICIO DNS

#. 

   #. **¿Qué es el servicio DNS?**

El servicio DNS (Domain Name System), o servicio de nombre de dominio,
gestiona y mantiene de forma distribuida las direcciones de Internet y
los nombres de sistema.

En una red TCP/IP las máquinas se identifican mediante su dirección de
red o número IP. Sin embargo, para las personas resulta mucho más cómodo
recordar un nombre que se asocia a una máquina concreta, ya que la
dirección IP puede cambiar.

Esto hace necesario establecer un mecanismo de traducción de nombres de
maquinas a direcciones IP. DNS es el servicio que proporciona este
mecanismo de traducción.

#. 

   #. **El espacio de nombres de dominio**

El servicio DNS se compone de una base de datos distribuida. En esta
base de datos se almacenan las asociaciones de nombres de dominios y
direcciones IP.

La base de datos de DNS está clasificada por nombres de dominio, donde
cada nombre de dominio es una rama en un árbol invertido llamado espacio
de nombres de dominio. El árbol comienza en el nodo raíz situado en el
nivel superior. Por debajo de él pueden existir un número indeterminado
de nodos de nivel inferior.

Los nodos se identifican mediante nombres no nulos. El nombre completo
de un nodo está formado por el conjunto de de nombres que forman la
trayectoria desde ese nodo hasta el nodo raíz. Este nombre de dominio
completo se llama nombre de dominio completamente cualificado o Fully
Qualified Domain Name. El FQDN de cualquier nodo del árbol debe acabar
siempre con un punto.

Los diferentes servidores DNS que existen en la red almacenan la
información relativa a los nombres de dominio DNS en los llamados
registros de recursos. Le permiten responder a las peticiones de nombres
relativas a la parte del espacio de nombres de dominio.

Los principales TLD son: .com, .edu, .net, .org, .gov.

Como parte del espacio de nombres de dominio también existen dominios de
primer nivel que designan zonas geográficas.

Organismo en España ? ESNIC

#. 

   #. **¿Cuándo se necesita DNS?**

Un servicio DNS se define como:

-  Un espacio de nombres jerárquico para las máquinas y las direcciones
   IP.
-  Una base de datos distribuida que contiene asociaciones de nombres de
   dominios a direcciones IP.
-  Un resolvedor (resolver) o biblioteca de rutinas que permite realizar
   consultas a esa base de datos.
-  Un protocolo para intercambiar información de nombres.

Los sitios web utilizan el servicio DNS ya que mantener un archivo local
/etc/hosts con una relación de todas las máquinas no es viable.

Cada servidor de DNS mantiene uno o varios elementos de la base de datos
distribuida que componen el servicio DNS.

Si la red es pequeña se puede configurar un servidor en uno de los
equipos o pedir al ISP que proporcione este servicio en su nombre.

Si es el sistema es muy grande, debe tener varios dominios DNS.

#. 

   #. **¿Qué es la delegación?**

DNS es una base de datos distribuida y por lo tanto permite su
administración descentralizada.

La delegación de dominios es el mecanismo que permite llevar a cabo es
administración descentralizada. Es decir, el dominio puede ser divido en
subdominios y el control de cada subdominio puede ser delegado. Debe
asumir también la responsabilidad de mantener los datos actualizados.

La división de un dominio en subdominios no implica siempre la cesión de
la autoridad sobre ellos.

#. 

   #. **Dominios y zonas**

El servidor de nombres almacena información acerca de algunas partes del
espacio de nombres de dominio. Cada una de esas partes se llama zona, y
se dice que el servidor de nombres tiene autoridad sobre una zona.

La zona es un archivo que contiene determinados registros de la base de
datos del espacio de nombres de dominio.

**Diferencia entre dominio y zona: El dominio es un subárbol del espacio
de nombres de dominio, es decir, un nodo con todos los nodos por debajo
de él.**

**La zona es un archivo que contiene determinados registros de la base
de datos del espacio de nombres de dominio.**

Un servidor de nombres de dice que es primario cuando obtiene la
información de sus zonas de sus archivos locales. Todas las
modificaciones sobre una zona, como añadir dominios, se llevan a cabo en
el servidor primario.

Un servidor de nombres se dice que es secundario cuando obtiene la
información de su zona o zonas de otro servidor de nombres.

Las transferencias de zona son solicitadas por servidores de nombre
secundarios con el objetivo de mantener actualizada la información
acerca de la zona para tenerla así correctamente duplicada. Es
interesante que, para cada zona, exista al menos un servidor primario y
otro secundario. En el caso de fallo de alguno de ellos, el otro atiende
las peticiones de resolución de nombres.

Un servidor de nombres de nombres se dice que es caché cuando sólo
atiende consultas de los clientes DNS.

#. 

   #. **Servidor de nombres autoritario**

Se define un servidor de nombres de dominios DNS autoritario para una
zona como aquel que contiene los registros de recursos para dicha zona.
Para ello se utilizan los registros de recursos SOA y NS.

Si el servidor es secundario, los registros de recursos de la zona se
cargan desde otro servidor de nombres utilizando el proceso de
transferencia de zona.

**7.9Base de datos del protocolo DNS**

Cada servidor de nombres de dominio mantiene una base de datos que sirve
para asociar los nombres de dominios con direcciones IP llamada archivos
de la zona, y una base de datos de resolución inversa llamada archivos
de resolución inversa de la zona. El formato de estas bases de datos es
de archivos de textos.

Para resolver nombres los servidores DNS consultan las zonas, las cuales
contienen los registros de recursos (RR) que describen la información
relativa al dominio DNS.

La descripción de cada uno de los campos es:

-  **Propietario:**\ nombre de máquina o dominio DNS al que pertenece el
   recurso. Puede contener un nombre de máquina/dominio.
-  **TTL:**\ (Time To Live) tiempo de vida o número de segundos que
   puede estar el registro en la caché. Si contiene un '0' indica que no
   tiene que ser almacenado en caché.
-  **Clase:**\ define la familia de protocolos en uso. Suele ser siempre
   'IN' de Internet, que representa una red TCP/IP.
-  **Tipo:**\ identifica el tipo de registro.
-  **RDATA:**\ información específica del tipo de recurso.

TIPOS DE REGISTRO

+--------------------------+------------------------+-------------------------------------------------------------------------------------+
| **Nombre del recurso**   | **Tipo de registro**   | **Función**                                                                         |
+--------------------------+------------------------+-------------------------------------------------------------------------------------+
| Inicio de autoridad      | SOA                    | Identifica al servidor autoritario de una zona y sus parámetros de configuración.   |
+--------------------------+------------------------+-------------------------------------------------------------------------------------+
| Servidor de nombres      | NS                     | Identifica servidores de nombres autorizados para una zona.                         |
+--------------------------+------------------------+-------------------------------------------------------------------------------------+
| Dirección                | A                      | Asocia un nombre de dominio FQDN con una dirección IP                               |
+--------------------------+------------------------+-------------------------------------------------------------------------------------+
| Puntero                  | PTR                    | Asocia una IP a un dominio FQDN. Para búsquedas inversas                            |
+--------------------------+------------------------+-------------------------------------------------------------------------------------+
| Registro de correo       | MX                     | Indica máquinas encargadas de la entrega de correo en el dominio                    |
+--------------------------+------------------------+-------------------------------------------------------------------------------------+
| Nombre canónico          | CNAME                  | Permite asignar uno o más nombres a una máquina                                     |
+--------------------------+------------------------+-------------------------------------------------------------------------------------+
| Text                     | TXT                    | Almacena cualquier información                                                      |
+--------------------------+------------------------+-------------------------------------------------------------------------------------+
| Servicio                 | SRV                    | Ubicación de los servidores para un servicio.                                       |
+--------------------------+------------------------+-------------------------------------------------------------------------------------+

**A) Registro de recurso SOA**

La configuración de cada zona comienza con el registro de recursos de
Inicio de Autoridad o SOA (Start of Authority).

-  **Propietario:**\ nombre de dominio de la zona
-  **Tipo:**\ SOA
-  **Persona responsable:**\ contiene la dirección de correo electrónico
   del responsable de la zona.
-  **Número de serie:**\ Número de versión de la zona. Sirve de
   referencia a los servidores secundarios de la zona para saber cuando
   deben hacer una transferencia (actualizar la base). Si el número de
   serie del servidor secundario es menor que el número de serie del
   primario, significa que en el primario ha cambiado la información de
   la zona, y por tanto el secundario debe solicitar al primario una
   transferencia de zona. Este número debe ser incrementado de forma
   manual por el administrador de la zona cada vez que realiza un cambio
   en algún registro de la zona. Se suele utilizar el formato
   AAAA/MM/DD/NN.
-  **Actualización (Refresh Time):**\ indica cada cuánto tiempo un
   servidor secundario debe contactar con el servidor primario para
   comprobar los cambios en la zona.
-  **Reintentos (Retry time):**\ si la transferencia de zona ha fallado,
   este parámetro indica el tiempo que espera el servidor secundario
   antes de volver a intentarlo.

-  **Caducidad (Expire Time):**\ indica el tiempo de caducidad, en
   segundos de la información acerca de la zona en un servidor
   secundario.
-  **TTL Mínimo (Minimal Time To Live):**\ indica el tiempo de validez
   del registro SOA, número de segundos que la información sobre el
   registro se mantiene en el servidor de nombres de dominio.

Ejemplo:

aulaESI.com. IN SOA servidor.aulaESI.com.

( 200051701; número de serie

10800; actualización

900; reintentos

604800; caducidad

86400; valor TTL

)

**B) Registro de recurso NS (NameServer)**

El registro de recurso NS establece los servidores de nombres
autorizados para la zona. Cada zona debe contener registros indicando
tanto los servidores primarios como los secundarios. Por tanto, cada
zona debe contener registros indicando tanto los servidores primarios
como los secundarios. Como mínimo un registro NS por zona.

Ejemplo:

aulaESI.com. IN NS servidor.aulaESI.com.

**C)Registro de recurso A (Address)**

Establece una correspondencia entre un FQDN y una dirección IP. Cada
registro A identifica un nombre de máquina y el cliente DNS puede
obtener a través de él su dirección IP.

Ejemplo de registro que se asigna una dirección a la maquina pc02:

pc02.aulaESI.com. IN A 192.168.1.2

**D)Registro de recurso PTR (PoinTeR)**

El registro de recurso PTR hace lo contrario que el registro A, es decir
asigna una dirección IP a un FQDN. Este tipo de recursos se utilizan en
la resolución inversa.

Ejemplo:

2.1.168.192.in-addr-arpa IN PTR pc02.aulaESI.com.

**E)Registro de recurso CNAME (Nombre canónico)**

Crea un alias para el nombre de dominio especificado.

Por ejemplo, a la maquina pc02 se le asigna el alias prueba:

prueba.aulaESI.com. IN CNAME pc02.aulaESI.com.

**F)Registro de recurso MX (Mail eXchange)**

Es un registro de correo, e indica una o varias máquinas encargadas de
la entrega de correo en el dominio. Si el dominio tiene varias máquinas
como registros MX se puede indicar, mediante un valor numérico, el orden
de preferencia de máquina que seguirá el servidor que envía el correo
para hacer la entrega del mismo.

Ejemplo:

AulaESI.com. IN MX 0 mail.aulaESI.com.

AulaESI.com. IN MX 1 maildos.aulaESI.com.

**G)Registro de recurso SRV (SeRVice)**

Los registros de recursos SRV especifican los servidores disponibles
para un servicio o protocolo determinados, como www o FTP.

http.tcp.aulaESI.com. IN SRV 0 0 80 www.aulaESI.com

ftp.tcp.aulaESI.com. IN SRV0 0 80 ftp.aulaESI.com.

#. 

   #. **Métodos de búsqueda**

      #. **Resolución de nombres**

La resolución de nombres es un mecanismo por el que se traducen los
nombres de máquinas, dados por los usuarios al conectarse a servidores
remotos, a direcciones IP.

-  **Búsqueda recursiva:**\ Se realiza una petición de resolución de
   nombre al servidor DNS local, y si el servidor no dispone de la
   información solicitada va a buscarla al servidor de nombres con
   autoridad que la contiene. Para ello, el servidor de nombres local
   necesita consultar a un servidor raíz y éste le dará la información
   acerca de aquellos servidores de nombres autoritarios intermedios
   hasta llegar al servidor que contiene el nombre del dominio objeto de
   la consulta. En este caso, el servidor local asume la responsabilidad
   de dar una respuesta al cliente y él consulta a los otros servidores
   en nombre del cliente.
-  **Búsqueda iterativa:** el servidor DNS local devuelve la mejor
   respuesta que puede ofrecer al cliente en función del contenido de su
   caché, pero si el servidor no dispone de la información solicitada
   indica la ip del siguiente servidor de nombres autorizado a
   preguntar, comenzando siempre por un servidor raíz. Éste le refiere
   al servidor del nivel siguiente que lo contiene, y el servidor local
   vuelve a lanzar la petición (iteración) al servidor referido, el
   cual, si no dispone de la información solicitada, le refiere al
   servidor del nivel siguiente que lo contiene; a continuación, el
   servidor DNS local vuelve a lanzar la petición al servidor referido y
   así sucesivamente hasta llegar al servidor de nombres que contiene la
   información acerca del dominio solicitado.

#. 

   #. **Configuración de un servidor DNS en Debian GNU/Linux**

El servicio DNS está compuesto por dos programas.

-  El demonio named: es el servidor de nombres de dominio, el que
   contiene la base de datos y responde a las peticiones
-  el resolver (cliente): es el que genera las peticiones. Es un
   conjunto de rutinas que permiten que los clientes accedan a los
   servidores de nombres para resolver la búsqueda de una dirección ip
   asociada a un nombre

El archivo de configuración del demonio named es /etc/bind/named.conf.

Las zonas específicas del servidor DNS se definen en
/etc/bind/named.conf.local

Para lanzar el servicio: /etc/init.d/bind9 start

Archivos de configuración implicados:

-  /etc/bind/named.conf
-  /etc/bind/named.conf.local
-  /etc/bind/db.aulaESI.com
-  /etc/bind/db.192.168.1

**EJEMPLO NAMED.CONF.LOCAL**

/\* resolución normal \*/

zone “aulaESI.com” {

type master;

allow-query {127.0.0.1 ; 192.168.1.1/24; }

allow-transfer { slaves;}

file “/etc/bind/db.aulaESI.com”;

};

/\*resolucion inversa \*/

zona “1.168.192.in-addr.arpa” {

type master;

allow-query {127.0.0.1 ; 192.168.1.1/24; }

allow-transfer { slaves;}

file “/etc/bind/db.192.168.1”;

};

**EJEMPLO DB.AULAESI.COM**

aulaESI.com. IN SOA servidor.aulaESI.com.

( 1;

10800;

900;

604800;

86400;)

aulaESI.com. IN A 192.168.1.1

aulaESI.com. IN NS servidor.aulaESI.com.

servidor IN A 192.168.1.1

cups IN CNAME servidor

www in CNAME servidor

pc02 IN A 192.168.1.2

pc03 IN A 192.168.1.3

**EJEMPLO DB.192.168.1**

aulaESI.com. IN SOA servidor.aulaESI.com.

(1;

10800;

900;

604800;

86400;)

aulaESI.com. IN NS servidor.aulaESI.com.

1 IN PTR gateway.aulaESI.com.

1 IN PTR servidor.aulaESI.com.

2 IN PTR pc02.aulaESI.com.

3 IN PTR pc03.aulaESI.com.
