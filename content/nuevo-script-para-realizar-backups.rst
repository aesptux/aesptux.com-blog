Nuevo script para realizar backups
##################################
:date: 2011-07-17 12:27
:author: aesptux
:category: backup, Bash, Linux, Programming
:tags: backup, copia, ejemplo, Linux, script, Security
:slug: nuevo-script-para-realizar-backups

Ayer estuve escribiendo un nuevo script para realizar los backups en mi
sistema, ya que mis necesidades han cambiado.

El script está adaptado a mi sistema y como digo, mis necesidades, pero
quizás os pueda servir a vosotros.

::

    #!/bin/bash
    #    Backup for my system.
    #    Copyright (C) <2011>  <Adrian 'aesptux' Espinosa>
    #
    #    This program is free software: you can redistribute it and/or modify
    #    it under the terms of the GNU General Public License as published by
    #    the Free Software Foundation, either version 3 of the License, or
    #    (at your option) any later version.
    #
    #    This program is distributed in the hope that it will be useful,
    #    but WITHOUT ANY WARRANTY; without even the implied warranty of
    #    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    #    GNU General Public License for more details.
    #
    #    You should have received a copy of the GNU General Public License
    #    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    #    Check if the folder with the ID name exists
    #    Mount the device
    #    Backup our files
    #    Unmount the device
    NOW=$(date +%Y-%m-%d)
    LOGPATH="/root/backup/"
    LOGFILE="$NOW.backup.log"
    ERRORMSG="zenity --error --title Error --text "
    INFOMSG="zenity --info --title Information --text "
    RSYNC="rsync -avuz --progress --delete "
    # Device info
    DEV1="/dev/sda2/"
    LABEL1="Multimedia"
    ID1="A61052121051EA37"
    PATH1="Backup/actual"

    clear
    if [ $UID -ne 0 ]; then
        $ERRORMSG "Sorry you have to run this script as root"
        exit 1
    else
        if [ ! -d /media/$ID1 ]; then
            mkdir /media/$ID1
            if [ $? -eq 0 ]; then
                echo "Folder created" | tee -a $LOGPATH$LOGFILE
            else
                $ERRORMSG "Error creating folder. Exiting"
                echo "Error creating folder. Exiting" | tee -a $LOGPATH$LOGFILE
                exit 2
            fi
        fi
        mount $DEV1 /media/$ID1
        if [ $? -eq 0 ]; then
            echo "Disk mounted." | tee -a $LOGPATH$LOGFILE
            $INFOMSG "Backup started"
            $RSYNC /etc /media/$ID1/$PATH1 2>> $LOGPATH$LOGFILE
            $RSYNC /var /media/$ID1/$PATH1 --exclude "/var/cache/*" 2>> $LOGPATH$LOGFILE
            $RSYNC /home /media/$ID1/$PATH1 --exclude "/home/mortuus/Downloads/*" --exclude "/home/mortuus/Videos/*" --exclude "/home/mortuus/.VirtualBox/HardDisks/*" --exclude "/home/mortuus/.local/share/Trash/*" --exclude "/home/mortuus/.cache/*" --exclude "/home/mortuus/.thumbnails/*" --exclude "/home/mortuus/Dropbox" 2>> $LOGPATH$LOGFILE
            ###### MYSQL DATABASES DUMP
            mysqldump --all-databases -u root -p123456789a > /media/$ID1/$PATH1/$NOW.mysqldump.sql 2>> $LOGPATH$LOGFILE
            umount $DEV1
            $INFOMSG "Backup finished"
        else
            $ERRORMSG "Disk failed to mount. Exiting" 
            echo "Disk failed to mount. Exiting" | tee -a $LOGPATH$LOGFILE
            exit 3
        fi
    fi

También podéis encontrarlo en mi `Github`_

.. _Github: https://github.com/aesptux/bash-scripts/blob/master/backup.sh
