Fix yum error TypeError: can't multiply sequence by non-int of type 'float'
###########################################################################
:date: 2013-01-03 13:20
:author: aesptux
:category: Linux, Python
:tags: bug, can't, fedora, float, Linux, multiply, non-int, package, python, sequence, TypeError, update, yum
:slug: fix-yum-error-typeerror-cant-multiply-sequence-by-non-int-of-type-float

I ran into this bug which prevented me to update yum packages, and after
a quick search, this helped to fix it:

::

    # vim /usr/lib/python2.7/site-packages/urlgrabber/grabber.py

Go to line 1539, with vim you can use **:1539**

Replace the line with this:

::

    if cur > (float(max_size)*1.10):

 
