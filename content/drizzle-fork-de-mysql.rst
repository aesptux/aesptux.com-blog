Drizzle. Fork de MySQL
######################
:date: 2011-03-21 13:00
:author: aesptux
:category: Databases, Drizzle, MySQL
:tags: con, datos, diferencias, drizzle, eliminadas, estable, fork, funciones, mysql, objetos, primera, tipos, version
:slug: drizzle-fork-de-mysql

Como bien indica el título Drizzle es un fork de MySQL, concretamente de
la versión 6.0.

Desde entonces ha habido muchos cambios, como los siguientes:

Uso
===

-  No hay un servidor embebido. El servidor Drizzle no se puede cargar
   como librería compartida
-  Drizzle está optimizado para entornos concurrentes masivos
-  Diseñado para sistemas POSIX modernos
-  Windows, HP-UX e IRIX no son soportados
-  Drizzle no utiliza timezones. Todo es UTC

Instalación
===========

-  No hay scripts/mysql\_install\_db o similar. Drizzle se basa en una
   instalación conocida como "just works" (simplemente funciona)
-  Drizzle puede escuchar en el puerto Drizzle (4427) y/o en el puerto
   MySQL (3306) y entender los respectivos protocolos

Procedimientos Almacenados
==========================

Drizzle actualmente no tiene ningún plugin que implemente procedimientos
almacenados. La implementación en MySQL no era óptima

Comandos eliminados
===================

-  ALTER TABLE UPGRADE
-  REPAIR TABLE
-  CREATE FUNCTION
-  CONVERT
-  SET NAMES
-  Borrado y actualizado multi-tabla

Funciones eliminadas
====================

-  crypt()
-  bit\_length()
-  bit\_count()

Palabras clave eliminadas
=========================

-  CIPHER
-  CLIENTE
-  CODE
-  CONTRIBUTORS
-  CPU
-  DEFINER
-  DES\_KEY\_FILE
-  ENGINES
-  EVERY
-  IO
-  IPC
-  ISSUER

Objetos eliminados
==================

-  No hay requerimiento de un schema mysql
-  No hay SET datatype, hay que usar ENUM
-  No hay comando SET NAMES, UTF-8 por defecto
-  No hay CHARACTER o CHARACTER SET, todo está por defecto en UTF-8
-  No hay TIME, DATETIME o INT
-  No hay TINYINT, SMALLINT o MEDIUMINT. Las operaciones de enteros han
   sido optimizadas para 32 y 64 bits
-  No hay TINYBLOB, MEDIUMBLOB o LONGBLOB. Hay un BLOB optimizado
-  No hay TINYTEXT, MEDIUMTEXT o LONGTEXT. Usar TEXT o BLOB
-  No hay UNSIGNED
-  No hay tipos de datos espaciales (GEOMETRY, POINT, LINESTRING,
   POLYGON)

 

Hay bastantes más cambios, pero con estos nos hacemos una idea de más o
menos lo que ha cambiado en este nuevo fork que acaba de publicar su
primera versión estable.

 

Podéis ver la lista de cambios completos aquí (inglés): `Drizzle
differences`_

 

.. _Drizzle differences: http://docs.drizzle.org/mysql_differences.html
