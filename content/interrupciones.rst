Interrupciones
##############
:date: 2009-11-12 14:33
:author: aesptux
:category: General
:tags: interrupciones, irq
:slug: interrupciones

Dos opciones para que los perifericos interactuen:

#. Cada cierto tiempo el ordenador (S.O) controla si existe alguna
   operación pendiente con alguno de los periféricos genera mucha
   perdida de tiempo
#. Cuando un periférico necesita comunicar con el ordenador se genera
   una petición de interrupción IRQ en el sentido de la comunicación que
   sigue una serie de patrones.

Interrupción: Es una comunicación especial ordenador periférico para
indicar que dicho dispositivo necesita atención inmediata. Entonces en
ese momento suspende lo que estuviera haciendo para atender siempre y
cuando no exista petición anterior de mayor prioridad pendiente.

Prioridad de las IRQ:

De mayor a menor importancia:

Excepciones de la CPU (error en tiempo de ejecución)

Interrupción software

Interrupciones hardware (no enmascarables)

Interrupciones Hardware (enmascarables)

Funcionamiento:

-  Se genera la petición de interrupción
-  CPU STOP y gestiona la IRQ a través de lo que se llama ISR (Routine
   Service Interruption) vía un programa cargado en la ram o en la bios.
   A este programa se apunta con el lector de interrupción (este lector
   depende de cada de interrupción). La información de los vectores de
   interrupción apuntando al programa que gestiona dicha interrupción se
   carga al iniciar el sistema operativo. (BIOS: Sistema que se encarga
   de realizar las funciones básicas para que el ordenador arranque con
   determinado sistema operativo)
-  Se ejecuta el programa y una vez terminado la CPU continuará por
   donde iba.

 

Algunos vectores de interrupción:

**Vector Interrupción**

3 -> Punto de ruptura de interrupción

4-> Desbordamiento

9-> Teclado

14-> Fallo de página (MP)

32+255->libres

 

 

¿Cómo llega la IRQ a la CPU?

A través del bus de control y llegan a un controlador de interrupciones
que también es un dispositivo hardware, de aquí a la CPU.

 

Proceso más detallado

#. Dispositivo de E/S quiere interrumpir se le asigna una línea de
   interrupción en el bus
#. Envía la interrupción vía IRQ
#. Señal recogida, pasa al controlador de interrupciones (PIC) este lo
   que hace es que primero clasifica y segunda lo envía a la CPU
#. La cpu pregunta porque tipo de interrupción al PIC
#. El PIC contesta
#. Se genera el vector de interrupción y se sirve la interrupción.

 

**Líneas de petición de interrupción**

Existe un estándar de facto donde se asignan una serie de líneas de
interrupción donde se especifica el nombre de la interrupción, el
hexadecimal como código de la interrupción, y la descripción..

 

La instalación de un nuevo dispositivo de E/S en nuestro sistema
internamente ocurre:

Se realiza la asignación de una IRQ del sistema para dicho dispositivo.

¿Cómo se hace esto?

Antiguamente-> Conectar un jumper la placa base y el dispositivo

Hoy día-> Se resuelve vía driver o bien si el dispositivo es PnP.
