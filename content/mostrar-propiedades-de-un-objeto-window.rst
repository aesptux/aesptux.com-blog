Mostrar propiedades de un objeto window
#######################################
:date: 2009-06-18 15:36
:author: aesptux
:category: Programming, Web
:slug: mostrar-propiedades-de-un-objeto-window

Un pequeño truquillo para mostrar las propiedades de un objeto window:

`` <script type="text/javascript"> for (property in window) { document.write(property) document.write('<br />') } </script>``
