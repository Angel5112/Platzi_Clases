# Inheritance o herencia es basicamente el darle a una subclase los atributos y metodos de una superclase

# Clase Padre = Superclase

class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def find_area(self):
        return self.base * self.altura


# Clase Hijo = Subclase de Rectangulo (Clase Padre)

class Cuadrado(Rectangulo):
    
    def __init__(self, lado):
        super().__init__(lado, lado)      # super() crea una referencia directa al constructor de la Clase Padre

    # Se debe adaptar a los parametros de la Superclase


if __name__ == '__main__':
    
    base, height = input("Enter the base and height of the rectangle: ").split()
    base, height = int(base), int(height)

    lado = int(input("Enter the side of the square: "))

    rectangle = Rectangulo(base, height)
    square = Cuadrado(lado)

    print(f"The Area of the Rectangle and Square are {rectangle.find_area()} and {square.find_area()}")

