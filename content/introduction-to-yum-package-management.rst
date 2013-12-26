Introduction to Yum package management.
#######################################
:date: 2011-09-16 13:39
:author: aesptux
:category: Linux
:tags: fedora, how to, install, Linux, list, management, manager, package, remove, rpm, search, yum
:slug: introduction-to-yum-package-management

Yum is the package manager of Fedora.It is able to install, remove,
update and query packages.

First of all, if you want to work with Yum, you have to have superuser
privileges, so we first log in as root:

::

    $ su -

Updating packages
-----------------

If we want to check if there are updates, we can use the next command:

::

    # yum check-update

Easy, isn't it? Next step, is update packages. We can choose whether
update all or just a single one.

Updating everything:

::

    # yum update

Updating a single one:

::

    # yum update packagename

    # yum update google-chrome-stable

We are also able to make queries to find our desired package.

::

    # yum search term1 [term2 term3 termN]

If we want to list available packages we can use:

::

    # yum list available

To list installed packages:

::

    # yum list installed

To retrieve information about a package we use:

::

    # yum search packagename

To install a package:

::

    # yum install packagename

And to remove:

::

    # yum remove packagename

 

Yum is a quit powerful package manager, with a good and clear syntax.
