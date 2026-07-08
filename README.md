# Python-cursos
### Integrantes del Curso:
- Camnasio, Avril
- Insaurralde Anriquez, Santiago Gabril
- Muñoa, Eugenia Ibel
- Muzzupappa, Nahir
- Otero, Nelson Facundo

Comision: ISI A - K1.1

### Descripción general del sistema:
Este programa está desarrollado en Python y permite gestionar la `inscripción de estudiantes a cinco cursos de gastronomía`, cada uno con un cupo máximo definido. En lugar de una base de datos, utiliza tres archivos de texto plano: uno para registrar a los estudiantes (DNI y nombre), otro para las inscripciones confirmadas, y otro para la lista de espera cuando un curso ya no tiene lugares disponibles. El sistema funciona mediante un menú interactivo por consola que se repite hasta que el usuario decide salir. Desde allí se puede registrar un nuevo estudiante, consultar el estado de los cursos (cupo, ocupados y si hay lista de espera), inscribirse a un curso, y ver el detalle completo de quienes están en lista de espera. Al inscribirse, el sistema verifica primero que el estudiante esté registrado; luego, si el curso elegido tiene cupo disponible lo inscribe directamente, y si no, lo agrega a la lista de espera de ese curso. Al finalizar el programa, se muestran estadísticas generales con el total de registrados, inscriptos y personas en espera

### Instrucciones de Ejecucción:
Al ejecutar el archivo, el programa muestra el menú con las 5 opciones disponibles.
- Si se elige opción 1, se ejecuta registrar_estudiante(): pide DNI y nombre y si todo es correcto, guarda la línea dni,nombre en gral_estudiantes.txt.
- Si se elige opción 2, se ejecuta ver_cursos_disponibles(): recorre el diccionario CURSOS, y para cada uno cuenta los inscriptos y verifica si hay lista de espera, mostrando todo en una tabla por pantalla.
- Si se elige opción 3, pide el DNI, busca el nombre asociado, (si no existe, corta y pide registrarse primero), muestra la lista de cursos con sus cupos ocupados, y según lo que elija el usuario, verifica si hay lugar disponible; si hay cupo, escribe la inscripción en inscripciones.txt, y si no, la escribe en lista_espera.txt.
- Si se elige opción 4, lee todas las líneas de la lista de espera y las muestra agrupadas por curso, con nombre y DNI de cada persona.
- Si se elige opción 5, cuenta las líneas de los tres archivos, muestra los totales (registrados, inscriptos, en espera) y luego finaliza la ejecución del programa.
- Cualquier otro valor ingresado en el menú no coincide, por lo que el programa simplemente vuelve a mostrar el menú.

 
> La IA que utilizamos para el trabajo fue `Claude IA`, la utilizamos para poder ayudarnos cuando no entendiamos que nos faltaba para que el codigo funcione; o cuando ocurria un error y por mas que se intentaba corregir, no se arreglaba.
