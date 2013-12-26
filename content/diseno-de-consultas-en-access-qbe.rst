Diseño de consultas en Access : QBE
###################################
:date: 2009-10-26 14:45
:author: aesptux
:category: Access, Databases
:tags: Access, consultas, diseño, qbe
:slug: diseno-de-consultas-en-access-qbe

.. raw:: html

   <div>

El diseño de las consultas en Access se realiza por un método llamado
QBE (Query By Example) que consiste en la construcción de la consulta en
un modo gráfico.

.. raw:: html

   </div>

-  **Consultas  de selección:**\ Son las consultas que extraen datos de
   una o más tablas para mostrarlos en una vista diferente. Muestra
   aquellos datos de una tabla que cumplen los criterios especificados
   en la consulta.
-  **Consultas de parámetros:**\ Una consulta parametrizada es una
   consulta que, cuando se ejecuta muestra un cuadro de diálogo propio
   que solicita información por ejemplo, criterios para recuperar
   registros o un valor que desea insertar en un campo. Para diseñar la
   consulta basta con introducir nombres de variables entre "[]" para
   que Access solicite los datos.
-  **Consultas de tabla de referencias cruzadas:**\ Las consultas de
   referencias cruzadas se utilizan para calcular y reestructurar datos
   de manera que su análisis sea más sencillo. Las consultas de
   referencias cruzadas calculan una suma, una media, un recuento u otro
   tipo de totales de datos, y agrupan los resultados en una tabla de
   dos entradas.
-  **Consultas de acción:**\ Son consultas que realizan cambios sobre
   los registros de las tablas a los que hacen referencia. Hay cuatro
   tipos:

   -  **Consulta de eliminación:**\ Elimina un grupo de registros de una
      o más tablas. Por ejemplo, puede utilizar una consulta de
      eliminación para quitar productos que ya no se fabrican o de los
      que no hay pedidos.
   -  **Consulta de actualización:**\ Realiza cambios globales en un
      grupo de registros de una o más tablas. Por ejemplo, puede
      aumentar los precios un 10% para todos los productos lácteos.
   -  **Consulta de datos anexados:**\ Agrega un grupo de registros de
      una o más tablas al final de una o más tablas. Por ejemplo,
      suponga que consigue nuevos clientes y que tiene una base de datos
      que contiene una tabla con información acerca de esos clientes.
      Para evitar tener que escribir toda esta información otra vez,
      puede anexar dicha tabla a la tabla Clientes.
   -  **Consulta de creación de tabla:**\ Crea una tabla nueva a partir
      de la totalidad o una parte de los datos de una o más tablas. Las
      consultas de creación de tablas son útiles para crear una tabla
      que desee exportar a otra base de datos o a una tabla histórica
      que contenga registros antiguos.

-  **Consultas específicas de SQL:**\ Son consultas que no se pueden
   definir desde la cuadrícula QBE de Access, si no que se tienen que
   definir directamente en SQL.

