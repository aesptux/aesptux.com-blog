C: Hallar max y min de una serie de numeros
###########################################
:date: 2009-06-17 14:17
:author: aesptux
:category: Programming
:tags: max, min, numeros
:slug: hallar-max-min-serie-numeros

`` #include <stdio.h> #include <conio.h> int main () {``

int n,max,min,num;
 printf("introduce un numero :n");
 scanf ("%d",&num);
 max=num;
 min=num;
 for (n=1;n<11;n++)
 {
 printf("Introduce otro numero :n");
 scanf("%d",&num);
 if (num>max)
 max=num;
 else;
 if (num<min)
 min=num;
 else;
 }
 printf("El mayor es %d.n",max);
 printf("El menor es %d.n",min);
 getch();
 }
 Un ejemplo bastante sencillo, se introducen una serie de numeros, el
primer número introducido, se iguala a la variable max y min, porque de
momento como no hay más números, ese es el máximo y el mínimo. Se siguen
introduciendo números, y si el número introducido es mayor que el actual
max, entonces se igualará a max, si es menor que min, se igualará a min.
Y así sucesivamente hasta completar la serie de números.
