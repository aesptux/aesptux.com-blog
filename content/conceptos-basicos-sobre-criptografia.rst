Conceptos básicos sobre criptografía
####################################
:date: 2009-08-09 23:42
:author: aesptux
:category: Others
:tags: basica, criptografia
:slug: conceptos-basicos-sobre-criptografia

Según el Diccionario de la Real Academia, la palabra criptografía
significa: *"Arte de escribir con clave secreta o de un modo
enigmático".*

Existen dos documentos fundamentales, uno escrito por Claude Shannon en
1948 ("*A Mathematical Theory of Communication*\ "), en el que se
sentaban las bases de la Teoría de la Información, y que junto con otro
artículo posterior del mismo autor, sirvió de base para la criptografía
moderna. El otro trabajo, publicado por Whitfield Diffie en 1975,
introducía el concepto de criptografía de llave pública, abriendo
enormemente el abanico de aplicación de esta disciplina.

**Criptosistema**

Definiremos criptosistema como una quíntupla (M, C, K, E, D), donde:

-  **M**\ representa el conjunto de todos los mensajes sin cifrar que
   pueden ser enviados.
-  **C**\ representa el conjunto de todos  los posibles mensajes
   cifrados , o criptogramas.
-  **K**\ representa el conjunto de claves que se pueden emplear en el
   criptosistema.
-  **E**\ es el conjunto de transformaciones de cifrado  o familia de
   funciones que se aplica a cada elemento M para obtener un elemento de
   C. Existe una transformación diferente E\ :sub:`k` para cada valor
   posible de la k
-  **D** es el conjunto de transformaciones de descifrado, análogo a E.

Todo criptosistema ha de cumplir la siguiente condición:

**D\ :sub:`k`\ (E:sub:`k`\ (m)) = m**

Es decir, si tenemos un mensaje m, lo ciframos empleando la clave k y
luego lo desciframos empleando la misma clave, obtenemos de nuevo el
mensaje original m.

Existen dos tipos fundamentales de criptosistemas:

-  **Criptosistemas simétricos o de clave privada.**\ Son aquellos que
   emplean la misma clave k tanto para cifrar como para descifrar.
   Presentan el inconveniente de que para ser  empleados en canales de
   transmisión la clave k debe estar tanto en el emisor como en el
   receptor, lo cual nos lleva a como transmitir la clave de forma
   segura.
-  **Criptosistemas asimétricos o de clave pública,**\ que emplean una
   doble clave (K:sub:`p`,K\ :sub:`p1`) siendo la primera la clave
   privada y la segunda la clave pública. Una de ellas sirve para la
   transformación E de cifrado y la otra para la transformación D de
   descifrado. Estos criptosistemas deben cumplir además que el
   conocimiento de la clave pública no permita calcular la clave
   privada.

