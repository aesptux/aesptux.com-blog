Optimizar Debian.
#################
:date: 2010-10-16 13:00
:author: aesptux
:category: Linux, Tutorial
:tags: arranque paralelo, cache, debian, optimizar, parallel starting, preload, receptivo, responsive
:slug: optimizar-debian

Antes de realizar cualquier cambio en el sistema, recomiendo hacer una
copia de seguridad de vuestra configuración actual, por lo que puediera
pasar.

Comenzamos:

El arranque secuencial tiene un pequeño problemilla: Si un servicio
tarda demasiado en arrancar, retrasará a los demás servicios.

La solución a esto es el *arranque paralelo.*\ Así un servicio que
inicie despacio, no retrasará a los demás

    # apt-get install insserv

Y ahora para activar el *arranque paralelo*:

    # echo 'CONCURRENCY=shell' >> /etc/default/rcS

Ahora pasamos a la parte de las aplicaciones

Preload corre como un daemon, monitorea lo que estás haciendo, los
programas que más usas y  se adapta. Esto significa que inicialmente no
verás ningún beneficio aparente, pero al cabo de unos días o semanas, la
diferencia será notable.

    # apt-get install preload

La configuración por defecto suele ser suficiente.

 

 

El siguiente cambio afectará al modo en que el kernel libera la cache de
dispositivos frente a las entradas del filesystem. Tener cacheadas las
entradas del filesystem hace que los filemanagers y otras aplicaciones
sean más receptivos. El valor por defecto es 100. Probaremos esto:

    # echo 'vm.vfs\_cache\_pressure=50' >> /etc/sysctl.conf

 

Con eso es suficiente, hay otras optimizaciones, pero yo no las he
implementado en mi sistema, así que no sé muy bien como reaccionarían.
Tampoco tengo el suficiente conocimiento técnico como para saber como
afectará esto a todos los sistemas.
