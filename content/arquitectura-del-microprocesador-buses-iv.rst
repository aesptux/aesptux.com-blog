Arquitectura del microprocesador: Buses (IV)
############################################
:date: 2009-12-16 14:38
:author: aesptux
:category: Others
:tags: arquitectura, buses, microprocesador
:slug: arquitectura-del-microprocesador-buses-iv

`Arquitectura del microprocesador: La unidad de control`_ (I)

`Arquitectura del microprocesador: Unidad aritmético-lógica`_ (II)

`Arquitectura del microprocesador: El banco de registros (III)`_

Arquitectura del microprocesador: Buses (IV)

Para construir un sistema informático, ya sea un ordenador o cualquier
otro tipo de equipo, además del microprocesador se precisan otros
elementos de apoyo que faciliten el almacenamiento temporal de la
información y la comunicación con el exterior.

El bus de datos está formado por una serie de líneas, físicamente salen
del microprocesador en forma de patillas/pines que se conectan sobre un
zócalo en una laca de circuito impreso, por las que se transmiten en
paralelo un número determinado de bits, tantos como líneas existan. Al
número de esas líneas a lo que se denomina ancho del bus que, por regla
general, coincide con la capacidad del acumulador y una parte de los
registros de propósito general. El bus de datos es bidireccional, de
forma que permite tanto enviar datos desde el microprocesador hacia el
exterior como a la inversa.

Mediante el bus de direcciones el microprocesador selecciona la posición
de memoria en la que va a escribirse o de la que se quiere leer. También
sirve para seleccionar dispositivos de E/S en caso de que éstos tengan
asociado un espacio de entrada/salida en la memoria. A diferencia del
bus de datos, el de direcciones es unidireccional. El número de líneas
que lo forman determina el ancho del bus de direcciones que, a su vez,
fijará el número máximo de direcciones que es posible componer y, en
consecuencia, el límite de memoria al que puede accederse de manera
directa.

Tanto el bus de datos como el de direcciones tienen una estructura
homogénea, en el sentido de que sus líneas contribuyen por igual, con un
bit, a generar el dato o la dirección que va a transferirse ocupando el
bus completo. El bus de control, por el contrario, es heterogéneo y las
líneas que lo forman tienen cada una un fin distinto, por lo que
raramente se utilizan de manera simultánea. Algunas de dichas lineas son
solamente de salida, otras únicamente de entrada y en raras ocasiones de
entrada/salida.

A través de las líneas del bus de control el microprocesador comunicará
al sistema si la dirección que está colocando en el bus de direcciones
ha de ser enviada a la memoria o a un dispositivo de E/S o si lo que se
quiere es efectuar una lectura o escritura.

Los dispositivos externos emplearán una cierta línea de este bus para
comunicar al microprocesador que necesitan su atención, provocando una
interrupción que, por ejemplo, recoja la última pulsación del teclado.

.. _`Arquitectura del microprocesador: La unidad de control`: http://mortuux.wordpress.com/2009/11/16/arquitectura-microprocesador-la-unidad-de-control/
.. _`Arquitectura del microprocesador: Unidad aritmético-lógica`: http://mortuux.wordpress.com/2009/11/18/arquitectura-del-microprocesador-unidad-aritmetico-logica/
.. _`Arquitectura del microprocesador: El banco de registros (III)`: http://mortuux.wordpress.com/2009/11/23/arquitectura-del-microprocesador-el-banco-de-registros/
