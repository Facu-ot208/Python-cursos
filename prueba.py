#primero abrimos el menu principal donde el usuario elegira que hace a continuación
print ("MENU")
print("1.Registrar")
print("2.Cursos Disp")
print("3.Inscribirse")
print("4.Lista de espera")
print("5.Salir")
elec = int(input("Elija una opción: "))
if elec == 1:
 print("REGISTRO DE UN ALUMNO")
 elif elec == 2:
  print("CURSOS DISPONIBLES")
 elif elec == 3:
  print("INSCRIPCIÓN A CURSOS")
 elif elec == 4:
  print("LISTA DE ESPERA DE CURSOS:")
 elif elec == 5 :
  print("GRACIAS POR TU VISITA")


def inscribir():
    dni = input("DNI: ")
    alumno = buscar_estudiante(dni)
    if alumno == None:
        print("No existe.")
        return

    nombre = input("Curso: ")
    curso = buscar_curso(nombre)

    if curso == None:
        print("Ese curso no existe.")
        return

    for x in curso["inscriptos"]:
        if x["dni"] == dni:
            print("Ya está inscripto.")
            return

    for x in curso["espera"]:
        if x["dni"] == dni:
            print("Ya está en espera.")
            return

    if len(curso["inscriptos"]) < curso["cupos"]:
        curso["inscriptos"].append(alumno)
        print("Inscripción realizada.")
    else:
        curso["espera"].append(alumno)
        print("No hay cupos.")
        print("Se agregó a la lista de espera.")

def baja():
    dni = input("DNI: ")

    for curso in cursos:
        for alumno in curso["inscriptos"]:
            if alumno["dni"] == dni:
                curso["inscriptos"].remove(alumno)
                print("Baja realizada.")

                if len(curso["espera"]) > 0:
                    primero = curso["espera"][0]
                    curso["espera"].remove(primero)
                    curso["inscriptos"].append(primero)
                    print(primero["nombre"], "entró desde la lista de espera.")
                return

    print("No se encontró ese estudiante.")
