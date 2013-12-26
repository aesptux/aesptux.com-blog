Comenzando con Git. Primeros pasos
##################################
:date: 2011-07-14 12:02
:author: aesptux
:category: Internet, Programming
:tags: add, como, fork, git, github, hacer, master, origin, pasos, primeros, push, repositorio
:slug: comenzando-con-git-primeros-pasos

Lo primero será registrarnos en `http://www.github.com`_ y una vez
tengamos la cuenta, procedemos a instalarlo si no lo tenemos instalado.

    $ sudo apt-get install git

Ahora tenemos que generar nuestra clave SSH (antes tenemos que tener
instalado ssh)

    $ ssh-keygen -t rsa -C "nuestroemail@email.com"

Introducimos la passphrase y listo.

En github.com nos dirigimos a "Account Settings" -> "SSH Public Keys" ->
"Add another public". Aquí tendremos que copiar el contenido de nuestra
clave.

En la terminal hacemos los siguiente:

    $ cat ~/.ssh/id\_rsa.pub

Y copiamos y pegamos nuestra clave en github.

Para comprobar que todo se ha realizado correctamente, nos conectamos
mediante ssh a github:

    $ ssh -T git@github.com

Nos hará una pregunta, que contestamos con "yes", y debería mostrarnos
una frase como esta:

    Hi username! You've successfully authenticated, but GitHub does not
    provide shell access.

Si es así, hasta aquí está todo correcto.

Ahora tenemos que establecer nuestros datos:

    $ git config --global user.name "Nombre apellido"

    $ git config --global user.email "nuestro@email.com"

    $ git config --global github.user nombreusuario

Ahora tenemos que encontrar nuestro API Token, que lo encontraremos en
github.com -> "Account  Settings" -> "Account Admin"

    $ git config --global github.token 74673264923(el nuestro)

**Crear un repositorio nuevo**

En github.com, hacemos clic en "New Repository" y escribimos el nombre y
si queremos la descripcion y sitio web.

Para tener todo organizado vamos a centrar los repositorios en una
carpeta, por ejemplo:

    $ cd

    $ mkdir ~/Documents/repositorios && cd ~/Documents/repositorios

Es una buena práctica crear un README para cada repositorio, para ello:

    $ git init

    $ gedit README

Ahora que ya tenemos creado el README, vamos a hacer lo que se conoce
como 'commit'. Es una instantánea de nuestros archivos en un determinado
tiempo.

    $ git add README

    $ git commit -m "añadido README"

    $ git push origin master

Para añadir todo podemos hacer:

    $ git add .

**Hacer FORK a un repositorio**

En github.com, cuando encontremos un repositorio al que queramos hacer
fork, hacemos clic en el botón FORK y después copiamos la dirección que
sale un poco más abajo:

`|image0|`_

    $ git clone git@github.com:usuario/repositorio.git

Y eso es todo lo básico.

.. _`http://www.github.com`: http://www.github.com
.. _|image1|: http://aesptux.com/wp-content/uploads/2011/07/Selection_008.png

.. |image0| image:: http://aesptux.com/wp-content/uploads/2011/07/Selection_008-300x24.png
.. |image1| image:: http://aesptux.com/wp-content/uploads/2011/07/Selection_008-300x24.png
