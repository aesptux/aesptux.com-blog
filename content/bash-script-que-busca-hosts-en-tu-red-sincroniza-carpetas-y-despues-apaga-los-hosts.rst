Bash script que busca hosts en tu red, sincroniza carpetas y después apaga los hosts.
#####################################################################################
:date: 2011-03-30 13:30
:author: aesptux
:category: Bash, Linux, Programming
:tags: apagar, bash, buscar, carpetas, hosts, nmap, red, remotamente, remoto, script, sincronizar
:slug: bash-script-que-busca-hosts-en-tu-red-sincroniza-carpetas-y-despues-apaga-los-hosts

En clase nos pidieron hacer un script que buscase hosts en tu red para
después apagarlos, o que incluso antes de apagarse sincronizasen unas
carpetas.

He tratado de automatizarlo todo lo que he podido, en mi red funciona
perfectamente, y el único requerimiento previo es que todos los hosts
tengan instalado un servidor SSH. Este script esta pensado para hosts
Linux, pero con algunos pequeños cambios se podría adaptar para Windows
también.

El código es el siguiente:

::

    #!/bin/bash
    # Find online hosts on your network, backup a directory and halt them
    # Copyright (C) <2011> <Adrian Espinosa>
    #
    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.
    #
    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    # GNU General Public License for more details.
    #
    # You should have received a copy of the GNU General Public License
    # along with this program. If not, see <http://www.gnu.org/licenses/>.
    # If you don't want to write every password, you should add the hosts keys to your machine.
    clear
    f=`echo networkscanned_$(date +%Y%m%d)`
    me=`echo $(whoami)`
    DIR="put_here_your_dir_to_sync"
    DEST="put_here_your_destination"
    if [ $UID -ne 0 ]
    then
       echo "Sorry, you have to run this script as root"
    else
       net=`ip route show | grep / | cut -d " " -f1`
       echo "Please, wait while your network is scanned"
       completescan=`nmap -sP $net | grep "is up" | cut -d " " -f2`
       clear
       echo "$completescan" > $f
       gateway=`ip route show | grep via | cut -d " " -f3`
       cat $f | egrep -v `echo $gateway$` > /tmp/net
       cat /tmp/net > $f
       rm -rf /tmp/net
       ownip=`ip route show | grep src | cut -d " " -f12`
       cat $f | grep -v $ownip > /tmp/net
       cat /tmp/net > $f
       rm -rf /tmp/net
       echo "Starting synchronization"
       for host in $(cat $f)
       do
         echo "Syncing with $host"
         rsync --progress -avhe ssh $me@$host:$DIR $DEST &> backup.log
         ssh $me@$host "shutdown -h now" &> backup.log
       done
       echo "Done. You may check backup.log to see if there are any errors"
       rm -rf $f
       exit 0
    fi # END

     

Hay que ser root para ejecutarlo y básicamente lo que hace es lo
siguiente

-  Si NO eres root

   -  Sale del programa

-  Si eres root

   -  Detecta tu red y máscara
   -  Escanea con nmap y recoge sólo la IP de los hosts y la guarda en
      fichero
   -  Detecta cuál es tu ip y tu gateway y los elimina del fichero
      anterior
   -  Recorre el fichero leyendo cada hosts y haciendo las
      correspondientes operaciones

.

Este script lo he probado en Debian, y como digo funciona correctamente.
En ubuntu hay que hacer unos pequeños cambios que podéis encontrar en
mi \ `github`_, también está publicado este script.

.. _github: https://github.com/aesptux
