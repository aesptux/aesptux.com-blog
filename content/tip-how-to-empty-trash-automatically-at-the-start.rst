Tip: How to empty Trash automatically at the start
##################################################
:date: 2011-09-24 11:33
:author: aesptux
:category: Linux
:tags: automatically, crontab, empty, fedora, how to, job, Linux, reboot, start, tip, trash, ubuntu
:slug: tip-how-to-empty-trash-automatically-at-the-start

This is an easy and fast tip.

We have to set up a cron job:

::

    $ crontab -e

And then we only have to write this line:

::

    @reboot rm -rf ~/.local/share/Trash/files/*

And that's it, on each reboot, Trash will be emptied. I tested this on
Ubuntu and Fedora.
