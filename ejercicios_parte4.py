# ACT 1
while True:
    n = int(input("Ingrese un número positivo (0 para salir): "))
    
    if n == 0:
        break
    
    for i in range(1, 11):
        resultado = n * i
        print(f"{i} x {n} = {resultado}")


# ACT 2
nombres = input("Ingrese una lista de nombres: ").split()

for i, n in enumerate(nombres):
    print(f"Nombre {i+1}: {n}")


# ACT 3
palabra = input("Ingrese una palabra: ")
vocales = "aeiouAEIOU"
contador_de_vocales = 0

for letra in palabra:
    if letra in vocales:
        contador_de_vocales += 1

if contador_de_vocales == 0:
    print("La palabra no contiene vocales")
else:
    print(f"La palabra tiene {contador_de_vocales} vocales")


# ACT 4
palabras = input("Ingrese palabras: ").split()

for palabra in palabras:
    if palabra == "salir":
        break
    elif palabra == "omitir":
        continue
    else:
        print(palabra)
else:
    print("No se encontró la palabra 'salir'")


# ACT 5
inventario = {}
num_producto = int(input("Ingrese la cantidad de productos: "))

for i in range(num_producto):
    nombre = input("Ingrese un producto: ")
    cantidad = int(input(f"Ingrese la cantidad de {nombre}: "))
    inventario[nombre] = cantidad

print("\nInventario:")
total_productos = 0

for producto, cantidad in inventario.items():
    print(f"{producto}: {cantidad}")
    total_productos += cantidad

print(f"\nEl total del inventario es: {total_productos}")