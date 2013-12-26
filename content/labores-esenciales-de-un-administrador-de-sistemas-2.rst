Labores esenciales de un administrador de sistemas
##################################################
:date: 2011-07-08 10:27
:author: aesptux
:category: Unix
:tags: actualizar, backups, copias, cuentas, hardware, instalar, kernel, monitorizar, operativos, problemas, resolucion, Security, sistemas, software, unix, usuario
:slug: labores-esenciales-de-un-administrador-de-sistemas-2

-  **Aprovisionamiento de cuentas**

El administrador de sistemas añade cuentas para los nuevos usuarios,
elimina las cuentas de los usuarios que ya no están activos y gestiona
todos los problemas posibles en relación a las cuentas, como por ejemplo
contraseñas olvidadas. El proceso de añadir y eliminar puede ser
automatizado, pero algunas decisiones (donde poner el home del usuario,
en que máquina, etc) deben hacerse antes  de añadir el usuario.

Cuando un usuario deje de pertenecer al sistema, su cuenta debe ser
deshabilitada. Se debe hacer una copia de seguridad de sus archivos y
sacarlos fuera del sistema para no acumular basura.

-   **Añadir y eliminar hardware**

Cuando se compra nuevo hardware o cuando el hardware es movido de una
máquina a otra, el sistema debe ser configurado para que reconozca y
utilice ese hardware. La dificultad de esta tarea puede variar por
ejemplo, desde instalar una impresora, hasta configurar un array de
discos.

Ahora con la virtualización, las configuraciones de hardware se
complican todavía más.

-  **Realizar copias de seguridad**

Quizás sea la tarea más importante del administrador de sistemas, y
también es la tarea más ignorada y que da más pereza realizar. Hacer
backups es aburrido y consume tiempo, pero son increíblemente
necesarias. Se pueden automatizar o delegar, pero sigue siendo
responsabilidad del administrador de sistemas cerciorarse de que se
ejectuan correctamente y en el tiempo planeado.

-   **Instalar y actualizar software**

Cuando se adquiere nuevo software, debe instalarse y probarse, a menudo
bajo diferentes sistemas operativos y diferente hardware.  Cuando el
software funciona correctamente, los usuarios deben ser informados de su
disponibilidad y localización. Si se trata de parches y actualizaciones
de seguridad, deben implementarse gentilmente en el entorno local.

El software local y los scripts administrativos deberían ser gestionados
de manera que sean compatibles con los procedimientos de actualización
utilizados.

-  **Monitorizar el sistema**

Las instalaciones grandes requieren de supervisión. No esperes que los
usuarios reporten sus problemas a no ser que sean graves. Regularmente
comprueba que el correo y servicio web funcionan correctamente, revisa
los ficheros log en busca de fallos o problemas, cerciórate de que las
redes locales están conectadas correctamente y mantén un ojo a la
disponibilidad de recursos en el sistema, como el espacio en disco. Todo
esto, se puede automatizar.

-  **Resolución de problemas**

Los fallos en el sistema son inevitables. Es el trabajo de un
administrador diagnosticar estos problemas y llamar a expertos si es
necesario. Normalmente es más difícil encontrar el problema que
solucionarlo.

-  **Mantener una documentación local**

Un sistema suele variar con las necesidades de la organización, y
comienza a diferir de lo que inicialmente se documentó. Como el
administrador de sistemas es responsable de estos cambios, también lo es
documentar los cambios.

-   **Seguridad**

El administrador es responsable de implementar una política de seguridad
y comprobar periódicamente que la seguridad no ha sido violada.


