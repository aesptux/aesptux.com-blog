Un poco más sobre el gestor pacman de Arch Linux.
#################################################
:date: 2010-02-01 12:59
:author: aesptux
:category: Linux
:tags: arch, gestor, Linux, mas, pacman, saber
:slug: un-poco-mas-sobre-el-gestor-pacman-de-arch-linux

Sincroniza la base de datos con los repositorios:

    pacman -Sy

Actualiza el sistema completo:

    pacman -Su

Instalar un paquete:

    pacman -S paquete

Eliminar un paquete:

    pacman -R paquete

Desinstala un paquete junto a las dependencias no utilizadas por otros
paquetes.:

    pacman -Rs paquete

Buscar un paquete específico:

    pacman -Ss paquete

Descargar el paquete sin instalarlo:

    pacman -Sw paquete

Muestra información sobre un paquete no instalado:

    pacman -Si paquete

Muestra información sobre un paquete instalado:

    pacman -Qi paquete

Borrar todos los archivos de la caché de pacman:

    pacman -Sc
