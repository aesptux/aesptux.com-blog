Matrices en Php (II)
####################
:date: 2009-09-09 10:19
:author: aesptux
:category: Php, Programming
:tags: matrices, php, recorrer
:slug: matrices-en-php-ii

Recorrido por las matrices

El método apropiado para recorrer una matriz es utilizar la sentencia
foreach(), cuya sintaxis es la siguiente:
 ``foreach(matriz as $clave => $valor) { ... ... ... }``

El parámetro matriz representa la matriz por la que realizaremos el
recorrido y $clave/$valor representan respectivamente el par individual
clave/valor por el que pasamos.
 ``$matriz = array('el', 'coche', 'es', 'azul');``

``/* Obtener tanto  la clave como el valor */ foreach($matriz as $clave => $valor) { echo "El valor de $clave es: $valor"; }``

``/*Obtener solamente el valor */ foreach($matriz as $valor) { echo "El valor es: $valor"; }``

`` ``
