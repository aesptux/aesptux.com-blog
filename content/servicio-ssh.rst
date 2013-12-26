Servicio SSH
############
:date: 2010-04-18 22:01
:author: aesptux
:category: Networking
:tags: algortimos, clave, Networking, privada, publica, servicio, ssh
:slug: servicio-ssh

#. 

   #. ¿\ **Qué es el servicio SSH?**

Inicialmente la administración remota se hacía con la orden Telnet.

En la actualidad no se debería utilizar Telnet por los importantes
agujeros de seguridad que presenta. La transmisión entre cliente y el
servidor se realiza completamente en texto plano (sin cifrar), por lo
que con cualquier sniffer es posible capturar tramas y obtener de ellas
login y la contraseña del usuario.

En la actualidad la herramienta de administración remota más utilizada
es Secure Shell (SSH). SSH es un protocolo para iniciar sesiones en
máquinas remotas que ofrecen autenticación, confidencialidad e
integridad.

SSH es una herramienta que permite realizar conexiones seguras entre
equipos unidos mediante una red insegura, como puede ser Internet.
Utiliza el puerto 22 y sigue el modelo cliente-servidor.

La seguridad de Ssh se basa en la utilización de mecanismo de
criptografía, de forma que toda transmisión de información es cifrada y
el mecanismo de autenticación es transparente al usuario.

**Ventajas de utilizar SSH**

-  Después de la primera conexión, el cliente puede saber que se está
   conectando al mismo servidor en futuras sesiones.
-  El cliente transmite al servidor la información necesaria para su
   autenticación en formato cifrado
-  Todos los datos que se envían y se reciben durante la conexión son
   cifrados
-  El cliente puede ejecutar aplicaciones gráficas desde el Shell.

#. 

   #. **Encriptación. Tipos de encriptación.**

La criptografía es una técnica utilizada para convertir un texto claro
en otro, llamado criptograma, cuyo contenido informativo es igual al
anterior pero sólo puede ser decodificado por personas autorizadas.

La criptografía se basa en algoritmos cada vez más sofisticados.

SSH utiliza varios algoritmos de encriptación y autenticación:

-  Para establecer la conexión con la máquina remota emplea algoritmos
   de encriptación asimétrica.
-  Para la transferencia de datos utiliza algoritmos de encriptación
   simétrica, que son más rápidos.

Los tipos de encriptación son:

-  Encriptación simétrica o de clave compartida.
-  Encriptación asimétrica o de clave pública/privada.

*Clave. Una clave es número codificado y encriptado en un archivo que
sirve para encriptar/desencriptar los mensajes transmitidos/enviados*

#. 

   #. 

      #. **Encriptación simétrica o de clave compartida**

Esta técnica se basa en la utilización de una clave que es conocida
tanto por el emisor como por el receptor o destinatario.

El usuario A y el usuario B conocen la clave K. El mensaje original,
utilizando un algoritmo de encriptación simétrico y la clave K, genera
el mensaje K que es transmitido al usuario B. Este, aplicando la misma
clave y el algoritmo inverso, obtiene el mensaje original.

**Ventaja**: Es muy eficiente ya que los algoritmos utilizados son muy
rápidos.

**Desventaja**: ambas partes deben conocer la clave.

#. 

   #. 

      #. **Encriptación asimétrica o de clave pública**

Las técnicas de cifrado asimétrico se basan en el uso de dos claves: una
pública y otra privada.

Según esta técnica cada usuario tiene dos claves. La clave privada sólo
la conoce el dueño de la clave y no se publica. La clave pública es
conocida por otros usuarios en otras máquinas, es decir se publica.
Estas claves se generan al mismo tiempo dando lugar a pares biunívocos,
de tal forma que la combinación pública-privada es única.

La información que recibe un usuario será segura mientras él controle
sus claves privadas. El usuario puede cambiar su clave privada en
cualquier momento y puede publicar su clave pública asociada para
sustituir la clave pública obsoleta.

**Ventaja:** La clave privada no se transmite

**Desventaja**: No utiliza algoritmos eficientes, ya que no son rápidos
cifrando y descifrando.

#. 

   #. 

      #. 
      #. **Algoritmos de clave pública**

El algoritmo RSA:

-  Es el algoritmo de cifrado de clave pública más utilizado
-  Puede utilizarse tanto para encriptar como para firmar documentos

El algoritmo DSA:

-  Puede utilizarse tanto para encriptar como para firmar documentos
-  Mayor grado de seguridad que RSA.

