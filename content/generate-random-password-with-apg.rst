Generate random password with apg.
##################################
:date: 2011-12-10 23:44
:author: aesptux
:category: Linux
:tags: administration, apg, bash, command, fedora, generate, line, Linux, password, random, system, ubuntu, utility
:slug: generate-random-password-with-apg

Quick tip.

If you want to generate a **random** **password**, you could use
/dev/random, but it is more complex than using **apg**\ (Automated
Password Generator).

So, to install apg on Fedora, run this command:

::

    # yum install apg

Useful parameters:

.. raw:: html

   <ul style="text-align: justify;">

.. raw:: html

   <li>

**-a** algorithm choose algorithm

.. raw:: html

   </li>

-  **1** - random password generation according to password modes
-  **0** - pronounceable password generation

.. raw:: html

   <li>

**-n** num\_of\_pass           generate num\_of\_pass passwords

.. raw:: html

   </li>

.. raw:: html

   <li>

**-m** min\_pass\_len         minimum password length

.. raw:: html

   </li>

.. raw:: html

   <li>

**-x** max\_pass\_len          maximum password length

.. raw:: html

   </li>

.. raw:: html

   <li>

**-l** spell generated password

.. raw:: html

   </li>

.. raw:: html

   <li>

**-t** print pronunciation for generated pronounceable password

.. raw:: html

   </li>

.. raw:: html

   </ul>

Some examples:

.. raw:: html

   <div class="mceTemp mceIEcenter" style="text-align: justify;">

`|Examples of APG|`_
    Examples of APG. Click to zoom.

.. raw:: html

   </div>

.. _|image1|: http://aesptux.com/wp-content/uploads/2011/12/Selection_001.png

.. |Examples of
APG| image:: http://aesptux.com/wp-content/uploads/2011/12/Selection_001.png
.. |image1| image:: http://aesptux.com/wp-content/uploads/2011/12/Selection_001.png
