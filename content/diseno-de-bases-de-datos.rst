Diseño de bases de datos
########################
:date: 2009-09-23 01:48
:author: aesptux
:category: Databases
:tags: bases, datos, diseño
:slug: diseno-de-bases-de-datos

**1. Diseño de bases de datos**

**1.1. Modelo de datos
**\ Un modelo de datos es un conjunto de conceptos, reglas y
convenciones que nos permiten describir los datos, las relaciones entre
los datos, las restricciones del mundo real y que nos permite manipular
dichos datos.
 Formalmente un modelo de datos sería MD = (R, O),
 Las Reglas serían la parte estática del modelo y las Operaciones la
parte dinámica
 **1.1.1. Parte estática
**\ Está compuesta de dos cosas: objetos y restricciones
 Objetos:
 • **Entidades**: Objeto abstracto o concreto del mundo real con
existencia propia y fácilmente identificable (persona, lugar, suceso,
etc.)
 • **Propiedades o atributos de las entidades**: Mínimo elemento lógico
de información que se puede encontrar en una entidad o relación entre
entidades.
 • **Dominio**: Rango de valores de cada atributo (nombre->alfanumérico,
cumpleaños-> fecha)
 • **Relación o asociación entre entidades**: Por ejemplo un grupo de
alumnos se relaciona con un aula.

**1.1.2. Tipos de restricciones**
 •\ **Las impuestas por el usuari**\ o las impone el mundo real (Por
ejemplo que los nº de teléfono tengan X números).
 •\ **Inherente al modelo**: El modelo de dato no nos permite
determinados objetos ni relaciones entre objetos.

DDL: Lenguaje de definición de datos
 Son órdenes que permiten describir la parte estática del modelo de
datos.

**1.1.3. Parte dinámica**
 Dinámica de un modelo de datos.
 Está compuesto por un conjunto de operaciones que se definen sobre la
estática del modelo y que se van a aplicar sobre los datos almacenados y
que se denominan ocurrencias.
 Las operaciones pueden ser:
 • **Selección**: Consiste seleccionar o localizar una o más
ocurrencias, por ejemplo de la entidad alumno localizar ocurrencia mayor
20 años
 •\ **Acción**: Operaciones que se realizan sobre ocurrencias
previamente seleccionadas, por ejemplo mirar, modificar, ver, insertar.

El lenguaje DML -> Lenguaje para la manipulación de datos
 **1.2. Pasos en el diseño de una base de datos**
 **1.2.1. Nivel conceptual**
 Consiste en analizar el mundo real para describir las entidades,
atributos y dominios y las relaciones entre entidades.
 Este modelo es totalmente independiente de cualquier sistema gestor de
base de datos (SGBD) El esquema conceptual es el modelo entidad-relación
(E/R)
 **1.2.2. Nivel lógico
**\ Se realiza la adaptación del esquema conceptual al tipo de SGBD que
vayamos a utilizar.
 **1.2.3. Nivel físico
**\ Se implementa el esquema relacional en el SGBD concreto (Access,
Oracle, MySQL).

**1.3. Modelo conceptual Entidad/Relación (E/R)
**\ • **Restricciones Entidad**: Debe tener existencia propia, puede
llevar asociado un predicado que deben cumplir todas las ocurrencias,
cada ocurrencia de la entidad debe poder distinguirse de las demás,
todas las ocurrencias de la entidad deben tener los mismos atributos.
Representación cuadrado con nombre de entidad.
 •\ **Restricciones atributo:** Cada atributo debe tener un significado
único y consistente, no es necesario especificar los atributos que se
obtienen mediante cálculos. Representación -----O nombre. Si el redondel
está en negrita, es el atributo principal (clave: identifica de forma
única cada ocurrencia de la entidad. Puede haber atributos alternativos
y atributos compuestos también. Por ejemplo Empleado->Clave: Nif…
alternativo: nº SS… Fecha nacimiento ->Día, mes, año: Compuesto

**1.4. Relaciones**
 La relación se representa con un rombo.
 **• Nombre:** Suele ser un verbo.
 **• Grado:** Número de entidades que asocia
 o Una entidad ( Persona – casa )
 o Binaria: Dos entidades (Profesor – imparte – Grupo)
 o Ternaria: Tres entidades ( Cliente – Hotel – Vuelo – contrata)
 •\ **Tipo de correspondencia:** Expresa el número de ocurrencias de la
entidad que pueden relacionarse con una ocurrencia de la otra entidad.
 Un profesor puede impartir a N grupos
 1 profesor – N grupos
 N Grupos – 1 grupos NM
 1 persona casada con una persona -> 1 – 1
 Cliente realiza pedido
 Cliente N pedidos
 Pedidos 1 cliente -> 1 N

**Cardinalidad** se expresa cómo (mínimo, máximo)
 Un profesor como mínimo imparte 1 grupo, máximo N.
 Un grupo es impartido como mínimo por 1, maximo N.
 Una persona se casa como minimo con 0, como máximo con 1.
 Cliente realiza como mínimo 1 como máximo N. un pedido como mínimo 1
como maximo por 1
