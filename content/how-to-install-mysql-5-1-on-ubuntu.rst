How to install MySQL 5.1 on Ubuntu
##################################
:date: 2011-11-01 14:33
:author: aesptux
:category: Databases, Linux, MySQL
:tags: 5.1, administrator, browser, how, install, installing, Linux, mysql, query, sql, to, ubuntu
:slug: how-to-install-mysql-5-1-on-ubuntu

 

::

    # apt-get install mysql-client-5.1 mysql-client-core-5.1 mysql-common mysql-server-5.1 mysql-server-core-5.1 mysql-admin mysql-gui-tools-common mysql-query-browser

With this packages we install mysql client, mysql server and some
administration tools.

[caption id="attachment\_742" align="aligncenter" width="545"
caption="Packages to install"]\ `|Packages to install|`_\ [/caption]

Later, we will be asked to set up a root password:

[caption id="attachment\_743" align="aligncenter" width="545"
caption="Asking for root password"]\ `|Asking for root
password|`_\ [/caption]

Be sure to remember that password.

Once it is installed we can run MySQL Administrator to manage our
recently installed server.

[caption id="attachment\_744" align="aligncenter" width="480"
caption="MySQL Administrator Connection"]\ `|MySQL Administrator
Connection|`_\ [/caption]

It's highly recommended to create other user to work

[caption id="attachment\_745" align="aligncenter" width="561"
caption="Creating a new user"]\ `|Creating a new user|`_\ [/caption]

With MySQL Administrator you also can manage backups or check server's
health for example.

And finally, with MySQL Query Browser you can que to your server; create
new databases, insert values, sql queries, etc.

[caption id="attachment\_746" align="aligncenter" width="593"
caption="Creating a new database with Query Browser"]\ `|Creating a new
database with Query Browser|`_\ [/caption]

 

.. _|image5|: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.01_13h07m18s_001_.png
.. _|image6|: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.01_13h13m19s_002_.png
.. _|image7|: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.01_13h21m26s_003_.png
.. _|image8|: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.01_13h24m53s_004_.png
.. _|image9|: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.01_13h28m45s_005_.png

.. |Packages to
install| image:: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.01_13h07m18s_001_.png
.. |Asking for root
password| image:: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.01_13h13m19s_002_.png
.. |MySQL Administrator
Connection| image:: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.01_13h21m26s_003_.png
.. |Creating a new
user| image:: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.01_13h24m53s_004_.png
.. |Creating a new database with Query
Browser| image:: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.01_13h28m45s_005_.png
.. |image5| image:: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.01_13h07m18s_001_.png
.. |image6| image:: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.01_13h13m19s_002_.png
.. |image7| image:: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.01_13h21m26s_003_.png
.. |image8| image:: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.01_13h24m53s_004_.png
.. |image9| image:: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.01_13h28m45s_005_.png
