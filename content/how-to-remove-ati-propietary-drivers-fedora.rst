How to remove ati propietary drivers. Fedora.
#############################################
:date: 2012-07-16 19:26
:author: aesptux
:category: Linux
:tags: ati, catalyst, driver, fedora, Linux, propietary, remove, yum
:slug: how-to-remove-ati-propietary-drivers-fedora

I wanted to give it a shot, and installed ATI propietary driver. It did
not ended well.

Gdm could not start, it stucked after loading services.

To remove it:

::

    # yum remove kmod-catalyst* xorg-x11-drv-cata*

I will not try them again.


