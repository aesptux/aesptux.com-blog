Expresiones regulares en JavaScript
###################################
:date: 2009-09-03 17:00
:author: aesptux
:category: JavaScript, Programming
:tags: expresiones, JavaScript, regulares
:slug: expresiones-regulares-en-javascript

Una expresión regular es una cadena de caracteres que nos permitirá
buscar coincidencias dentro de un texto o comprobar que una cadena tiene
un formato concreto. En JavaScript se identifican colocando *"/"*\ al
principio y al final de la cadena.

Consiste en escribir un conjunto de caracteres  para después encontrar
coincidencias con él. Por ejemplo en la frase *"el volante del coche"*
si nuestro patrón es */el/*\ obtendríamos que las palabras "el y "del"
lo cumplen.

Para hacer más útiles los patrones, hay una serie de estructuras y
caracteres especiales:

**Caracteres de repetición**

-  **Asterisco(\*):**\ El caracter que le precede aparecerá cero o más
   veces.
-  **Más(+):**\ El caracter que le precede aparecerá una o más veces.
-  **Interrogación(?):**\ Igual que las opciones anteriores, pero el
   caracter puede aparecer ninguna o una vez.
-  **{n}:**\ Siendo **n** un número entero positivo, indicamos que el
   caracter se debe repetir al menos n veces.
-  **{n,}:**\ Similar al anterior, pero esta vez indicamos que al menos
   se debe repetir n veces.
-  **{n, m}:**\ El caracter debe repetirse entre n y m veces.

**Caracteres especiales**

-  **Punto(.):**\ Coincidirá con cualquier caracter simple excepto el
   salto de línea.
-  **n :**\ Salto de línea.
-  **r :**\ Retorno de carro.
-  **t :**\ Caracter de tabulado.
-  **v :** Tabulado vertical.
-  **f :**\ Avance de página.
-  **uxxxx :**\ Caracter unicode.
-  **b :**\ Coincide con un separador de palabras.
-  **B :**\ Coincide con un caracter que no sea separador de palabras.
-  **d :**\ Dígito entre cero y nueve.
-  **D :**\ Caracter que no sea un dígito.
-  **s :**\ Coincide con un único caracter de separación.
-  **S :**\ Coincide con un único caracter que no sea de separación.
-  **w :**\ Coincide con cualquier caracter alfanumérico (De la "a" a la
   "z" en máyusculas y minúsculas, números del cero al nueve) o el
   subrayado.
-  **W:**\ Coincide con cualquier caracter no alfanumérico ni subrayado.

**Agrupaciones de valores**

-  **[xxx]:**\ Coincide con los caracteres entre corchetes. También se
   puede especificar un rango *contiguo*\ de caracteres: [0-6] que esto
   equivale a [0123456].
-  **[^xxx]:**\ El acento circunflejo indica que coincidirán cualquier
   caracter salvo los especificados en los corchetes.
-  **Barra vertical ( x \| y ):**\ O una cosa o la otra. Por ejemplo:
   /*cara\|cruz/, /perr[o\|a]/*

**Modificadores**

Los modificadores se colocan detras de la última barra, por ejemplo:
*/hola/g*.

-  **g :**\ Fuerza a que se sigan buscando coincidencias después de
   encontrar la primera
-  **i :**\ Elimina distinción entre mayúsculas y minúsculas.
-  **x :**\ Fuerza que los espacios escritos sean ignorados.

**Ejemplos útiles**

#. /d{9}/ -> Número teléfono
#. /d{8}[a-zA-Z]/ -> Número DNI
#. /d{2}-d{2}-d{4} -> Fecha DD/MM/AAAA
#. /w+@w+.w{2,3}/ -> Dirección correo electrónico.

