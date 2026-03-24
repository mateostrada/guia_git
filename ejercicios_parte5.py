# ACT 1
def agregar_tarea(tareas, tarea):
    tareas.append(tarea)

def marcar_completada(tareas, indice):
    if 0 <= indice < len(tareas):
        tareas[indice] = "✓ " + tareas[indice]

def listar_tareas(tareas):
    for i, tarea in enumerate(tareas):
        print(f"{i + 1}. {tarea}")

tareas_pendientes = []

while True:
    print("\n1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Listar tareas")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        tarea = input("Ingresa la tarea: ")
        agregar_tarea(tareas_pendientes, tarea)
    elif opcion == "2":
        listar_tareas(tareas_pendientes)
        indice = int(input("Número de tarea: ")) - 1
        marcar_completada(tareas_pendientes, indice)
    elif opcion == "3":
        listar_tareas(tareas_pendientes)
    elif opcion == "4":
        break


# ACT 2
def agregar_contacto(agenda, nombre, telefono, correo):
    agenda[nombre] = {"telefono": telefono, "correo": correo}

def buscar_contacto(agenda, criterio):
    for nombre, info in agenda.items():
        if criterio in nombre or criterio == info["telefono"]:
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {info['telefono']}")
            print(f"Correo: {info['correo']}")

agenda = {}

while True:
    print("\n1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")
        agregar_contacto(agenda, nombre, telefono, correo)
    elif opcion == "2":
        criterio = input("Buscar por nombre o teléfono: ")
        buscar_contacto(agenda, criterio)
    elif opcion == "3":
        break