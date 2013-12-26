Hacking videojuegos. Trucos para casi cualquier juego en offline. Ejemplo Dead Space 2.
#######################################################################################
:date: 2011-02-01 12:30
:author: aesptux
:category: General, Others
:tags: cheat engine, cheats, dead, dead space 2, hackear, hacking, pc, space, trucos, videojuegos
:slug: hacking-videojuegos-trucos-para-casi-cualquier-juego-en-offline-ejemplo-dead-space-2

En algunas ocasiones, se nos atasca algún juego, y tiramos de alguna
combinación de teclas para aumentar munición o lo que necesitemos.

En algunos juegos eso no es posible, como es el caso del Dead Space 2,
en el cuál el truco para aumentar munición, dinero o nodos brilla por su
ausencia.

En este caso podemos utilizar `Cheat Engine`_.

Una breve explicación:

Cuando ejecutamos un juego, se carga el proceso en la ram. Ese proceso
tiene unas variables en la ram, que pueden ser editadas mediante Cheat
Engine. Estas variables pueden ser la munición, vida, dinero, etc.
cualquiera que tenga el juego (¿ya pilláis por dónde va la cosa?)

`|image0|`_

Esta es la interfaz de Cheat Engine.  El botón que está recuadrado en
verde es el que tenemos que pinchar para cargar el proceso, en este caso
el juego que nos interese

Empezamos los pasos a seguir:

1- Abrimos el juego que nos interese, en este caso voy a abrir Dead
Space 2

[caption id="" align="alignnone" width="761" caption="Munición antes de
editar la variable"]\ `|image1|`_\ [/caption]

2- Abrimos Cheat Engine y seleccionamos el proceso del juego

`|image2|`_

3- Como sabemos que tenemos 9 balas, buscamos 9 en el buscador. Vemos
que hay muchas variables. Entonces lo que haremos será gastar una bala,
y dar **Next scan** poniendo el numero actual de balas tras el disparo,
es decir 8. Y así, hasta que logremos aislar la(s) variable(s) en las
que se almacena la munición

[caption id="" align="alignnone" width="631" caption="Click para
ampliar"]\ `|image3|`_\ [/caption]

4- Una vez aislada la variable la arrastramos al cajón de abajo y con el
botón derecho sacamos el menú desplegable y hacemos click en Change
Record -> Value

[caption id="" align="alignnone" width="584" caption="Click para
ampliar"]\ `|image4|`_\ [/caption]

5- Establecer el nuevo valor, en mi caso voy a poner 999, y como vemos
**¡En el juego también tenemos 999 de munición!**

[caption id="" align="alignnone" width="629" caption="Click para
ampliar"]\ `|image5|`_\ [/caption]

6 - Jugar!

Yo lo he probado en el Counter Strike, modificando satisfactoriamente el
dinero y la munición

Con Dead Space 2 he modificado la munición de todas las armas, el
dinero, y la cantidad de nodos.

Quizás sea un poco engorroso, pero útil para cuando nos quedamos
atascados.

Espero que os sirva :D

.. _Cheat Engine: http://www.cheatengine.org/downloads.php
.. _|image6|: http://files.droplr.com/files/21931279/JCYt.screenshot_01-02-2011_0-35.png
.. _|image7|: http://files.droplr.com/files/21931279/Wv2E.screenshot_01-02-2011_1-11.png
.. _|image8|: http://files.droplr.com/files/21931279/QtTI.screenshot_01-02-2011_1-13.png
.. _|image9|: http://files.droplr.com/files/21931279/zO9s.screenshot_01-02-2011_1-17.png
.. _|image10|: http://files.droplr.com/files/21931279/rFq1.screenshot_01-02-2011_1-20.png
.. _|image11|: http://files.droplr.com/files/21931279/cdtH.screenshot_01-02-2011_1-23.png

.. |image0| image:: http://files.droplr.com/files/21931279/JCYt.screenshot_01-02-2011_0-35.png
.. |image1| image:: http://files.droplr.com/files/21931279/Wv2E.screenshot_01-02-2011_1-11.png
.. |image2| image:: http://files.droplr.com/files/21931279/QtTI.screenshot_01-02-2011_1-13.png
.. |image3| image:: http://files.droplr.com/files/21931279/zO9s.screenshot_01-02-2011_1-17.png
.. |image4| image:: http://files.droplr.com/files/21931279/rFq1.screenshot_01-02-2011_1-20.png
.. |image5| image:: http://files.droplr.com/files/21931279/cdtH.screenshot_01-02-2011_1-23.png
.. |image6| image:: http://files.droplr.com/files/21931279/JCYt.screenshot_01-02-2011_0-35.png
.. |image7| image:: http://files.droplr.com/files/21931279/Wv2E.screenshot_01-02-2011_1-11.png
.. |image8| image:: http://files.droplr.com/files/21931279/QtTI.screenshot_01-02-2011_1-13.png
.. |image9| image:: http://files.droplr.com/files/21931279/zO9s.screenshot_01-02-2011_1-17.png
.. |image10| image:: http://files.droplr.com/files/21931279/rFq1.screenshot_01-02-2011_1-20.png
.. |image11| image:: http://files.droplr.com/files/21931279/cdtH.screenshot_01-02-2011_1-23.png
