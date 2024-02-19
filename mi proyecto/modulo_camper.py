campers = []

def registrar_camper(nuevocamper):
    
    campers.append(nuevocamper)

def mostrar_campers():
    print("\n================ Lista de Campers =================")
    for camper in campers:
        print("Identificación:", camper["Identificación"])
        print("Nombre:", camper["Nombre"])
        print("Apellidos:", camper["Apellidos"])
        print("Dirección:", camper["Dirección"])
        print("Acudiente:", camper["Acudiente"])
        print("Teléfono Celular:", camper["Teléfono Celular"])
        print("Teléfono Fijo:", camper["Teléfono Fijo"])
        print("Rutas asignadas:", camper["Rutas asignadas"])
        print("Notas:", camper["Notas"])
        print("Estado:", camper["Estado"])
        print("--------------------------")
    print("=====================================================")