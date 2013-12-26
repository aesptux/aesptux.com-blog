Bases de datos relacionales.
############################
:date: 2010-11-08 12:30
:author: aesptux
:category: Databases, Notes
:tags: abstraccion, apuntes, bases de datos, datos, lenguajes, objetivos, procedimientos almacenados, relacionales, Security, sql, teoria, triggers
:slug: bases-de-datos-relacionales

?

#. \ **Bases de datos relacionales**\ 

   \ **Objetivos y ventajas del modelo relacional**

El principal objetivo del modelo relacional es traducir el modelo de
negocio (realidad) para que el modelo de base de datos sea lo más
parecido posible.

**Abstracción del almacenamiento físico**

Separación entre el nivel de almacenamiento físico y el nivel conceptual

Utilizando bases de datos relacionales, el depósito de información es
compacto, está gestionado de forma transparente. Todas las entidades
residen en mismo depósito de información.

**Relaciones reflexivas y recursividad**

Permite relaciones reflexivas.

Una entidad puede relacionarse consigo misma, lo cual nos lleva pensar
en esquemas recursivos.

**Abstracción de tablas y vistas**

Podemos tener entidades almacenadas en tablas (filas y columnas) y
también podemos componer vistas empleando los contenidos de diferentes
tablas.

**Relaciones y reglas de integridad referencial**

Son las líneas que vinculan unas entidades con otras.

Las reglas de integridad referencial se generan a partir de relaciones
entre tablas.

Dependiendo de si el campo es clave en origen o en destino podemos tener
relaciones fuertes o débiles. Las relaciones fuertes implican reglas de
integridad referencial.

Las reglas de integridad referencial sirven para exigir coherencia entre
los datos.

**Relaciones fuertes y relaciones débiles. Cardinalidad.**

Hay varios tipos de relaciones, pueden ser 1 a N o N a M.

Si la relación es NM, se debe crear una tabla de cruce con los campos
clave de ambas tablas

Relación fuerte: Porque se trata de una relación de uno a muchos. El
hecho de que exista un sello implica que debe estar guardado en un
álbum.

**Procedimientos almacenados y disparadores (triggers)**

Los procedimientos almacenados son funciones y métodos que amplían las
posibilidades de manejo de la base de datos.

Estos procedimientos constituyen una capa de programación intermedia muy
cercana a la base de datos.

Ejemplos de tareas:

Dar de alta entidades. Una empresa tiene como norma que un cliente nunca
pueda darse de alta si no se le ha realizado un análisis de riesgo de
cobro. El procedimiento de alta de un cliente verificará que el valor de
la columna Riesgo no sea nulo.

Distribuir datos lógicos a lo largo de diferentes tablas físicas sin que
externamente se modifique nada.

Obtener datos de hardware o controlar dispositivos externos.

 

Los disparadores o triggers son procedimientos almacenados que se ponen
en marcha automáticamente cuando sucede un acontecimiento previsto. Por
ejemplo, la inserción de un nuevo registro sobre una tabla.

Más ejemplos:

Llamar a los técnicos de control cuando se ha insertado un registro en
la tabla de incidencias de maquinaria

Para enviar un mensaje de correo electrónico a un cliente cuando su
mercancía está lista para salir de almacén

**Transacciones**

Una transacción es un bloque diferenciado de operaciones de escritura
sobre una o más tablas, cuyo resultado puede ser confirmado o revocado
en su totalidad.

La inserción de una factura implica a su vez la inserción de una
cabecera de factura y de unas líneas de factura.

Imaginemos que intentan entrar una línea de factura con una cantidad 0
de unidades o que estamos trabajando con albaranes/factura y las
unidades facturadas superan las unidades que tenemos en stock para
entregar.

Lo que sucede en este caso es que se revoca la escritura de la cabecera,
de las líneas anteriormente grabadas de esa factura y se retorna al
estado anterior.

Debe respetar las condiciones ACID.

-  \ **A de atomización**\ : la palabra átomo quiere decir indivisible.
   Una factura es una entidad lógica indivisible, por ejemplo.
-  \ **C de consistencia**\ : se garantiza que sólo se realizará el
   bloque si no se rompe ninguna regla de integridad referencial ni
   ninguna regla de negocio explícitamente guardada en la base de datos.
-  \ **I de Isolation**\ : una operación no puede afectar a otras. Dos
   transacciones sobre la misma información son independientes y no
   generan errores.
-  \ **D de durabilidad**\ : una vez que la transacción se ha
   confirmado, se mantiene en disco completamente grabada aunque haya un
   fallo de sistema

   .. raw:: html

      <p>

   **Seguridad**

Pueden establecer normas de seguridad para proporcionar acceso de
lectura, escritura, inserción y borrado de sus usuarios, así como
establecer seguridad también sobre los derechos de administración, como
por ejemplo creación y destrucción de tablas.

En programación orientada a objetos, una tabla equivale a una entidad o
un tipo de objeto: una clase. La seguridad es a nivel de tipos, y no de
registro.

Existe una segunda forma de seguridad que no está implementada en las
bases de datos relacionales que es la seguridad a nivel de instancias;
la seguridad a nivel de filas individuales de las tablas.

**Lenguajes propias para la gestión de datos y recursos**

Lenguaje unificado. Se trata del lenguaje SQL del cual han surgido
variaciones y dialectos propias de cada fabricante:

-  \ **DDL (Data Definition Language):**\  Lenguaje de definición de
   estructuras de datos. Permite crear tablas, modificarlas y
   eliminarlas
-  \ **DML (Data Management Language):**\  Lenguaje de manipulación de
   datos. Permite dar de alta filas, modificar contenido de columnas y
   borrar filas y columnas
-  \ **DCL (Data Control Language):**\  Lenguaje de control de datos.
   Permite administrar la seguridad de quién puede leer, escribir o
   borrar datos en una tabla; quién puede crear o eliminar tablas, etc.

 
