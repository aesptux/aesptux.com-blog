Condiciones en PHP.
###################
:date: 2011-07-13 13:03
:author: aesptux
:category: Php, Programming
:tags: case, condiciones, elif, else, if, limpio, operador, ordenado, php, si, si no, switch
:slug: condiciones-en-php

Una condición es básicamente una decisión, resultado de una condición
específica. Por ejemplo:

::

    <?php
        $edad = 16;
        print "Tu edad es $edad\n";
        if ($edad < 18 ) {
            print "Eres joven, disfruta.\n";
        } else {
            print "No eres menor de 18\n";
        }

        if ($edad  >= 18 && $edad < 50) {
            print "Estas en la flor de la vida!\n";
        } else {
            print "No estas en la flor de la vida\n";
        }

        if ($edad >= 50) {
            print "Te queda poco para retirarte\n";
        } else {
            print "No te queda poco para retirarte\n";
        }
    ?>

 Se entiende fácilmente, pero aún así lo explico un poco.

Es una simple condición que evalúa una edad y muestra unos mensajes en
función de la edad.

La condición del medio, lleva el operador lógico AND. Si quieres saber
más sobre los operadores de php, en `esta entrada`_ hablo un poco sobre
ellos.

Si (if) se cumple la condición, ejecuta el primer bloque de
instrucciones, si no se cumple (else) ejecuta el segundo bloque.

También podemos utilizar esta forma:

::

    <?php
        $edad = 23;

        if ($edad < 10) {
            echo "Tienes menos de 10.";
        } elseif ($edad < 20 ) {
            echo "Tienes menos de 20.";
        } elseif ($edad < 30 ) {
            echo "Tienes menos de 30.";
        } elseif ($edad < 40 ) {
            echo "Tienes menos de 40.";
        } elseif ($edad < 40 ) {
            echo "Tienes menos de 40.";
        } else {
            echo "Tienes mas de 40";
        }

    ?>

Con la instrucción **elif**\ nos ahorramos hacer varios bloques.

Sin embargo cuando nos encontramos con que tenemos que trabajar con
numerosos elif, la cosa puede complicarse y podemos liarnos. Para ello
tenemos la instrucción case, los dos siguientes ejemplos, actúan de la
misma manera:

::

    <?php
        $nombre = "Bob";
        if ($nombre == "Bob") {
            echo "Te llamas Bob\n";
        } elseif ($nombre == "Linda") {
            echo "Te llamas Linda\n";
        } elseif ($nombre == "Jim") {
            echo "Te llamas Jim\n";
        } elseif ($nombre == "Sally") {
            echo "Te llamas Sally\n";
        } else {
            echo "No se como te llamas";
        }

    ?>

::

    <?php
        $nombre = "Linda";
        switch($nombre){
            case "Bob":
                echo "Te llamas Bob\n";
                break;
            case "Linda":
                echo "Te llamas Linda\n";
                break;
            case "Jim":
                echo "Te llamas Jim\n";
                break;
            case "Sally":
                echo "Te llamas Sally\n";
                break;
            default:
                echo "No se como te llamas";
        }

    ?>

Como podemos observar, cuando se trata de varios elif, utilizar case
queda más ordenado y es de más fácil lectura.

.. _esta entrada: http://aesptux.com/2011/07/11/operadores-en-php/
