Sistemas de archivos en Linux
#############################
:date: 2011-03-12 13:00
:author: aesptux
:category: Linux
:tags: archivos, fstab, Linux, montaje, opciones, particiones, sistemas
:slug: sistemas-de-archivos-en-linux

Los sistemas de archivos de GNU/Linux se organizan de forma jerárquica,
empezando desde el raíz (/)hacia abajo por una estructura de directorios
y subdirectorios.

Los sistemas de archivos no se organizan de igual forma en Linux que en
Windows. En éste último se utilizan letras de unidad para cada
“partición” en un disco local, en un sistema de archivos de red, cd-rom
u otro medio de almacenamiento. En Linux se “encajan” dentro del sistema
de archivos (son directorios) através de los “puntos de montaje”.

Para acceder a las particiones actualmente configuradas en nuestro
sistema (discos duros exclusivamente) utilizamos el comando fdisk
-l.Para saber que particiones se están utilizando en este momento en
nuestro sistema utilizamos el comando mount . Este comando nos mostrará
tanto las particiones disponibles “montadas” como el lugar donde están
montadas (punto de montaje).

Punto de montaje: este término se refiere al directorio que se asocia
con una partición de disco o concualquier otro dispositivo de
almacenamiento secundario.

 

GNU/Linux trata todos los dispositivos como archivos y tiene archivos
reales que representan cada dispositivo. En Linux estos “archivos de
dispositivo” se localizan en el directorio /dev. En este directorio
podemos encontrar los siguientes “archivos de dispositivo”:

/dev/hda Primera unidad IDE.

/dev/hdb Segunda unidad IDE.

/dev/sda Primera unidad SCSI (también utilizada para pendrive)

/dev/sdb Segunda unidad SCSI

/dev/fd0 Disquetera

/dev/cdrom Unidad de CD-ROM

Las “particiones” se nombran igual que el dispositivo pero seguidas del
número de partición. Así si tuvieramos 3 particiones el el segundo disco
IDE estas se nombrarían:

/dev/hdb1

/dev/hdb2

/dev/hdb3

 

Un sistema de archivos es una forma de escribir los datos en el disco
físico.Los ficheros, en casi todos los sistemas de archivos Linux, son
sensibles a mayúsculas, es decir, fichero.txt no es Fichero.txt.

En Linux, cuando el sistema operativo entra a operar en modo kernel para
resolver un acceso a discotrabaja con una capa intermedia de abstracción
de sistema de ficheros que se denomina VFS (Virtual FileSystem). Cada
sistema de archivos conoce cómo convertir una orden para VFS en algo que
sea implementable en él. Esto permite a Linux trabajar con una cantidad
realmente alta de sistemas de ficheros distintos de forma consistente y
homogénea.

**fichero /etc/fstab**

Nos permite definir las particiones que se “montan” en el inicio de
sistema, o las que son posible su montaje por parte de usuarios que no
sean root. Cualquier dispositivo que no se encuentre en este fichero
sólo podrá ser montado por el usuario root. Es un fichero con formato
texto (podemos modificarlo con el editor vi) y la siguiente estructura:

1ª columna: Nombre del dispositivo o partición a montar.

2ª columna: punto de montaje.

3ª columna: sistema de archivos

.4ª columna: opciones de montaje

:rw: lectura y escritura

ro: sólo lectura

sw: partición swap

noexec: impide la ejecución

auto: se montará al inicio del sistema

noauto: no se montará en el inicio del sistema

user: permitirá a un usuario normal montar o desmontar el dispositivo en
el punto de montaje indicado en la columna 2.

uid o gid: el usuario o grupo que tendrán control sobre los archivos.

5ª columna: por defecto a 0, tiene relación con los errores producidos
en el arranque del montaje.

6ª columna: el número de este campo indica si el sistema de archivos
necesita ser comprobado.

 

 
