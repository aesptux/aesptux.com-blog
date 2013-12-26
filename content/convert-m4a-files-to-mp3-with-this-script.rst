Convert m4a files to mp3 with this script.
##########################################
:date: 2012-05-10 13:32
:author: aesptux
:category: Bash, Linux, Programming
:tags: bash, convert, files, Linux, m4a, mp3, play, script, shell, transform, wav
:slug: convert-m4a-files-to-mp3-with-this-script

Some of my library was in m4a files, which I have problems to play,
furthermore I prefer having everything in mp3 format.

So I wrote the following script:

::

    echo "Dependencies: mplayer and lame"
    if [ $# -lt 1 ]; then
        echo "Usage: sh m4a2mp3.sh '/path/to/files'"
    else 
        echo "This could take sometime. Converting to 320kbps MP3 files..."
        sleep 1
        cd "$1"
        for i in *.m4a; do mplayer -ao pcm "$i" -ao pcm:file="$i.wav"; done
        for i in *.wav; do lame -h -b 320 "$i" "$i.mp3"; done
        echo "Cleaning the house..."
        rm -rf *.m4a
        rm -rf *.wav
    fi
    echo "All files converted. Thank you."

Usage is pretty straightforward:

::

    sh m4a2mp3.sh /path/to/your/songs

The only dependencies, as you can see also in the script are mplayer and
lame

You can install them with the following command:

::

    # Yum based (Fedora, CentOS, SuSE)
    yum install mplayer lame
    # Apt based (Debian, Ubuntu, Mint) (NOT TESTED)
    apt-get install mplayer lame

As always, you also can find the script on my Github.
