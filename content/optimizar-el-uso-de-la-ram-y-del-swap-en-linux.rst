Optimizar el uso de la RAM y del Swap en Linux.
###############################################
:date: 2010-12-15 13:00
:author: aesptux
:category: Linux
:tags: cambiar, memoria, ram, swap, swappiness, swapping, valor, zona
:slug: optimizar-el-uso-de-la-ram-y-del-swap-en-linux

La mayoría de los sistemas operativos modernos poseen un mecanismo
llamado memoria virtual, que permite hacer creer a los programas que
tienen más memoria que la disponible realmente; por ejemplo, 4 Gb en un
ordenador de 32 bits. Como en realidad no se tiene físicamente toda esa
memoria, algunos procesos no podrán ser ubicados en la memoria RAM.
 En este caso es cuando es útil el espacio de intercambio: el sistema
operativo puede buscar un proceso poco activo, y moverlo al área de
intercambio (el disco duro) y de esa forma liberar la memoria principal
para cargar otros procesos. Mientras no haga falta, el proceso extraído
de memoria puede quedarse en el disco, ya que ahí no gasta memoria
física. Cuando sea necesario, el sistema vuelve a hacer un intercambio,
pasándolo del disco a memoria RAM. Es un proceso lento (comparado con
usar sólo la memoria RAM), pero permite dar la impresión de que hay más
memoria disponible.

En Linux, existe un parámetro llamado '**swappiness**\ ' cuyo valor
estará situado entre 0 y 100. El valor 0 dará mucha más prioridad a la
ram que al swap, y si el valor es 100 al revés.

Para poder ver el swappiness que tenemos en nuestro sistema, hacemos lo
siguiente:

    $ cat /proc/sys/vm/swappiness

    60

El valor por defecto es 60.

Para cambiarlo tenemos que hacer lo siguiente:

    # sysctl vm.swappiness=45

En el caso de que queramos un valor de 45.

Este cambio no es persistente, y al reiniciar perderemos el cambio. Para
que el cambio se quede guardado hacemos lo siguiente:

    # vim /etc/sysctl.conf

Buscamos la línea y cambiamos el valor (si no está la añadimos)

    vm.swappiness=45

Guardamos y listo, ya tenemos cambiado el valor de nuestro swappiness.

 
