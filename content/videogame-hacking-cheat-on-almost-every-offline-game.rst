Videogame hacking. Cheat on almost every offline game.
######################################################
:date: 2011-11-29 17:06
:author: aesptux
:category: General
:tags: 2, ammo, be, call, cheat, counter strike, crysis, dead space, duty, effect, engine, game, hacking, life, mass, modern, money, succesfull, videogame, warfare
:slug: videogame-hacking-cheat-on-almost-every-offline-game

Sometimes we get stuck on a game, and we use **cheats**, that is ok. But
in certain cases there is no cheats or are very limited.

In games like Dead Space 2 it is not possible, I did not find any cheat.

We can use  `Cheat Engine`_.

Brief explanation:

When a game is running, the process is loaded into the **RAM**. This
process reserves some space on the memory for the variables. A variable
is like a box, it stores a value which can be integer, string, float,
etc. Well, this variables can be for example, our money or ammunition,
or even life and can be edited with **Cheat Engine **

`|image0|`_

This is the interface of Cheat Engine. Clicking on the button with green
borders, will open a process selector, in which we have to select our
game process.

Steps:

1- Open our desired game, in this case Dead Space 2

`|Ammo before editing|`_

2- Open Cheat Engine and select the correct process.

`|image2|`_

3- We know we have 9 shoots available, we are going to search that
number on the browser. We will see thousands of results, that is not
interesting because we do not know what variable is.

*Warning: Editing an unknown variable can result in a game crash.*

So now we go back to the game and shoot just one time, now our ammo will
be 8.  On Cheat Engine, put 8 and click **Next scan**, to indicate we
are still scanning for the same variable with before was 9, but now it
is 8. And so on, until we isolate our variable(s) (maybe two or three).

.. raw:: html

   <div class="mceTemp mceIEcenter">

`|Isolated variable|`_
    Isolated variable

.. raw:: html

   </div>

4- Once it is isolated, we drag to the underneath field and click with
right button to drop the menu and then click on Change Record --> Value.

.. raw:: html

   <div class="mceTemp mceIEcenter">

`|Changing the value|`_
    Changing the value

.. raw:: html

   </div>

5- We set up a new value, not to high, we can provoke an overflow and
crash the game. I put 999 and it worked fine.Now we go back to the game
and see the result. \ **¡999 ammo!**

.. raw:: html

   <div class="mceTemp mceIEcenter">

`|Final result|`_
    Final result

.. raw:: html

   </div>

6 - Play!

I have tested it with Counter Strike (offline) modifying money and ammo.
Also with Modern Warfare 2, Mass Effect, Crysis, and more games.

In Dead Space 2 I have modified ammo of all weapons, money and node
quantity.

It may be a bit thorny, but useful if there is no other way.

 

.. _Cheat Engine: http://www.cheatengine.org/downloads.php
.. _|image6|: http://files.droplr.com/files/21931279/JCYt.screenshot_01-02-2011_0-35.png
.. _|image7|: http://files.droplr.com/files/21931279/Wv2E.screenshot_01-02-2011_1-11.png
.. _|image8|: http://files.droplr.com/files/21931279/QtTI.screenshot_01-02-2011_1-13.png
.. _|image9|: http://files.droplr.com/files/21931279/zO9s.screenshot_01-02-2011_1-17.png
.. _|image10|: http://files.droplr.com/files/21931279/rFq1.screenshot_01-02-2011_1-20.png
.. _|image11|: http://files.droplr.com/files/21931279/cdtH.screenshot_01-02-2011_1-23.png

.. |image0| image:: http://files.droplr.com/files/21931279/JCYt.screenshot_01-02-2011_0-35.png
.. |Ammo before
editing| image:: http://files.droplr.com/files/21931279/Wv2E.screenshot_01-02-2011_1-11.png
.. |image2| image:: http://files.droplr.com/files/21931279/QtTI.screenshot_01-02-2011_1-13.png
.. |Isolated
variable| image:: http://files.droplr.com/files/21931279/zO9s.screenshot_01-02-2011_1-17.png
.. |Changing the
value| image:: http://files.droplr.com/files/21931279/rFq1.screenshot_01-02-2011_1-20.png
.. |Final
result| image:: http://files.droplr.com/files/21931279/cdtH.screenshot_01-02-2011_1-23.png
.. |image6| image:: http://files.droplr.com/files/21931279/JCYt.screenshot_01-02-2011_0-35.png
.. |image7| image:: http://files.droplr.com/files/21931279/Wv2E.screenshot_01-02-2011_1-11.png
.. |image8| image:: http://files.droplr.com/files/21931279/QtTI.screenshot_01-02-2011_1-13.png
.. |image9| image:: http://files.droplr.com/files/21931279/zO9s.screenshot_01-02-2011_1-17.png
.. |image10| image:: http://files.droplr.com/files/21931279/rFq1.screenshot_01-02-2011_1-20.png
.. |image11| image:: http://files.droplr.com/files/21931279/cdtH.screenshot_01-02-2011_1-23.png
