# Actividad 4.2 - Agenda de contactos
agenda = []

def agregar_contacto():
    nombre = input("Nombre: ")
    telefono = input("Telefono: ")
    email = input("Email: ")
    agenda.append({"nombre": nombre, "telefono": telefono, "email": email})
    print("Contacto agregado!")

def buscar_contacto():
    nombre = input("Nombre a buscar: ")
    for c in agenda:
        if c["nombre"].lower() == nombre.lower():
            print(f"Encontrado: {c}")
            return
    print("No encontrado")

def eliminar_contacto():
    nombre = input("Nombre a eliminar: ")
    for c in agenda:
        if c["nombre"].lower() == nombre.lower():
            agenda.remove(c)
            print("Eliminado")
            return
    print("No existe")

def listar_contactos():
    if not agenda:
        print("Agenda vacia")
    else:
        for c in agenda:
            print(f"{c['nombre']} - {c['telefono']} - {c['email']}")

# Menu simple
while True:
    print("\n1.Agregar 2.Buscar 3.Eliminar 4.Listar 5.Salir")
    op = input("Opcion: ")
    if op == "1": agregar_contacto()
    elif op == "2": buscar_contacto()
    elif op == "3": eliminar_contacto()
    elif op == "4": listar_contactos()
    elif op == "5": break