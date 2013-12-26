10 herramientas para dar más vida a tus scripts en shell
########################################################
:date: 2010-04-22 13:00
:author: aesptux
:category: Bash, Linux
:tags: bash, gui, herramientas, mas, mejorar, scripts, shell, vida
:slug: 10-herramientas-para-dar-mas-vida-a-tus-scripts-en-shell

En la mayoría de nuestros scripts, no utilizamos para nada una GUI, pero
a veces, si es un script que va a ir enfocado al usuario, es mejor
intentar usar una GUI para que sea más amigable.

Es una tarea que a lo mejor cuesta más porque hay que dedicarle un poco
más de tiempo, pero es algo que merece la pena, no todos aprecian la
belleza de la consola :D

-  **Notify-send**

Comando que envía notificaciones a través del daemon de notificaciones
(por defecto, se muestran casi en la esquina superior derecha). Para
poder utilizar ese comando, debemos instalar:

    $ sudo apt-get install libnotify-bin

Después basta con un simple:

    $ notify-send "texto"

Esto puede ser útil para mensajes que no tengan por qué interferir en la
actividad, del usuario... por ejemplo para informarle de algo.

[caption id="" align="aligncenter" width="463"
caption="notify-send"]\ `|notify-send|`_\ [/caption]

-  **Comando setleds**

Cambiar el estado de los leds del teclado

    $ setleds -D +num

Activaría el NumLock

    $ setleds -D -caps

Desactivaría el CapsLock

-  **Zenity**

Uno de mis favoritos. Muestra diálogos utilizando GTK+. Nos permite
mostrar información, pedir datos al usuario, etc...

[caption id="" align="aligncenter" width="721"
caption="Zenity"]\ `|Zenity|`_\ [/caption]

El resto de las herramientas, las podéis encontrar `aquí`_

Enlace \| `nixCraft`_

.. _|image2|: http://farm3.static.flickr.com/2707/4541655858_f8ffe7ab87_o.png
.. _|image3|: http://farm5.static.flickr.com/4026/4541064865_9daea96197_o.png
.. _aquí: http://www.cyberciti.biz/tips/spice-up-your-unix-linux-shell-scripts.html
.. _nixCraft: http://www.cyberciti.biz/tips/spice-up-your-unix-linux-shell-scripts.html

.. |notify-send| image:: http://farm3.static.flickr.com/2707/4541655858_f8ffe7ab87_o.png
.. |Zenity| image:: http://farm5.static.flickr.com/4026/4541064865_9daea96197_o.png
.. |image2| image:: http://farm3.static.flickr.com/2707/4541655858_f8ffe7ab87_o.png
.. |image3| image:: http://farm5.static.flickr.com/4026/4541064865_9daea96197_o.png
