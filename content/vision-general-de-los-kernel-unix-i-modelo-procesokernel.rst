Visión general de los Kernel Unix (I): Modelo Proceso/Kernel.
#############################################################
:date: 2011-07-06 11:30
:author: aesptux
:category: Unix
:tags: excepciones, general, hilo, kernel, modelo, proceso, thread, unix, usuario, vision
:slug: vision-general-de-los-kernel-unix-i-modelo-procesokernel

Proveen un entorno de ejecución donde las aplicaciones se ejecutan.
Luego, el kernel debe implementar un conjunto de servicios y sus
correspondientes interfaces. Las aplicaciones utilizan esas interfaces y
normalmente no interactuan directamente con los recursos hardware.

Una CPU puede ejecutarse en modo Usuario o en modo Kernel. En realidad,
algunas CPUs pueden tener más de dos modos de ejecución, pero todos los
kernel estándar de Unix utilizan los dos modos mencionados
anteriormente.

Cuando un programa es ejecutado en modo usuario, no puede acceder
directamente a las estructuras del kernel o a los programas de éste.
Cuando se ejecuta en modo Kernel, sin embargo, esas restricciones
desaparecen. Cada modelo de CPU provee instrucciones especiales para
cambiar de modo Usuario a modo Kernel y vice versa. Un programa
normalmente se ejecuta en modo Usuario y cambia a modo Kernel sólo
cuando requiere de un servicio que provee el kernel. Cuando el kernel ha
completado la petición del programa, vuelve a modo Usuario.

Los procesos son entidades dinámicas que normalmente tienen una vida
limitada en el sistema. La tarea de crear, eliminar y sincronizar los
procesos existentes se delega a un grupo de rutinas del kernel.

El kernel como tal, no es un proceso si no un gestor de procesos. El
modelo proceso/kernel asume que los procesos que requieren un servicio
kernel utilizan lo que se conoce como llamadas al sistema. Cada llamada
al sistema establece el grupo de parámetros que identifican la petición
del proceso y después ejecuta la instrucción CPU independiente del
hardware para cambiar de modo Usuario a modo Kernel.

Además de los procesos de usuario, los sistemas Unix incluyen unos pocos
procesos privilegiados llamados hilos kernel (kernel threads) con las
siguientes características:

-  Se ejecutan en modo Kernel en el espacio de direcciones Kernel
-  No interactuan con usuarios, no requiere dispositivos terminales.
-  Normalmente son creados durante el inicio del sistema y permanecen
   vivos hasta que el sistema se apaga.

.. raw:: html

   <div style="text-align: justify;">

Los kernel Unix hacen mucho más que gestionar llamadas al sistema; de
hecho, las rutinas kernel pueden ser activadas de diferentes formas:

.. raw:: html

   </div>

.. raw:: html

   <div>

-  Un proceso invoca una llamada al sistema
-  La CPU recibe una excepción mientras ejecuta un proceso, lo cual es
   una condición inusual así como una instrucción no valida. El kernel
   gestiona la excepcion en nombre del proceso que la causó.
-  Un hilo kernel es ejecutado. Como se ejecuta en modo Kernel, el
   programa correspondiente debe ser considerado parte del kernel.

.. raw:: html

   </div>

