# ACT 1
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Ambos números son pares")
else:
    print("Uno o ambos números son impares")


# ACT 2
num1 = int(input("Ingrese un número: "))

if num1 % 2 == 0:
    if num1 % 3 == 0 and num1 % 5 == 0:
        print("Es par y divisible por 3 y 5")
    else:
        print("Es par pero no divisible por 3 y 5")
else:
    print("No es par")


# ACT 3
numero = int(input("Ingrese un número: "))

if numero > 0:
    if numero % 2 == 0:
        print("El número es positivo y par")
    else:
        print("El número es positivo pero impar")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es 0")


# ACT 4
numero = int(input("Ingrese un número: "))

if numero > 0:
    print("El número es positivo")
else:
    print("El número no es positivo")