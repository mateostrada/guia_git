#modulo 2 
# ACT 1
nombres = input("Ingrese nombres separados por comas: ")

conjunto = set(nombres.split(","))
cantidad = len(conjunto)

print(f"Los nombres son {conjunto} y la cantidad de nombres únicos es {cantidad}")


# ACT 2
inventario = {
    "Manzanas": 50,
    "Bananas": 30,
    "Peras": 40
}

producto_nuevo = input("Agregue el nuevo producto: ")
cantidad_nueva = int(input("Ingrese la cantidad: "))
inventario[producto_nuevo] = cantidad_nueva

producto_existente = input("Ingrese producto existente: ")
nueva_cantidad = int(input(f"Ingrese nueva cantidad de {producto_existente}: "))
inventario[producto_existente] = nueva_cantidad

print(inventario)


# ACT 3
oracion = input("Agregá tu oración: ")

en_mayuscula = oracion.upper()
cantidad_python = oracion.count("python")
sin_espacios = oracion.strip()

print(f"La oración es: {oracion}")
print(f"En mayúscula: {en_mayuscula}")
print(f"'python' aparece {cantidad_python} veces")
print(f"Sin espacios: {sin_espacios}")


# ACT 4
a = set(input("Ingrese números separados por coma: ").split(","))
b = set(input("Ingrese números separados por coma: ").split(","))

print("Unión:", a | b)
print("Intersección:", a & b)