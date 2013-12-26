Arquitectura del microprocesador: Unidad aritmético-lógica (II)
###############################################################
:date: 2009-11-18 10:37
:author: aesptux
:category: Others
:tags: alu, aritmético, arquitectura, lógica, microprocesador, unidad
:slug: arquitectura-del-microprocesador-unidad-aritmetico-logica

`Arquitectura del microprocesador: La unidad de control`_ (I)

Arquitectura del microprocesador: Unidad aritmético-lógica (II)

`Arquitectura del microprocesador: El banco de registros`_ (III)

`Arquitectura del microprocesador: Buses (IV)`_

Conocida también como ALU (Arithmetic Logic Unit), podría decirse que es
la calculadora interna del microprocesador, con capacidad para realizar
operaciones aritméticas pero también de tipo lógico.

Las operaciones aritmético-lógicas que puede ejecutar por sí mismo un
procesador dependerán del diseño de la ALU. Los x86 hasta el 80386, por
ejemplo, contaban con una ALU que ofrecía únicamente operaciones con
aritmética entera y solamente se contemplaban las cuatro operaciones
aritméticas básicas. Las aplicaciones que requerían trabajar con coma
flotante, y realizar operaciones más complejas, tenían que hacerlo por
software, lo cual era lento, o bien requerir que el sistema contase con
un coprocesador matemático.

En la actualidad los microprocesadores disponen de una ALU preparada
para operara con aritmética entera y de punto flotante, ejecutando por
hardware operaciones complejas que, de ser implementadas mediante
software, requerirían mucho más tiempo.

La ALU cuenta con dos entradas, asumiéndose que una de ellas siempre es
el acumulador y que la otra, procedente de cualquier otro registro o e
la memoria, está en un registro temporal. La única salida, en la parte
superior, se dirige al acumulador. En el funcionamiento de la ALU
también interviene el contenido del registro de estado, si bien éste no
actúa como un tercer operando sino como un agente externo que puede
influir en la operación que realice la ALU. Dicha operación vendrá
dictada por la unidad de control que, a través del bus interno, controla
también el funcionamiento de la ALU.

.. _`Arquitectura del microprocesador: La unidad de control`: http://mortuux.wordpress.com/2009/11/16/arquitectura-microprocesador-la-unidad-de-control/
.. _`Arquitectura del microprocesador: El banco de registros`: http://mortuux.wordpress.com/2009/11/23/arquitectura-del-microprocesador-el-banco-de-registros/
.. _`Arquitectura del microprocesador: Buses (IV)`: http://mortuux.wordpress.com/2009/12/16/arquitectura-del-microprocesador-buses-iv/
