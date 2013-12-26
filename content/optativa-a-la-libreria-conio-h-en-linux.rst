Optativa a la librería conio.h en Linux
#######################################
:date: 2009-04-03 10:39
:author: aesptux
:category: Linux, Programming
:tags: conio, Linux, ncurses, Programming
:slug: optativa-a-la-libreria-conio-h-en-linux

Bien es sabido por los programadores, que la librería conio.h es
exclusiva de Borland, y contiene las famosas funciones gotoxy(x,y),
clrscr(), getch()... que son tan usadas en programas en modo texto.

Pues bien, la librería conio.h no está disponible para GNU/Linux, pero
la alternativa es la librería ncurses.h. Esta librería no viene por
defecto instalada, pero su instalación en distribuciones basadas en
debian es bien sencilla, basta con esto:

apt-get update
 apt-get install ncurses\*

Y voilà! Ya tenemos instalado ncurses.h
 Esta librería, incluye las librerías stdio.h y conio.h. Bien ahora
vamos a ver como sería un programilla sencillo:
 ¿Qué es lo primero que hay que incluir?
 Obviamente, la librería ncurses.h

#include ncurses.h

Ahora se declararía la función principal, como siempre. Pero ahora, hay
incluir initscr(), para iniciar la pantalla. La sintaxis de algunas
funciones son diferentes: printw(), equivale a printf(), para borrar la
pantalla erase(), que equivaldría a clrscr(), scanw() equivale a
scanf(),. Entonces un pequeño programa que muestre un texto por pantalla
y nos pida dos números para hacer una operación, quedaría así:

#include ncurses.h

int main()
 {
 initscr();
 printw("Hola mundo!");
 getch();
 erase();

printw("Escribe dos numeros para que sean sumados");
 int a;
 scanw("%d", &a);
 int b;

.. raw:: html

   <div style="text-align:left;">

 scanw("%d", &b);

.. raw:: html

   </div>

 int c = a + b;
 printw("El resultado de la suma es: %dn", c);
 getch();

 endwin();

 return 0;
 }
 Es importante cerrar la aplicacion endwin();

A la hora de compilarlo, es la misma orden de siempre, pero añadiendo un
parámetro:
 gcc archivo.c -o archivo -lncurses

Con ese último parámetro, indicamos al compilador use esa librería.
 Y eso es todo por hoy.

Un saludo,

Mortuus.
