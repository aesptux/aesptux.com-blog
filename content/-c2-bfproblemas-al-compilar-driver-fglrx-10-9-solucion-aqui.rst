¿Problemas al compilar driver fglrx 10.9? Solución aquí.
########################################################
:date: 2010-10-21 12:30
:author: aesptux
:category: Linux, Tutorial
:tags: 10.9, ati, bad request, debian, driver, fglrx, no funciona, opensuse, privativo, problema, server, ubuntu, xorg
:slug: %c2%bfproblemas-al-compilar-driver-fglrx-10-9-solucion-aqui

Los desarrolladores del kernel han solucionado una vulnerabilidad
crítica y una librería que utilizaba fglrx ha sido eliminada.

El error puede ser algo así:

::

    /usr/src/kernel-modules/fglrx /
    make: Entering directory `/usr/src/packages/BUILD/kernel-2.6.35.50.3desktop'
      LD      /usr/src/kernel-modules/fglrx/built-in.o
      CC [M]  /usr/src/kernel-modules/fglrx/firegl_public.o
    /usr/src/kernel-modules/fglrx/firegl_public.c: In function ‘KCL_GetInitKerPte’:
    /usr/src/kernel-modules/fglrx/firegl_public.c:2378:5: warning: return makes integer from pointer without a cast
    /usr/src/kernel-modules/fglrx/firegl_public.c:2379:5: warning: return makes integer from pointer without a cast
    /usr/src/kernel-modules/fglrx/firegl_public.c:2380:5: warning: return makes integer from pointer without a cast
    /usr/src/kernel-modules/fglrx/firegl_public.c: In function ‘KCL_GetPageTableByVirtAddr’:
    /usr/src/kernel-modules/fglrx/firegl_public.c:2425:5: warning: return makes integer from pointer without a cast
    /usr/src/kernel-modules/fglrx/firegl_public.c:2428:5: warning: return makes integer from pointer without a cast
    /usr/src/kernel-modules/fglrx/firegl_public.c:2429:5: warning: return makes integer from pointer without a cast
    /usr/src/kernel-modules/fglrx/firegl_public.c: In function ‘KCL_TestAndClearPageDirtyFlag’:
    /usr/src/kernel-modules/fglrx/firegl_public.c:2598:5: warning: return makes integer from pointer without a cast
    /usr/src/kernel-modules/fglrx/firegl_public.c: In function ‘KCL_GetDmaPhysAddr’:
    /usr/src/kernel-modules/fglrx/firegl_public.c:2636:5: warning: return makes integer from pointer without a cast
    /usr/src/kernel-modules/fglrx/firegl_public.c:2637:5: warning: return makes integer from pointer without a cast
    /usr/src/kernel-modules/fglrx/firegl_public.c:2638:5: warning: return makes integer from pointer without a cast
    /usr/src/kernel-modules/fglrx/firegl_public.c:2640:5: warning: return makes integer from pointer without a cast
      CC [M]  /usr/src/kernel-modules/fglrx/kcl_acpi.o
      CC [M]  /usr/src/kernel-modules/fglrx/kcl_agp.o
      CC [M]  /usr/src/kernel-modules/fglrx/kcl_debug.o
      CC [M]  /usr/src/kernel-modules/fglrx/kcl_ioctl.o
    /usr/src/kernel-modules/fglrx/kcl_ioctl.c: In function ‘KCL_IOCTL_AllocUserSpace32’:
    /usr/src/kernel-modules/fglrx/kcl_ioctl.c:196:5: error: implicit declaration of function ‘compat_alloc_user_space’
    /usr/src/kernel-modules/fglrx/kcl_ioctl.c:196:5: warning: return makes pointer from integer without a cast
    make[1]: *** [/usr/src/kernel-modules/fglrx/kcl_ioctl.o] Error 1
    make: *** [_module_/usr/src/kernel-modules/fglrx] Error 2
    make: Leaving directory `/usr/src/packages/BUILD/kernel-2.6.35.50.3desktop'

Y la salida del comando 'glxinfo', así:

::

    root@normandy:~# glxinfo
    name of display: :0.0
    X Error of failed request:  BadRequest (invalid request code or no such operation)
      Major opcode of failed request:  136 (GLX)
      Minor opcode of failed request:  19 (X_GLXQueryServerString)
      Serial number of failed request:  15
      Current serial number in output stream:  15

Solucionar esto, a pesar de que quizás parezca lo contrario, es bastante
sencillo:

Nos movemos a la siguiente carpeta:

    Debian: cd /lib/modules/fglrx/build\_mod

    Otra posible localización: cd  /usr/src/kernel-modules/fglrx/

Ahora tenemos que editar el archivo **kcl\_ioctl.c**

    # gedit kcl\_ioctl.c

Buscamos la línea 197, el fragmento debe ser algo así:

::

    void* ATI_API_CALL KCL_IOCTL_AllocUserSpace32(long size)
    {
        return compat_alloc_user_space(size);
    }

    #endif // __x86_64__

Pues lo cambiamos por lo siguiente:

::

    void* ATI_API_CALL KCL_IOCTL_AllocUserSpace32(long size)
    {
        return arch_compat_alloc_user_space(size);
    }

    #endif // __x86_64__

Guardamos el archivo, y ahora tenemos que compilarlo otra vez, para
ello:

::

    # cd ..
    # ./make_install.sh

Y eso es todo, yo así conseguí arreglarlo.
