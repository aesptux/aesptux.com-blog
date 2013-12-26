Instalar y configurar Oracle XE en Linux
########################################
:date: 2010-01-12 11:51
:author: aesptux
:category: Databases, Oracle
:tags: configurar, instalar, Linux, Oracle
:slug: instalar-y-configurar-oracle-xe-en-linux

Lo primero que debemos hacer es descargar el correspondiente .rpm o
.deb, en mi caso he descargado el .deb

Podemos descargarlo desde la `página oficial`_

Una vez instalado, debemos configurarlo:

    sudo /etc/init.d/oracle-xe configure

    Oracle Database 10g Express Edition Configuration
     -------------------------------------------------
     This will configure on-boot properties of Oracle Database 10g
    Express
     Edition.  The following questions will determine whether the
    database should
     be starting upon system boot, the ports it will use, and the
    passwords that
     will be used for database accounts.  Press <Enter> to accept the
    defaults.
     Ctrl-C will abort.
     Specify the HTTP port that will be used for Oracle Application
    Express [8080]:**8080**
     Specify a port that will be used for the database listener
    [1521]:**1521**
     Specify a password to be used for database accounts.  Note that the
    same
     password will be used for SYS and SYSTEM.  Oracle recommends the
    use of
     different passwords for each database account.  This can be done
    after
     **initial configuration:
     Confirm the password:**
     Do you want Oracle Database 10g Express Edition to be started on
    boot (y/n) [y]:**y**
     Starting Oracle Net Listener...Done
     Configuring Database...Done
     Starting Oracle Database 10g Express Edition Instance...Done
     Installation Completed Successfully.
     To access the Database Home Page go to "http://127.0.0.1:8080/apex"

Y ya está!

Ahora sólo nos queda acceder a la página de inicio de Oracle XE y
acceder con el usuario SYS o SYSTEM y la contraseña que hemos elegido.

[caption id="" align="aligncenter" width="500"
caption="Oracle."]\ `|Oracle|`_\ [/caption]

.. _página oficial: http://www.oracle.com/technology/software/products/database/xe/htdocs/102xelinsoft.html
.. _|image1|: http://farm3.static.flickr.com/2715/4266865159_a3e552882d.jpg

.. |Oracle| image:: http://farm3.static.flickr.com/2715/4266865159_a3e552882d.jpg
.. |image1| image:: http://farm3.static.flickr.com/2715/4266865159_a3e552882d.jpg
