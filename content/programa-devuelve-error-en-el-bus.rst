Programa devuelve "Error en el bus"
###################################
:date: 2010-02-15 13:21
:author: aesptux
:category: Linux
:tags: bus, error, firefox, Linux, pidgin, programa, solucionar
:slug: programa-devuelve-error-en-el-bus

A mi me ha pasado, que tras un reinicio forzado, al ejecutar de nuevo
Pidgin, rhythmbox y el Centro de Software, no se me ejecutaban

El motivo era porque al iniciarse, daban un error en el bus. Esto puede
deberse a que algunas librerías hayan quedado corruptas.

Para solucionarlo podemos utilizar debsums:

    sudo apt-get install debsums

Chequeamos las librerías así:

    sudo debsums -s &> /tmp/debsums.txt

Ahora para no tener que estar instalando todas las librerías una a una,
generamos un archivo con las librerías dañadas:

    sudo cat /tmp/debsums.txt \| grep "mismatch"  \| cut -d " " -f4 \|
    uniq  > debsums\_reinstall.txt

Y finalmente:

    apt-get install --reinstall \`(cat debsums\_reinstall.txt)\`

Vía: Glug.es
