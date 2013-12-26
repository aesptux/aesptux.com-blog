Declaración de variables en JavaScript
######################################
:date: 2009-09-01 11:09
:author: aesptux
:category: JavaScript, Programming
:tags: declaración, JavaScript, variables
:slug: declaracion-de-variables-en-javascript

Para utilizar una variable en nuestro código debe estar indicado en
alguna parte de éste cuál es su nombre y/o valor. A esto se le conoce
como declarar una variable.

En la mayoría de los lenguajes de programación es obligatorio declarar
cada variable antes de utilizarla en el código mientras que en
JavaScript se puede hacer sobre la marcha según las vayamos necesitando.
Hay dos maneras de declarar variables:

#. Declaración explícita: Consiste en usar la sentencia *var*\ seguida
   del nombre de la variable. Esta opción es la más recomendada, para
   que el código sea más legible, personalmente la recomiendo.
#. Declaración implícita: Es cuando escribimos directamente el nombre de
   la variable. En este caso debe ir acompañada obligatoriamente de un
   valor.

`` // declaración explícita var nombre; // declaración implícita nombre = "Paco"; // declaración explícita múltiple var nombre, edad, apellido; // declaración explícita múltiple con inicialización var nombre = "paco", edad = 20, apellido = "ruiz"; // declaración implícita múltiple con inicialización nombre = "paco", edad = 20, apellido = "ruiz";``

También se pueden declarar constantes, por ejemplo el numero pi, o un
valor máximo. Se declaran con la sentencia *const.*\ Pero es
recomendable no usarlo porque sólo es soportado a partir del motor 1.5
de JavaScript.
