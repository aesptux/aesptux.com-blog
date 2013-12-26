Short and useful tip: How to make "tail -f" beep on each new line.
##################################################################
:date: 2011-11-28 12:30
:author: aesptux
:category: Bash, Linux
:tags: -f, bash, beep, each, fedora, file, follow, how, line, make, realtime, short, tail, tip, to, ubuntu, useful
:slug: short-and-useful-tip-how-to-make-tail-f-beep-on-each-new-line

Just in case you do not know, **tail**\ prints the last ten lines of the
indicated file. Like this:

::

    tail /var/log/yum.log

Furthermore, if you want to print more lines you can do it with
**-n** parameter:

::

    tail -n 20 /var/log/yum.log

But I think the most interesting parameter for **tail** is **-f**. This
parameter allows tail to "**f**\ ollow" the file. New data is displayed
as the file grows.

Now, using **sed** we can append to each new line, a bell sound:

::

    tail -f /var/log/yum.log | sed -e $'s/$/\a/'

Notice that '$' escape sequences will only work on bash.

This was tested on Fedora 16.


