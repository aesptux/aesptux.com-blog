Buscar comando "sin saber que buscar"
#####################################
:date: 2010-01-11 22:01
:author: aesptux
:category: Linux
:tags: comando, encontrar, Linux, man, paginas
:slug: buscar-comando-sin-saber-que-buscar

Por ejemplo, necesita un programa o una utilidad para llevar a cabo una
cierta tarea, por ejemplo contar las palabras contenidas en un archivo,
pero no sabe qué buscar.

¿Cómo salir de este dilema?

Pues hay dos formas

    apropos count words

    man -k count words

En este caso, las palabras clave a buscar son "count"  y "words".
Saldrán un montón de resultados, pero el más eficiente para este caso es
*wc*.
