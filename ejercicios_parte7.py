# ACT 1
class Figura:
    def area(self):
        return "Área de la figura"


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * (self.radio ** 2)


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


c = Circulo(3)
print(f"Área del círculo: {c.area()}")

r = Rectangulo(3, 5)
print(f"Área del rectángulo: {r.area()}")


# ACT 2
class Calculadora:
    @classmethod
    def suma(cls, num1, num2):
        return num1 + num2


print("Suma:", Calculadora.suma(2, 5))


# ACT 3
class Empleado:
    def __init__(self, nombre, apellido, edad, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.salario = salario

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}, Salario: {self.salario}"

    def aumentar_salario(self, porcentaje):
        self.salario += self.salario * (porcentaje / 100)
        return self.salario


class Gerente(Empleado):
    def __init__(self, nombre, apellido, edad, salario, departamento):
        super().__init__(nombre, apellido, edad, salario)
        self.departamento = departamento

    def mostrar_informacion(self):
        return super().mostrar_informacion() + f", Departamento: {self.departamento}"


empleado1 = Empleado("Juan", "García", 45, 100000)
gerente1 = Gerente("Ana", "Pérez", 35, 200000, "Ventas")

print(empleado1.mostrar_informacion())
print(gerente1.mostrar_informacion())

empleado1.aumentar_salario(20)
print(f"Nuevo salario de {empleado1.nombre}: {empleado1.salario}")


# ACT 4
class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.disponible = True


class Biblioteca:
    cantidad_total_libros = 0

    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        Biblioteca.cantidad_total_libros += 1

    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo and libro.disponible:
                libro.disponible = False
                return f"El libro '{titulo}' fue prestado"
        return f"El libro '{titulo}' no está disponible"

    def devolver_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo and not libro.disponible:
                libro.disponible = True
                return f"El libro '{titulo}' fue devuelto"
        return f"No se puede devolver el libro '{titulo}'"

    def mostrar_disponibles(self):
        disponibles = [libro.titulo for libro in self.libros if libro.disponible]
        return f"Libros disponibles: {', '.join(disponibles)}"


libro1 = Libro("El Gran Gatsby", "F. Scott Fitzgerald", 1925)
libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)

biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

print(biblioteca.prestar_libro("El Gran Gatsby"))
print(biblioteca.devolver_libro("El Gran Gatsby"))
print(biblioteca.mostrar_disponibles())


# ACT 5
class Producto:
    def __init__(self, nombre, precio, cantidad_disponible, codigo):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible
        self.codigo = codigo


class CarritoCompras:
    total_productos = 0

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        CarritoCompras.total_productos += 1
        return f"Se agregó {producto.nombre}"

    def eliminar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                self.productos.remove(producto)
                CarritoCompras.total_productos -= 1
                return f"Se eliminó {producto.nombre}"
        return "Producto no encontrado"

    def total_precio(self):
        total = sum(p.precio for p in self.productos)
        return f"Total a pagar: {total}"


p1 = Producto("Laptop", 800, 5, "LP001")
p2 = Producto("Teléfono", 300, 10, "PH002")

carrito = CarritoCompras()
print(carrito.agregar_producto(p1))
print(carrito.agregar_producto(p2))

print(carrito.eliminar_producto("Teléfono"))
print(carrito.total_precio())
print("Cantidad de productos:", CarritoCompras.total_productos)