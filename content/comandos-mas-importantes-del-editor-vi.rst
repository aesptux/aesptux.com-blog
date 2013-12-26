Comandos más importantes del editor vi
######################################
:date: 2009-04-16 23:39
:author: aesptux
:category: Linux
:tags: comandos, editor, Linux, vi
:slug: comandos-mas-importantes-del-editor-vi

¿Qué es vi?

vi es un simple procesador de texto, no formatea texto. Es un procesador
incluido es sistemas basados en Unix.

Comandos más importantes:
 dd -> Para borrar una línea entera. También podemos borrar un numero x
de líneas, con el comando xdd, por ejemplo para borrar 6 líneas: 6dd

i - > Inserta texto antes de la posición del cursor. Ejemplo: El cursor
estará representado con negrita,y vamos a escribir una Q: hola -> holqa

a -> Inserta texto después de la posición del cursor. Siguiendo con el
ejemplo anterior: hola -> holaq

I -> Inserta texto al principio de la línea en la que está el cursor.

A -> Inserta texto al final de la línea en la que está el cursor.

#G -> Ir al número de línea indicado. Por ejemplo, 10G, irá a la línea
10. Para ir al final, sería con $ -> $G

x -> Borra el carácter sobre el que está situado el cursor

yy -> Copiar línea actual

p -> Pegar detrás del cursor

P -> Pegar delante del cursor

u -> Deshacer último comando

:r archivo -> Inserta el archivo indicado detrás del cursor

:w -> Guardar Archivo

:q -> Salir ( Si no hay cambios )

:q! -> Salir sin guardar cambios

:wq -> Guardar y salir

Eso es todo.

Un saludo,

Mortuus.
