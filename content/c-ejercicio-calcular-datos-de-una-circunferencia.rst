C: Ejercicio calcular datos de una circunferencia.
##################################################
:date: 2009-06-06 01:00
:author: aesptux
:category: Programming
:tags: c, circunferencia
:slug: c-ejercicio-calcular-datos-de-una-circunferencia

Aquí os dejo un ejercicio propuesto y resuelto, para los interesados en
la programación C.
 En el ejemplo resulto explico todo lo que puedo, para que sea fácil de
entender.

Programa que a partir del radio introducido por el usuario, calcule el
área, volumen y longitud.

Ejercicio Resuelto:

#include <stdio.h>
 #include <conio.h>
 #include <math.h>
 int main()
 {

//Declaracion de variables
 float pi = 3.14159265;
 float radio;
 float longitud;
 float volumen;
 float area;

//En esta seccion recogemos el dato introducido por el usuario
 printf("Escribe el radio del circulon");
 scanf("%f", &radio);

// Las respectivas operaciones
 longitud = 2 \* pi \* radio;
 volumen = (4/3) \* pi \* pow(radio,3);
 area = pi \* pow(radio,2);

// A continuacion muestra los resultados por pantalla
 printf("La longitud es : %fn", longitud);
 printf("El volumen es: %fn", volumen);
 printf("El area es: %fn", area);
 getch();

}

Como veis, para declarar las variables he utilizado float y no int, que
sería para un entero. Pow(x,y)  equivale a elevar una base(x) a un
exponente(y).

Cualquier duda podeis preguntar.
