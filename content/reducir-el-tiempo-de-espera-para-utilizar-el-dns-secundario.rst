Reducir el tiempo de espera para utilizar el DNS Secundario. Balanceo de carga
##############################################################################
:date: 2011-05-06 14:17
:author: aesptux
:category: Linux, Networking
:tags: attempts, balancear, carga, distribuir, dns, Linux, nameserver, primario, resolv.conf, rotate, secundario
:slug: reducir-el-tiempo-de-espera-para-utilizar-el-dns-secundario

En el archivo\ **/etc/resolv.conf** se encuentran definidos los
servidores dns, por ejemplo:

    nameserver 192.168.1.10

    nameserver 192.168.1.11

Éstos actuarían como dns primario y secundario respectivamente. En caso
de que falle el primero, se utilizaría el segundo.

El problema se encuentra en que el tiempo de espera (**timeout**) es
alto, alrededor de unos 5 segundos, por lo que la utilización del
segundo dns no será instantánea.

Esto se puede solventar utilizando la directiva **options** y el
parámetro\ **timeout**:

    nameserver 192.168.1.10

    nameserver 192.168.1.11

    options timeout:1

Aquí lo que estamos indicando es que el tiempo de espera, sea de 1
segundo.

Si queremos distribuir la carga entre los dos servidores lo haremos de
la siguiente manera:

    nameserver 192.168.1.10

    nameserver 192.168.1.11

    options timeout:1 rotate attempts:1

Así, la carga se distribuirá entre los dos servidores evitando saturar
siempre el primero.

Vía \| `rm-rf.es`_

.. _rm-rf.es: http://rm-rf.es/hacer-que-etcresolv-conf-utilice-el-dns-secundario-o-balancee-carga/
