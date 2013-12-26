Quick tip: MySQL disallow database creation which certain name
##############################################################
:date: 2012-10-29 23:43
:author: aesptux
:category: Databases, Linux, MySQL
:tags: as, certain, database, disallow, forbid, name, prevent, quick tip, schema, use, using
:slug: quick-tip-mysql-disallow-database-creation-which-certain-name

If we want to prevent a name to be used as a schema name, it is pretty
easy to accomplish:

::

    # move to your mysql data folder, default /var/lib/mysql
    cd /var/lib/mysql
    # create an empty folder with the desired name
    mkdir dontusethisname
    # set permissions to 000
    chmod 000 dontusethisname
    # change ownership to mysql user
    chown mysql:mysql dontusethisname

If you try to create this schema now, you will receive the following
error:

::

    mysql> create schema dontusethisname;
    ERROR 1007 (HY000): Can't create database

 

 
