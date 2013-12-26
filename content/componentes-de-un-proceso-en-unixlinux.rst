Componentes de un proceso en Unix/Linux.
########################################
:date: 2011-07-10 19:33
:author: aesptux
:category: Linux, Operative Systems, Unix
:tags: apache, bind, componentes, cpu, direcciones, espacio, estado, euid, hilo, kernel, Linux, multithread, nice, niceness, pid, ppid, prioridad, proceso, quantum, thread, tiempo, time, uid, unix
:slug: componentes-de-un-proceso-en-unixlinux

Un proceso consiste de un espacio de dirección y un conjunto de
estructuras de datos en el kernel. La dirección es un conjunto de
páginas de la memoria que el kernel ha marcado para el uso de ese
proceso. Contiene el código y las librerías que el proceso utiliza, sus
variables, sus pilas e información extra utiliza por el kernel mientras
el proceso se está ejecutando. Dado que Unix y Linux son sistemas de
memorias virtuales, no hay ninguna correlación entre la localización de
las páginas en el espacio de direcciones del proceso y su localización
dentro de la memoria física o swap.

Las estructuras de datos internas del kernel registran información sobre
cada proceso. Algunas de las más importantes son:

.. raw:: html

   <ul style="text-align: justify;">

-  El mapa del espacio de direcciones del proceso.
-  El estado actual del proceso (durmiendo, detenido, etc.)
-  La prioridad de ejecución
-  Información sobre los recursos que ha utilizado el proceso
-  Información sobre los archivos y los puertos de red que el proceso ha
   abierto
-  El dueño del proceso

.. raw:: html

   </ul>

Un hilo de ejecución, normalmente conocido simplemente como hilo
(**thread**) es el resultado de un **fork** (bifurcación) del proceso.
Un thread hereda muchos de los atributos del proceso que lo contiene, y
múltiples threads pueden ejecutarse concurremente en un único proceso
bajo un modelo llamado **multithreading**.

La ejecución concurrente es simulada por el kernel en un sistema de un
único procesador, pero en los sistemas de varios núcleos o procesadores
(**multicore** o **multi-cpu**) la concurrencia se reparte entre los
diferentes núcleos. Las aplicaciones **multithread** como pueden ser
Apache o BIND obtienen su máximo rendimiento en sistemas multicore.

**PID: Process ID Number**

El kernel asigna un ID único a cada proceso. Es asignado a la vez que el
proceso es creado.

**PPID: Parent PID**

Ni Unix ni Linux tienen una llamada al sistema que inicie un nuevo
proceso ejecutando un programa en particular. En vez de eso, un proceso
existente debe clonarse a si mismo para crear un nuevo proceso. Luego el
clon, puede intercambiar el proceso que está ejecutando por otro
diferente. El PPID identifica el proceso del que se clonó (proceso
padre)

**UID and EUID**

La UID de un proceso es la identificación del usuario que lo ha creado.

La EUID es la identificación del usuario "efectiva", es una UID extra
usada para determinar que recursos y archivos puede acceder el proceso.
Para la mayoría de los procesos, la UID y EUID son idénticos.

**Niceness**

La prioridad del proceso determina cuánto tiempo de CPU recibe. El
kernel utiliza un algoritmo dinámico para computar las prioridades. El
kernel también presta atención a un valor que puede ser establecido por
el administrador llamado 'nice value' o 'niceness'. Llamado así del
inglés nice porque nos dice como de nice (buenos) vamos a ser con el
resto de usuarios del sistema.
