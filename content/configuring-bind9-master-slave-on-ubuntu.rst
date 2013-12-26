Configuring BIND9 Master / Slave on Ubuntu.
###########################################
:date: 2011-11-08 02:04
:author: aesptux
:category: DNS, Linux
:tags: bind, bind9, desktop, dns, error, fix, Linux, master, permission, replicate, slave, solution, solve, transfer, ubuntu, zone
:slug: configuring-bind9-master-slave-on-ubuntu

I know it is strange to set up this type of configuration on an Ubuntu
Desktop, but we had to do it for Internet Services class, and it gave
problems to me and most of my class.

I am going to use two virtual machines, both running Ubuntu Desktop.
First step is installing bind9.

::

    # apt -get install bind9

The test domain will be "etg.local"

.. raw:: html

   <ul>

.. raw:: html

   <li>

**Master dns:**

.. raw:: html

   </li>

-  IP:  192.168.7.1
-  name: dns1

.. raw:: html

   <li>

**Slave dns:**

.. raw:: html

   </li>

-  IP: 192.168.7.2
-  name: pc02 (with dns2 CNAME)

.. raw:: html

   </ul>

*Be careful with using underscore on names.*

**MASTER**
----------

We are going to start by editing /etc/bind/named.conf.local, to define
our zone. I am going to define just one zone. You may want to define
also a reverse zone.

[caption id="attachment\_753" align="aligncenter" width="567"
caption="named.conf.local"]\ `|named.conf.local|`_\ [/caption]

Notice that the "type" of this host is **master**, that is important. We
also can see that I used absolute path to the file, because I did not
specified any directory on the options.

Allow-transfer, allow-update and also-notify are allowing our slave dns
to transfer the zone(s) file(s).

This is my zone file:

[caption id="attachment\_754" align="aligncenter" width="463"
caption="Zone file"]\ `|Zone file|`_\ [/caption]

 

We must pay attention to thenames to be fully qualified if they include
domain name, and both servers must be declared with NS register.

Finally we configure our DNS, this is my configuration file
/etc/resolv.conf

[caption id="attachment\_755" align="aligncenter" width="306"
caption="/etc/resolv.conf"]\ `|/etc/resolv.con|`_\ [/caption]

**SLAVE**
---------

Here comes the tricky part, at least with Ubuntu Desktop.

First, we configure /etc/resolv.conf to be equally as in master. Search
parameter must be "etg.local" and nameserver "127.0.0.1"

Now, we declare our zone, pay attention:

[caption id="attachment\_756" align="aligncenter" width="488"
caption="Zone declaration on slave"]\ `|Zone declaration on
slave|`_\ [/caption]

As you may see, we declared the type of this server as **slave,** and we
set who is its master(s).

Now it should replicate our zone from master server, but it won't until
we do a couple more of steps to avoid errors of writing permission.

We have to edit the file **/etc/apparmor.d/usr.sbin.named**

[caption id="attachment\_757" align="aligncenter" width="562"
caption="Default usr.sbin.named"]\ `|Default
usr.sbin.named|`_\ [/caption]

We have to find the line highlighted in red.

r stands for read, read permission. So we can deduce that it does not
have permission to write the zone, that is the because it gives us
permission errors.

We change that line to this:

[caption id="attachment\_758" align="aligncenter" width="308"
caption="Modified usr.sbin.named"]\ `|Modified
usr.sbin.named|`_\ [/caption]

And the last step is giving all permissions to the the bind group in the
bind folder:

::

    # chmod -R 775 /etc/bind

Now we restart first the bind server of the master and then the slave
with:

::

    # /etc/init.d/bind9 restart

Then if we want to check the log file to see if everything went fine
(slave):

::

    # tail -f /var/log/syslog

[caption id="attachment\_759" align="aligncenter" width="566"
caption="Syslog"]\ `|Syslog|`_\ [/caption]

I highlighted some important messages. It tells us that the zone
transfer went fine. Now we finally take a look to our recently
replicated zone file.

*Note: In the next screenshot you will se that the serial is 2. You can
transfer with serial, I just added another register (see www) to show
you that it really works*

[caption id="attachment\_760" align="aligncenter" width="515"
caption="Replicated zone"]\ `|Replicated zone|`_\ [/caption]

 

And that's all, it should work now.

.. _|image8|: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.08_00h13m01s_028_.png
.. _|image9|: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.08_00h23m41s_030_.png
.. _|image10|: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.08_00h30m52s_031_.png
.. _|image11|: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.08_00h40m47s_032_.png
.. _|image12|: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.08_00h45m01s_033_.png
.. _|image13|: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.08_00h49m25s_034_.png
.. _|image14|: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.08_00h54m50s_035_.png
.. _|image15|: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.08_00h57m33s_036_.png

.. |named.conf.local| image:: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.08_00h13m01s_028_.png
.. |Zone
file| image:: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.08_00h23m41s_030_.png
.. |/etc/resolv.con| image:: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.08_00h30m52s_031_.png
.. |Zone declaration on
slave| image:: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.08_00h40m47s_032_.png
.. |Default
usr.sbin.named| image:: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.08_00h45m01s_033_.png
.. |Modified
usr.sbin.named| image:: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.08_00h49m25s_034_.png
.. |Syslog| image:: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.08_00h54m50s_035_.png
.. |Replicated
zone| image:: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.08_00h57m33s_036_.png
.. |image8| image:: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.08_00h13m01s_028_.png
.. |image9| image:: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.08_00h23m41s_030_.png
.. |image10| image:: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.08_00h30m52s_031_.png
.. |image11| image:: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.08_00h40m47s_032_.png
.. |image12| image:: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.08_00h45m01s_033_.png
.. |image13| image:: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.08_00h49m25s_034_.png
.. |image14| image:: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.08_00h54m50s_035_.png
.. |image15| image:: http://aesptux.com/wp-content/uploads/2011/11/Snap_2011.11.08_00h57m33s_036_.png
