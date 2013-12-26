Fix bug: Fedora 17 does not shutdown. Kernel Panic.
###################################################
:date: 2012-05-30 21:00
:author: aesptux
:category: Linux
:tags: down, error, fedora, fix, kernel, Linux, not, panic, problem, shutdown, shutting, solve, upgrade, upgrading
:slug: fix-bug-fedora-17-does-not-shutdown-kernel-panic

If you upgraded from Fedora 16 to Fedora 17, you may get an error when
shutting down the system.

This happens because the kernel is the same, and grub2.cfg does not get
the Fedora 17 kernel, but it is installed, although not recognized.

To fix this just run the following command:

::

    # grub2-mkconfig > /etc/grub2.cfg && grub2-install /dev/sda

Notice that you should change /dev/sda for your partition

This will generate a new grub2.cfg with the new Fedora 17 kernel.
