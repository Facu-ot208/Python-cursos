#definimos los archivos y cursos con sus cupos
ARCHIVO_ESTUDIANTES = "gral_estudiantes.txt"
ARCHIVO_INSCRIPCIONES = "inscripciones.txt"
ARCHIVO_ESPERA = "lista_espera.txt"

CURSOS = {
 "Panadería Artesanal": 5,
 "Cocina Italiana": 3,
 "Repostería Básica": 4,
 "Sushi y comida Asiática": 2,
 "Parrilla y Asados": 6
}

#definimos la funcion para buscar si existe el nombre del estudiante en el archivo
def buscar_nombre_por_dni(dni):
    try:
        with open(ARCHIVO_ESTUDIANTES, "r") as f:
            for linea in f:
                datos = linea.strip().split(",")
                if datos[0] == dni:
                    return datos[1]
    except FileNotFoundError:
        pass
    return None

#definimos la funcion para registrar el estudiante en el archivo- escribe el dni y el nombre
def registrar_estudiante():
 print("\n--- Registro de Estudiante ---")
 dni = input("Ingrese DNI: ").strip()
 nombre = input("Ingrese Nombre Completo: ").strip()
 if not dni or not nombre:
  print("Error: el DNI y el nombre no pueden estar vacíos")
  return
 if buscar_nombre_por_dni(dni) is not None:
  print("Error: ese DNI ya está registrado")
  return
 with open(ARCHIVO_ESTUDIANTES, "a") as f:
  f.write(f"{dni},{nombre}\n")
  print("Estudiante registrado con éxito")

#funcion para contar ocupados en un curso leyendo el archivo
def contar_inscriptos(nombre_curso):
 contador = 0
 try: 
  with open (ARCHIVO_INSCRIPCIONES, "r") as f:
   for linea in f:
    if linea.startswith(nombre_curso + ","):
     contador += 1
 except FileNotFoundError:
  pass
 return contador

#función para ver todos los cursos disponibles
def ver_cursos_disponibles():
 print("\n" + "="*70)
 print(f"{'CURSO':<30} | {'CUPO':<10} | {'OCUPADOS':<10} | {'LISTA ESPERA'}")
 print("-" * 70)
 curso_top = None
 max_ocupados = -1
 for nombre, cupo_max in CURSOS.items():
  ocupados = contar_inscriptos(nombre)
  espera_status = "SÍ" if verificar_lista_espera(nombre) else "NO"
  print(f"{nombre:<30} | {cupo_max:<10} | {ocupados:<10} | {espera_status}")
  if ocupados > max_ocupados:
            max_ocupados = ocupados
            curso_top = nombre
  print("="*70)
  if max_ocupados > 0:
   print(f"Curso con mayor demanda: {curso_top} ({max_ocupados} inscritos)")

#función clave para incribir estudiante a un curso
def inscribir_estudiante():
 print("\n--- Inscripción a Curso ---")
 dni = input("Ingrese su DNI: ").strip()
 nombre = buscar_nombre_por_dni(dni)
 if nombre is None:
  print("Error: debe registrarse antes de inscribirse a un curso")
  return  
 lista_cursos = list(CURSOS.items())
 print("\nCursos disponibles:")
 for i, (nombre_curso, cupo_max) in enumerate(lista_cursos, start=1):
  ocupados = contar_inscritos(nombre_curso)
  print(f"{i}. {nombre_curso} - Cupos ocupados: {ocupados}/{cupo_max}")   
 opcion = input("Elija el número de curso: ").strip() 
 if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > len(lista_cursos):
  print("Opción Inválida")
  return
 indice = int(opcion) - 1
 nombre_curso, cupo_max = lista_cursos[indice]
 ocupados = contar_inscriptos(nombre_curso)
 if ocupados < cupo_max:
  with open(ARCHIVO_INSCRIPCIONES, "a") as f:
   f.write(f"{nombre_curso}, {dni}, {nombre}\n")
  print(f"{nombre} fue inscrito en {nombre_curso}.")
 else:
  with open(ARCHIVO_ESPERA, "a") as f:
   f.write(f"{nombre_curso}, {dni}, {nombre}\n")
  print(f"No hay cupo, {nombre} fue agregado a la lista de espera de {nombre_curso}.")

#verifica si existe una lista de espera para un determinado curso.
def verificar_lista_espera(nombre_curso):
 try:
  with open(ARCHVIO_ESPERA, "r") as f:
   for linea in f:
    if linea.startswith(nombre_curso + ","):
     return True
 except FileNotFoundError:
  pass
 return False

#funcion que lee todo el archivo y muestra el detalle completo, con nombre y DNI de cada persona en espera, agrupado por curso (según el orden en que quedaron guardados)
def ver_lista_espera():
 print("\n--- Lista de Espera por Curso ---")
 try:
  with open(ARCHIVO_ESPERA, "r") as f
  lineas = f.readlines()
 except FileNotFoundError:
  print("Todavía no hay nadie en lista de espera")
  return
 if not lineas:
  print("Todavía no hay nadie en lista de espera")
  return
 for linea in lineas:
  curso, dni, nombre = linea.strip().split(",")
  print(f"{curso}: {nombre} (DNI {dni})")


#abrimos el menu principal donde el usuario elegira que hace a continuación
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
 elif opcion == 3:
  print("\nINSCRIPCIÓN A CURSOS")
  inscribir_estudiante()
 elif opcion == 4:
  print("\nLISTA DE ESPERA DE CURSOS:")
  ver_lista_espera()
 elif opcion == 5 :
  mostrar_estadisticas_finales()
  print("\nGRACIAS POR TU VISITA")
  break
else:
print("Opcion invalida, intente de nuevo")
