import json
import modulo_camper
import modulo_coordinador

# Función para cargar la información de los salones desde un archivo JSON
def cargar_salones():
    global salones
    with open("salones.json", "r") as file:
        salones = json.load(file)
    return salones

# Función para guardar la información de los salones en un archivo JSON
def guardar_salones(salones):
    with open("salones.json", "w") as file:
        json.dump(salones, file)

# Función para mostrar el menú principal
def menu_principal():
    print("******************** Menu camper ********************")
    print("*           1. Registrar camper                      *")
    print("*           2. Mostrar la información                *")
    print("*           3. Modificar tu información              *")
    print("*           4. Salir del menú del camper             *")
    print("******************************************************")
    print("")

    opcion = input("Seleccione una opción: ")
    return opcion

# Función para manejar las opciones del menú
def manejar_opcion(opcion):
    if opcion == "1":
        nuevo_camper = pedir_camper()
        modulo_camper.registrar_camper(nuevo_camper)
        modulo_coordinador.menu_coordinador(nuevo_camper, cambiar_estado, colocar_notas)
    elif opcion == "2":
        print("llegue hasta aqui")
        modulo_camper.mostrar_campers()
        print("se debio mostrar la info")
    elif opcion == "3":
        pass
    elif opcion == "4":
        modulo_coordinador.menu_coordinador()
    else:
        print("Opción inválida. Por favor intente de nuevo.")

# Función para manejar las opciones del menú del coordinador
def menu_coordinador(camper, cambiar_estado, colocar_notas):
    print("\n============== Menú del coordinador ===============")
    print("*                                                    *")
    print("*              1. Colocar notas del camper           *")
    print("*              2. Cambiar estado del camper          *")
    print("*              3. Asignar salon al camper            *")
    print("*              4. Salir                              *")
    print("=====================================================")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        colocar_notas(camper)
    elif opcion == "2":
        cambiar_estado(camper)

# Función para colocar notas de un camper
def colocar_notas(camper):
    notas_camper = input("Ingrese las notas del camper: ")
    camper["Notas"] = notas_camper
    print("Notas registradas con éxito.")

# Función para cambiar el estado de un camper
def cambiar_estado(camper):
    nuevo_estado = input("Ingrese el nuevo estado del camper: en proceso de ingreso, inscrito, aprobado, cursando, graduado, expulsado, retirado: ")
    camper["Estado"] = nuevo_estado
    print("Estado del camper actualizado con éxito.")

def pedir_camper():
    nombres = input("Ingrese los nombre: ")
    apellidos = input("Ingrese los apellidos: ")
    num_identificacion = input("Ingrese el numero de documento: ")
    direccion = input("Ingrese la dirección: ")
    Acudiente = input("Ingrese el acudiente: ")
    Telefono_celular = input("Ingrese el numero del celular: ")
    Telefono_fijo = input("Ingrese el numero del fijo: ")

    nuevo_camper = {
        "Identificación": num_identificacion,
        "Nombre": nombres,
        "Apellidos": apellidos,
        "Dirección": direccion,
        "Acudiente": Acudiente,
        "Teléfono Celular": Telefono_celular,
        "Teléfono Fijo": Telefono_fijo,
        "Rutas asignadas": " ",
        "Notas": " ",
        "Estado": " ",
    }

    return nuevo_camper

# Función para ejecutar el menú principal
while True:
    opcion = menu_principal()
    manejar_opcion(opcion)
    if opcion == "4":
        break

# Llamar función del menú del coordinador
modulo_coordinador.menu_coordinador()