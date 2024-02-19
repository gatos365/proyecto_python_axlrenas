notas = []

def menu_coordinador(camper, cambiar_estado, colocar_notas):
    print("\n============== Menú del coordinador ===============")
    print("*                                                    =")
    print("*              1. Colocar notas del camper           =")
    print("*              2. Cambiar estado del camper          =")
    print("*              3. Asignar salon al camper            =")
    print("*              4. Salir                              =")
    print("=====================================================")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        colocar_notas(camper)
    elif opcion == "2":
        cambiar_estado(camper)


def colocar_notas(camper):
    notas_camper = input("Ingrese las notas del camper: ")
    notas.append({"Identificación": camper["Identificación"], "Notas": notas_camper})
    print("Notas registradas con éxito.")

def cambiar_estado(camper):
    nuevo_estado = input("Ingrese el nuevo estado del camper (en proceso de ingreso, inscrito, aprobado, cursando, graduado, expulsado, retirado): ")
    camper["Estado"] = nuevo_estado
    print("Estado del camper actualizado con éxito.")