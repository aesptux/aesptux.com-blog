Enable "delete key" on GNOME3 (Fedora 15 and Ubuntu 11.04)
##########################################################
:date: 2011-09-05 20:03
:author: aesptux
:category: Linux
:tags: activate, dconf-editor, delete key, enable, fedora, files, gnome, gnome3, nautilus 3, remove, ubuntu
:slug: enable-delete-key-on-gnome3-fedora-15-and-ubuntu-11-04

By default, we can't delete files in Nautilus 3 with delete key, as we
did always, because it's deactivated.

For  enable this on Fedora 15, go to terminal and write this down:

    $ gsettings set org.gnome.desktop.interface can-change-accels true

Then go to a nautilus window, click on Edit menu and put the mouse over
(**don't press, only hover**) "Delete" and press delete key. You will
see the new shortcut at the right.

Once you've done it, I recommend to turn it off again:

    $ gsettings set org.gnome.desktop.interface can-change-accels false

If you use ubuntu you can use dconf-editor. Press ALT+F2 and write
**dconf-editor** and then follow this path: org > gnome > desktop >
interface and check can-change-accels.

Then, do the same as in Fedora, but you may have to hit the key twice.

Don't forget to uncheck the box for preventing changing other shortcuts.
