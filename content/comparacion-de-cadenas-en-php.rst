Comparación de cadenas en php
#############################
:date: 2009-07-08 14:46
:author: aesptux
:category: Programming
:tags: cadenas, comparar, php
:slug: comparacion-de-cadenas-en-php

Comparar cadenas en php no es tan fácil como hacerlo con números. Si
examinamos una cadena basándonos en su forma binaria, "Juan" y "juan"
serán completamente diferentes. El valor de "Juan" en binario es:
*010010100111010101100001011011100000110100001010*\ y para "juan" es:
*01\ **1**\ 010100111010101100001011011100000110100001010*.

La primera función de comparación es strcmp(). El valor devuelto por
esta función depende de la relación alfabética entre las dos cadenas. Si
$val1 y $val2 son idénticas, strcmp() devolverá 0. strcmp() distingue
entre mayúsculas y minúsculas. Si no son igualesm el valor devuelto
estará determinado por las reglas de orden alfabético. Si $val1 es
alfabéticamente inferior a $val2, el resultado será negativo, en caso
contrario, será positivo.
 `` echo strcmp("Alvaro", "Benito"); // Devuelve < 0 ``

``echo strcmp("manzana", "Manzana"); // Devuelve > 0``

Los números tienen un valor contexual más bajo que las letras, y las
letras mayúsculas un valor contextual más bajo que las minúsculas. Si
queremos comparar cadenas sin distinción entre mayúsculas y minúsculas,
debemos usar la función strcasecmp();

``echo strcasecmp("Juan", "juan"); // devuelve 0;``

Aún no existe una solución que se acerque a la capacidad del cerebro
humano, pero se han desarrollado varios algoritmos que nos proporcionan
un método para medir la "similitud" entre dos cadenas. Uno de estos
ejemplos es el algoritmo soundex. Soundex funciona asignando un valor a
cada constante del alfabeto y calculando posteriormente el valor total
de una palabra basándose en sus sílabas iniciales y componentes. En php
se implanta mediante la función soundex();

`` echo soundex("Mortuus"); //Devuelve M632 echo soundex("Mortiis"); // Devuelve M632 echo soundex("Mortem"); // Devuelve M635``

Otro algoritmo para comparar dos palabras basándonos en sus
representaciones fonéticas es el metáfono. Este algoritmo funciona
asignando un valor fonético a combinaciones de caracteres basándose en
su uso típico en inglés. Php lo implanta a través de la función
metaphone();

``echo metaphone("Mortuus"); // Devuelve MRTS echo metaphone("Mortiis"); // Devuelve MRTS echo metaphone("Mortem"); //Devuelve MRTM``
