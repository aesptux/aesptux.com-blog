Herramienta rsync.
##################
:date: 2009-12-24 16:28
:author: aesptux
:category: Linux
:tags: backup, Linux, rsync
:slug: herramienta-rsync

Rsync es una herramienta fascinante para sincronizar carpetas y crear
copias de seguridad.

Un uso básico podría ser el siguiente:

    rsync -avuz "/media/pendrive/clase" "/home/usuario/materias"

-  **-a:**\ Mantener permisos, propietarios, etc.
-  **-v:**\ Verbose.
-  **-u:**\ Saltarse archivos que sean más recientes en el destino
   (actualizaciones)
-  **-z:** Comprimir durante la transferencia

    rsync -e ssh -avuz user@192.168.1.2:/home/user/imagenes
    /media/pendrive

El comando anterior sirve para transmitir vía SSH.

Luego mediante crontab podemos automatizarlo, por ejemplo para que cada
día a las 23.00 haga una copia:

    crontab -e

    \* 23 \* \* \* usuario rsync -avuz /home/user/fotos
    /media/pendrive/fotos 2>&1  > /var/rsync.log
