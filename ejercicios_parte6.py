# ACT 1
ciudades_info = {
    'Paris': {
        'Pais': 'Francia',
        'Poblacion': 2187526,
        'Puntos_de_Interes': ['Torre Eiffel', 'Louvre', 'Catedral de Notre-Dame']
    },
    'Nueva York': {
        'Pais': 'Estados Unidos',
        'Poblacion': 8398748,
        'Puntos_de_Interes': ['Estatua de la Libertad', 'Central Park', 'Times Square']
    },
    'Tokio': {
        'Pais': 'Japón',
        'Poblacion': 13929286,
        'Puntos_de_Interes': ['Torre de Tokio', 'Templo Senso-ji', 'Palacio Imperial']
    }
}

ciudad = input("Ingrese la ciudad buscada: ")

try:
    informacion = ciudades_info[ciudad]
    print(f"Información sobre {ciudad}")
    print(f"País: {informacion['Pais']}")
    print(f"Población: {informacion['Poblacion']}")
    print(f"Puntos de interés: {', '.join(informacion['Puntos_de_Interes'])}")
except KeyError:
    print(f"No se encontró la ciudad {ciudad}")


# ACT 2
try:
    edad = int(input("Ingrese su edad: "))
    if edad <= 0:
        raise ValueError("La edad debe ser positiva")
    print("Edad ingresada correctamente")
except TypeError:
    print("Se esperaba un número")
except ValueError as e:
    print(f"Error: {e}")
except:
    print("Error desconocido")


# ACT 3
try:
    descuentos_validos = ["DESC10", "DESC20", "DESC30"]
    
    precio = int(input("Ingrese un precio: "))
    cupon = input("Ingrese cupón: ")

    if precio <= 0:
        raise ValueError("El precio debe ser positivo")
    
    if cupon not in descuentos_validos:
        raise ValueError("El cupón no es válido")

    if cupon == "DESC10":
        precio_descuento = precio * 0.9
    elif cupon == "DESC20":
        precio_descuento = precio * 0.8
    else:
        precio_descuento = precio * 0.7

    print(f"El precio con descuento es: {precio_descuento}")

except ValueError as ve:
    print(f"Error de valor: {ve}")
except TypeError:
    print("Error: entrada no válida")
except Exception as e:
    print(f"Error desconocido: {e}")