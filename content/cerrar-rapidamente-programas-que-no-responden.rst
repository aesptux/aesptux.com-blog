Cerrar rápidamente programas que no responden
#############################################
:date: 2009-07-28 01:27
:author: aesptux
:category: Windows
:tags: cerrar, programas, rapidamente
:slug: cerrar-rapidamente-programas-que-no-responden

En Unix tenemos el comando kill que es muy rápido y efectivo. Sin
embargo en Windows, es un engorro tener que abrir el Administrador de
tareas, buscar el programa y finalizarlo.

Hay una solución aún más rápida:

En un bloc de notas escribimos **taskkill /im programa**

Donde *programa* es el nombre el programa que no responde. Una vez hecho
lo guardamos como un *.bat*. Para hacerlo más genérico podemos poner
**taskkill.exe /f /fi "status eq not responding"** que directamente
cerrará aquellos programas que no estén respondiendo.
