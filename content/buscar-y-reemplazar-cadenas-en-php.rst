Buscar y reemplazar cadenas en php
##################################
:date: 2009-07-11 18:53
:author: aesptux
:category: Php, Programming
:tags: buscar, cadenas, php, reemplazar
:slug: buscar-y-reemplazar-cadenas-en-php

Esta tarea normalmente se realiza a través de la función
strpos(cadena\_donde\_se\_busca,subcadena\_a\_buscar) que devuelve false
si no encuentra nada, o devuelve la posión del primer carácter buscado
dentro de la cadena.

`` $cadena = "Hola que tal estoy probando las cadenas" $pos = strpos($cadena, "estoy"); if (!$pos) echo "No se ha encontrado nadan"); else echo "Posición: $posn");``

Eso devolvería el valor 13.

También se puede indicar que empiece a buscar desde la derecha, para
ello existe la función strrpos(). Como ya esperabas, strpos() es
sensible a las mayúscualas y minúsculas, pero curiosamente no hay otra
alternativa para esta función. Pero en php existe la función strstr()
que funciona de manera similar a strpos() y tiene una variante sin
sensibilidad a mayúsculas denominada stristr(). La diferencia entre
strstr() y strpos(), es que strstr() devuelve la parte posterior de la
subcadena buscada. En el ejemplo anterior, strpos() devolvía 13, pues
bien, utilizando la función strstr():

`` $cadena = "Hola que tal estoy probando las cadenas" $pos = strstr($cadena, "estoy"); if (!$pos) echo "No se ha encontrado nadan"); else echo "Posición: $posn");``
 Eso devolvería "estoy probando las cadenas"

Para reemplazar cadenas existen dos funcionaes. Una de ellas es
substr\_replace, que podrá ser utilizada siempre que conozcamos la
posición y la longitud de la sub cadena a reemplazar.

`` $cadena = "Hola que tal estoy probando las cadenas"; $nueva = substr_replace($cadena, "estoy", 13, 5); echo "$nuevan";``

Pero no tenemos porque conocer la longitud ni la posición, para estos
casos tenemos la función str\_replace(subcadena\_buscada,
subcadena\_nueva, cadena)

`` $cadena = "Hola que tal estoy probando las cadenas"; $nueva = str_replace("probando", "quemando", $cadena); echo "$nuevan";``
