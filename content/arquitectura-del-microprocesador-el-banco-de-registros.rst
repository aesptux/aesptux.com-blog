Arquitectura del microprocesador: El banco de registros. (III)
##############################################################
:date: 2009-11-23 11:42
:author: aesptux
:category: Others
:tags: arquitectura, banco, microprocesador, registros
:slug: arquitectura-del-microprocesador-el-banco-de-registros

`Arquitectura del microprocesador: La unidad de control`_ (I)

`Arquitectura del microprocesador: Unidad aritmético-lógica`_ (II)

Arquitectura del microprocesador: El banco de registros (III)

`Arquitectura del microprocesador: Buses (IV)`_

Tradicionalmente el banco de registros se ha divido en dos grupos: los
registros de propósito general y los que tienen una función específica.
Al primer grupo pertenecen aquellos que el programador puede usar
libremente para almacenar temporalmente datos, mientras que los segundos
se utilizan de manera indirecta. Los registros con función específica
más usuales son:

-  **Contador de programa:**\ Contiene la dirección de la memoria donde
   está alojada la siguiente instrucción a ejecutar. Actúa, por tanto,
   como un puntero y, de hecho en algunos microprocesadores se denomina
   puntero de instrucción. Es la unidad de control la que utiliza este
   registro para recuperar las instrucciones del programa, incrementando
   su contenido a medida que se avanza en la ejecución o modificándolo
   cuando se encuentra una instrucción de salto.
-  **Puntero de pila:**\ En ocasiones es necesario guardar temporalmente
   el contador de programa, por ejemplo al saltar a una subrutina o
   cuando el microprocesador debe atender una interrupción externa, con
   la intención de recuperarlo posteriormente. Los primeros
   microprocesadores contaban con una pila interna, en el propio
   circuito integrado, que tenía una capacidad limitada y solía permitir
   5 u 8 niveles como máximo. Actualmente la pila se almacena en memoria
   principal, externa al microprocesador de forma que éste lo único que
   necesita es conocer la dirección donde está el tope o parte alta de
   la pila. Almacenar dicha dirección es el objetivo del registro del
   puntero de pila.
-  **Acumulador:**\ Puede ser utilizado como registro de propósito
   general en muchas situaciones, pero en otras adquiere el papel de
   registro específico al ser el destinatario de diferentes operaciones
   aritméticas, lógicas o de entrada/salida.
-  **Estado:**\ Su denominación cambia según el tipo de diseño y
   fabricante, pero su finalidad es siempre la misma: mantener una serie
   de bits indicando el estado en que se encuentra el microprocesador.
   Ese estado proviene normalmente de la ejecución de la última
   instrucción, pudiendo influir en cómo se ejecutarían las posteriores.
   También es posible que ciertos bits modifiquen el modo de
   funcionamiento del procesador, de forma general o ante determinadas
   instrucciones.
-  **Otros registros:**\ Si bien los cuatro citados pueden considerarse
   los más importantes, todos los microprocesadores disponen además de
   otros registros de uso específico, ocultos en su mayor parte que
   emplean para almacenar el código de la instrucción que está
   ejecutándose, contener temporalmente datos procedentes de memoria que
   van a intervenir en un cálculo, etc.

En un principio los microprocesadores contaban sólo con registros de 8 o
16 bits pensados para operar con aritmética entera, pero en la
actualidad el tamaño ha crecido hasta los 32, 64 e incluso 80 bits,
contemplándose tanto la aritmética entera como la de punto flotante.

.. _`Arquitectura del microprocesador: La unidad de control`: http://mortuux.wordpress.com/2009/11/16/arquitectura-microprocesador-la-unidad-de-control/
.. _`Arquitectura del microprocesador: Unidad aritmético-lógica`: http://mortuux.wordpress.com/2009/11/18/arquitectura-del-microprocesador-unidad-aritmetico-logica/
.. _`Arquitectura del microprocesador: Buses (IV)`: http://mortuux.wordpress.com/2009/12/16/arquitectura-del-microprocesador-buses-iv/
