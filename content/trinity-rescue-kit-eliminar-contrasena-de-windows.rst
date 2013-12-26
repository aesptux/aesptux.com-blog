Trinity Rescue Kit: Eliminar contraseña de Windows
##################################################
:date: 2009-12-13 15:40
:author: aesptux
:category: Others, Tutorial, Windows
:tags: contraseña, eliminar, kit, olvidada, rescue, trinity, Windows
:slug: trinity-rescue-kit-eliminar-contrasena-de-windows

Este magnífico kit nos permite, entre otras cosas eliminar nuestra
contraseña de Windows.

Imagínense que hemos olvidado nuestra contraseña, pues con unos
sencillos pasos la podremos dejar en blanco para más tarde volver a
acceder y cambiarla otra vez.

Lo primero es cargar el teclado en español:

    loadkeys es

[caption id="" align="alignnone" width="429" caption="Cargamos el
teclado en español."]\ `|loadkeys|`_\ [/caption]

Ahora listamos las cuentas de windows. También nos pedirá especificar en
que partición se encuentra windows, por si tenemos más de un sistema
operativo. Para listar las cuentas:

    winpass -l

[caption id="" align="alignnone" width="503" caption="Aquí vemos las
cuentas listadas."]\ `|listar cuentas|`_\ [/caption]

Ahora que sabemos el nombre exacto de nuestra cuenta, procederemos a
dejar en blanco la contraseña en este caso, de la cuenta
"Administrator":

    winpass -u Administrator

Nos pedirá otra vez elegir la partición

[caption id="" align="alignnone" width="632" caption="Atención con
syskey!"]\ `|syskey|`_\ [/caption]

Atención con esta pregunta, debemos responder que **no**\ queremos
deshabilitar syskey.

Y a continuación nos saldrá un menú:

#. Limpiar contraseña del usuario (dejarla en blanco)
#. Editar (poner una nueva) contraseña (Cuidado con esto en XP o Vista)
#. Promocionar usuario (hacerle administrador)
#. Desbloquear y activar cuenta

En nuestro caso, elegimos la opción 1 y si todo sale bien saldrá algo
así:

[caption id="" align="alignnone" width="557" caption="Operación
exitosa!"]\ `|resultado|`_\ [/caption]

.. _|image4|: http://farm3.static.flickr.com/2728/4180756203_cc3ffc83d9_o.png
.. _|image5|: http://farm3.static.flickr.com/2695/4180756279_450ef72ce4_o.png
.. _|image6|: http://farm3.static.flickr.com/2543/4180756359_547a1b18bf_o.png
.. _|image7|: http://farm3.static.flickr.com/2495/4180756465_f8f9e2fa3f_o.png

.. |loadkeys| image:: http://farm3.static.flickr.com/2728/4180756203_cc3ffc83d9_o.png
.. |listar
cuentas| image:: http://farm3.static.flickr.com/2695/4180756279_450ef72ce4_o.png
.. |syskey| image:: http://farm3.static.flickr.com/2543/4180756359_547a1b18bf_o.png
.. |resultado| image:: http://farm3.static.flickr.com/2495/4180756465_f8f9e2fa3f_o.png
.. |image4| image:: http://farm3.static.flickr.com/2728/4180756203_cc3ffc83d9_o.png
.. |image5| image:: http://farm3.static.flickr.com/2695/4180756279_450ef72ce4_o.png
.. |image6| image:: http://farm3.static.flickr.com/2543/4180756359_547a1b18bf_o.png
.. |image7| image:: http://farm3.static.flickr.com/2495/4180756465_f8f9e2fa3f_o.png
