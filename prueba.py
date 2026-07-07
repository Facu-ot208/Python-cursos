#primero abrimos el menu principal donde el usuario elegira que hace a continuación
def main():
 while True:
  print ("\nMENU")
  print("1.Registrar estudiante")
  print("2.Ver cursos disponibles")
  print("3.Inscribirse a un curso")
  print("4. Ver lista de espera")
  print("5. Salir")
opcion = input("Elija una opción: ").strip()
if opcion == "1":
 print("\nREGISTRO DE UN ALUMNO")
 registrar_estudiante()
 elif opcion == "2":
  print("\nCURSOS DISPONIBLES")
  ver_cursos_disponibles()
 elif elec == 3:
  print("\nINSCRIPCIÓN A CURSOS")
  inscribir_estudiante()
 elif elec == 4:
  print("\nLISTA DE ESPERA DE CURSOS:")
  ver_lista_espera()
 elif elec == 5 :
  mostrar_estadisticas_finales()
  print("\nGRACIAS POR TU VISITA")
  break
else:
print("Opcion invalida, intente de nuevo")


def inscribir_estudiante():
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
