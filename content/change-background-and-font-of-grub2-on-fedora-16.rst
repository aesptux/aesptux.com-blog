Change background and font of Grub2 on Fedora 16.
#################################################
:date: 2011-11-23 15:11
:author: aesptux
:category: Linux
:tags: background, change, custom, customize, fedora 16, grub.cfg, grub2, Linux, modify
:slug: change-background-and-font-of-grub2-on-fedora-16

With **Fedora 16 Grub2** was introduced.

We have some major changes with grub2, for example, there's no menu.lst
anymore to edit entries.

I do not know the reason, but the default grub2 of Fedora 16 is raw,
with black background, in contrast to Fedora 15 with at least had a
background picture.

We can **customize** grub2 in an easy way, just a few steps:

1) Copy your desired wallpaper to \ **/boot **\ 

::

    # cp /home/user/Pictures/wallpaper1.jpg /boot/wall.jpg

2) Edit \ **/etc/default/grub ** and add the following lines:

::

    GRUB_GFXMODE=1920x1080x16
    GRUB_GFXPAYLOAD_LINUX=keep
    GRUB_BACKGROUND=/boot/wall.jpg

You can use whatever resolution is supported by your monitor.

Next step is to convert a **.ttf font**\ (if you want to use a different
font) to a suitable format, and generate our new grub.cfg

3) Generate font and grub.cfg

::

    # grub2-mkfont --output=/boot/grub2/unicode.pf2 /usr/share/fonts/Sansation/Sansation_Regular.ttf

    # grub2-mkconfig -o /boot/grub2/grub.cfg

In my case, I used Sansation font.

Then, all you have to do is reboot brand new GRUB2.

Here's mine:

[caption id="attachment\_778" align="aligncenter" width="640"
caption="My Grub2. Click to zoom."]\ `|image0|`_\ [/caption]

 

.. _|image1|: http://aesptux.com/wp-content/uploads/2011/11/picplz_20111123_00005879786_original.jpg

.. |image0| image:: http://aesptux.com/wp-content/uploads/2011/11/picplz_20111123_00005879786_original-1024x768.jpg
.. |image1| image:: http://aesptux.com/wp-content/uploads/2011/11/picplz_20111123_00005879786_original-1024x768.jpg
