Detección de hardware en Linux.
###############################
:date: 2010-02-03 12:33
:author: aesptux
:category: Linux
:tags: deteccion, hardware, Linux
:slug: deteccion-de-hardware-en-linux

Queremos saber que componentes hay instalados dentro de un ordenador:

Para un resumen de todos los dispositivos pci conectados:

    lspci

La anterior orden lo más seguro es que se nos quede corta, para saber
más podemos utilizar

    dmesg

Para su mejor lectura, podemos combinarlo con less con una pipe

    dmesg \| less

Para hacer filtros utilizaremos grep:

Lista dispositivos USB:

    dmesg \| grep -i usb

Saber cuanta memoria física hay:

    dmesg \| grep -i memory

Información sobre los SATA:

    dmesg \| grep -i sata

Puertos serie:

    dmesg  \| grep -i tty

Listar procesador/es

    dmesg \| grep -i cpu

También podemos obtener instantáneas con /proc

Para explorar /proc, utilizaremos la orden *cat*

Para ver información de la cpu:

    cat /proc/cpuinfo

Para ver la memoría física y swap:

    cat /proc/meminfo
