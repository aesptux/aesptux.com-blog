Operadores en PHP.
##################
:date: 2011-07-11 12:24
:author: aesptux
:category: Php, Programming
:tags: and, aritméticos, asignación, cadenas, concatenación, división, igual, logico, mayor, menos, módulo, multiplicación, not, operadores, or, php, referencia, resta, strings, suma
:slug: operadores-en-php

**Operadores aritméticos**

::

    // Suma
    $a + $b;

    // Resta
    $a - $b;

    // Multiplicación
    $a * $b;

    // División
    $a / $b;

    // Módulo
    $a % $b;

    // Sumar y asignar
    // Para sumar $b al valor actual de $a, hariamos
    $a = $a + $b;
    // Pues con este operador podría hacerse así
    $a += $b;

    // Restar y asignar
    $a -= $b;

    //Multiplicar y asignar
    $a *= $b;

    //Dividir y asignar
    $a /= $b;

\ ****Operadores de asignación**
**\ 

::

    // Asignación
    // Asigna el valor de una variable a otra
    $a = $b;

    // Referencia
    // Una referencia es como un enlace
    $a =& $b;

**Operadores de cadenas**

::

    // Concatenación
    // Concatena la segunda variable a la primera
    $a = "Hola ";
    $b = "Mundo";
    $c = $a . $b;
    //la salida de $c será "Hola Mundo"

    // Concatenar y asignar
    // Lo mismo que los operadores aritméticos
    $d = "Adrian";
    $a .= $d;
    // Ahora, el valor de $a es "Hola Adrian"

**Operadores de comparación**

::

    // Es igual
    $a == $b;

    // Identico
    // Son iguales y además son del mismo tipo
    $a === $b;

    // No son iguales
    $a != $b;
    $a <> $b;

    // No son identicos
    // No son iguales y no son del mismo tipo
    $a !== $b;

    // Menor que
    $a < $b;

    // Mayor que
    $a > $b;

    // Menor o igual que
    $a <= $b;

    // Mayor o igual que
    $a >= $b;

**Operadores de incremento y decremento**

::

    // Pre-incremento
    // Incrementa en uno, y devuelve el valor
    ++$a;

    // Post-incremento
    // Devuelve el valor, e incrementa en uno
    $a++;

    // Pre-decremento
    // Decrementa en uno, y devuelve el valor
    --$a;

    // Post-decremento
    // Devuelve el valor, y decrementa en uno
    $a--;

**Operadores lógicos**

::

    // AND lógico
    $a && $b;
    $a AND $b;

    // OR lógico
    $a || $b;
    $a OR $b;

    // NOT lógico
    !$a;

 
