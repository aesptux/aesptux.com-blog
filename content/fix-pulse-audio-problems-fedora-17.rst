Fix pulse audio problems Fedora 17.
###################################
:date: 2012-10-06 14:08
:author: aesptux
:category: Linux
:tags: audio, fedora, fix, Linux, no sound, problem, pulse, pulseaudio
:slug: fix-pulse-audio-problems-fedora-17

With this release, I have been having some pulse audio problems.
Sometimes I do not have sound while playing  Spotify, Rhythmbox or any
other desktop player.

After a research, it is usually fixed with this three lines (not
always):

::

    rm -rf ~/.pulse
    pulseaudio --kill
    pulseaudio -vvvvv

Do not run it as root.
