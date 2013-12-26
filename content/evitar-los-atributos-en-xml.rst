Evitar los atributos en XML.
############################
:date: 2011-03-28 13:30
:author: aesptux
:category: Programming, XML
:tags: atributos, datos, evitar, metadatos, xml
:slug: evitar-los-atributos-en-xml

Algunos de los problemas de (ab)usar de los atributos en XML son:

-  Los atributos no pueden contener valores múltiples. (Los elementos
   sí)
-  Los atributos no pueden contener estructuras en árbol. (Los elementos
   sí)
-  Los atributos no se pueden extender fácilmente (para futuros cambios)

Los atributos son difíciles de leer y mantener. Para datos es mejor
utilizar elementos. Usa atributos para información que no sea relevante
para los datos.

::

    <nota dia="10" mes="01" anio="2008"
    para="Marcos" de="Adrian" asunto="Recordatorio"
    contenido="No te olvides de mi cumpleaños eh :P">
    </nota>

 

El código anterior es complicado de leer, y ya que estamos no es para
nada bonito. La forma más correcta sería:

::

    <nota>
      <fecha>
      <dia>10</dia>
      <mes>01</mes>
      <anio>2008</anio>
    </fecha>
    <para>Marcos</para>
    <de>Adrian</de>
    <asunto>Recordatorio</asunto>
    <contenido>No te olvides de mi cumpleaños eh </contenido>
    </nota>

Un uso que podemos dar a los atributos en XML es para metadatos, es
decir, datos sobre los datos. Por ejemplo:

::

    <nota id="200">
      <fecha>
      <dia>10</dia>
      <mes>01</mes>
      <anio>2008</anio>
    </fecha>
    <para>Marcos</para>
    <de>Adrian</de>
    <asunto>Recordatorio</asunto>
    <contenido>No te olvides de mi cumpleaños eh</contenido>
    </nota>

Esta nota tiene un id "200", y otra nota cualquiera tendrá otro id
diferente, para así diferenciar las posibles notas que haya.
