Arquitectura microprocesador: La unidad de control (I)
######################################################
:date: 2009-11-16 17:17
:author: aesptux
:category: Others
:tags: arquitectura, control, microprocesador, unidad
:slug: arquitectura-microprocesador-la-unidad-de-control

.. raw:: html

   <div id="_mcePaste">

[caption id="attachment\_271" align="aligncenter" width="300"
caption="Arquitectura Microprocesador"]\ `|arquitectura
microprocesador|`_\ [/caption]

Arquitectura del microprocesador: La unidad de control (I)

`Arquitectura del microprocesador: Unidad aritmético-lógica`_ (II)

`Arquitectura del microprocesador: El banco de registros`_ (III)

`Arquitectura del microprocesador: Buses (IV)`_

.. raw:: html

   </div>

.. raw:: html

   <div>

Un microprocesador es un circuito integrado formado por millones de
componentes lógicos que es necesario coordinar para que cada uno realice
su trabajo en el momento que se espera, tarea que recae fundamentalmente
en la conocida CU (Control Unit) o unidad de control.

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste">

Es tarea de la CU emitir las señales necesarias para que la siguiente
instrucción de un programa, cuya localización  en memoria indica un
registro específico al que suele llamarse "contador de programa" o
"puntero de instrucción", sea transferida hasta el interior del
microprocesador (fase de captación). A continuación esa instrucción se
analiza y se preparan los operandos que precise (fase de
descodificación) para a continuación ejecutarla (fase de ejecución) y
generar los resultados que correspondan (fases de escritura en memoria y
registros).

.. raw:: html

   </div>

.. raw:: html

   <div id="_mcePaste">

A través de un bus interno la unidad de control se comnica con el resto
de elementos del microprocesador, estableciendo por ejemplo los
registros que han de utilizarse como operandos en un cálculo o fijando
la operación que debe llevar acabo la ALU sobre dichos operandos.

.. raw:: html

   </div>

.. raw:: html

   <div>

Un microprocesador es un circuito integrado formado por millones de
componentes lógicos que es necesario coordinar para que cada uno realice
su trabajo en el momento que se espera, tarea que recae fundamentalmente
en la conocida CU (Control Unit)o unidad de control.Es tarea de la CU
emitir las señales necesarias para que la siguiente instrucción de un
programa, cuya localización  en memoria indica un registro específico al
que suele llamarse "contador de programa" o "puntero de instrucción",
sea transferida hasta el interior del microprocesador (fase de
captación). A continuación esa instrucción se analiza y se preparan los
operandos que precise (fase de descodificación) para a continuación
ejecutarla (fase de ejecución) y generar los resultados que correspondan
(fases de escritura en memoria y registros).A través de un bus interno
la unidad de control se comnica con el resto de elementos del
microprocesador, estableciendo por ejemplo los registros que han de
utilizarse como operandos en un cálculo o fijando la operación que debe
llevar acabo la ALU sobre dichos operandos.

.. raw:: html

   </div>

.. _|image1|: http://mortuux.files.wordpress.com/2009/11/arquitectura-microprocesador.png
.. _`Arquitectura del microprocesador: Unidad aritmético-lógica`: http://mortuux.wordpress.com/2009/11/18/arquitectura-del-microprocesador-unidad-aritmetico-logica/
.. _`Arquitectura del microprocesador: El banco de registros`: http://mortuux.wordpress.com/2009/11/23/arquitectura-del-microprocesador-el-banco-de-registros/
.. _`Arquitectura del microprocesador: Buses (IV)`: http://mortuux.wordpress.com/2009/12/16/arquitectura-del-microprocesador-buses-iv/

.. |arquitectura
microprocesador| image:: http://mortuux.files.wordpress.com/2009/11/arquitectura-microprocesador.png?w=300
.. |image1| image:: http://mortuux.files.wordpress.com/2009/11/arquitectura-microprocesador.png?w=300
