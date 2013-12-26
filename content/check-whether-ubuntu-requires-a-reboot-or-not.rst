Check whether Ubuntu requires a reboot or not
#############################################
:date: 2012-01-12 15:46
:author: aesptux
:category: Linux
:tags: find, Linux, reboot, required, ubuntu
:slug: check-whether-ubuntu-requires-a-reboot-or-not

To find whether Ubuntu requires a reboot or not, is as simply as
checking if a special file exists.

To do so:

::

    file /var/run/reboot-required
    --------------------------
    ls /var/run/reboot-required | grep required

If the file exists, system would require a reboot.
