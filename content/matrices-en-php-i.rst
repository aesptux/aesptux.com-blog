Matrices en Php (I)
###################
:date: 2009-09-08 12:25
:author: aesptux
:category: Php, Programming
:tags: matrices, php, sintaxis
:slug: matrices-en-php-i

En PHP, podemos crear una variable de matriz de varias formas. La más
sencilla:
 ``$variable[expr clave] = expr;``

*Expr clave*\ es una expresión que se evalúa para una cadena o cualquier
entero no negativo y *expr* representa la expresión cuyo valor se
asociará con la clave.
 ``$var['a'] = 1; $var['b'] = 2; $var['c'] = 3; $var['d'] = 4;``

Si *expr clave* no se especifica, PHP utilizará **automáticamente el
siguiente entero disponible** como clave.

Cuando definamos una matriz dentro de una secuencia de comandos
manualmente, utilizar esta sintaxis puede ser difícil. En estos casos es
mejor utilizar la sintaxis formal para las matrices; la sentencia
array(). La sintaxis general es la siguiente:
 ``$variable = array([mixto]);``

En la sintaxis anterior, *mixto*\ representa los distintos pares de
claves/valores definidos en este formato:
 `` expr clave => expr valor; expr clave => expr valor;``

Por ejemplo:
 ``$hola = array('a' => 1, 'b' => 2, 'c' => 3);``
 Es lo mismo que:
 ``$hola['a'] = 1; $hola['b'] = 2; $hola['c'] = 3;``

Matriz que asigna claves del 1 al 12 a los meses del año:

``$meses = array(1=>"Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre");``
