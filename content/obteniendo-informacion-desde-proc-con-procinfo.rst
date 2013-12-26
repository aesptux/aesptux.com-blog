Obteniendo información desde /proc con procinfo.
################################################
:date: 2011-03-23 13:00
:author: aesptux
:category: Linux
:tags: /proc, acerca, informacion, interrupciones, libre, memoria, obtener, ocupada, page, procinfo, saber, sistema, swap, uptime
:slug: obteniendo-informacion-desde-proc-con-procinfo

En  /proc podemos encontrar toda una fuente de información sobre nuestro
sistema, y para facilitarnos la tarea, tenemos el comando **procinfo**,
su instalación es muy sencilla:

    # apt-get install procinfo

Luego lo ejecutamos con

    # procinfo

Y nos mostrará la información del sistema.

**Memory:**\ Muestra el total de ram libre y ocupada. También muestra el
swap

**Bootup:**\ Hora de inicio del sistema.

**Load average:**\ Media de 'jobs' corriendo, seguido por el número de
procesos ejecutables y el número total de procesos, seguido por el PID
de el último proceso ejecutado.

**User:**\ Cantidad de tiempo empleada en correr 'jobs' en el espacio
del usuario

**Nice:**\ Cantidad de tiempo empleada en ejecutar 'niced jobs' en el
espacio del usuario

**System:**\ Cantidad de tiempo empleada ejecutada en el espacio del
kernel

**Idle:**\ Cantidad de tiempo sin hacer nada

**Uptime:**\ Tiempo que ha estado el sistema activo

**Page in:**\ Número de bloques del disco paginados en el núcleo del
disco.

**Page out:**\ Número de bloques del disco paginados fuera del disco.

**Swap in:**\ Número de páginas de memoria paginadas a el swap

**Swap out:**\ Número de páginas de memoria paginadas fuera del swap

**Interrupts:**\ Número de interrupciones servidas desde que se inició
el sistema.

La información completa la puedes encontrar en el respectivo manual del
comando.
