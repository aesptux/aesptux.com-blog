Instalar fonts en Linux.
########################
:date: 2010-02-08 13:30
:author: aesptux
:category: Linux
:tags: fonts, fuentes, instalar, Linux
:slug: instalar-fonts-en-linux

Para instalar nuevas fonts es muy sencillo:

Supongamos que nos hemos descargado un zip con varias fuentes:

    tar -c /home/usuario/Documentos/fonts.zip

Ahora tenemos que copiarlas a /usr/share/fonts. En mi caso, copio
también la carpeta para mantener un orden.

    cp -r /home/usuario/Documentos/fonts /usr/share/fonts/

Y por último agregamos las fonts a la caché:

    fc-cache /usr/share/fonts/carpeta
