from abc import ABC , abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

class Circulo(Figura):
    def area(self):
        print (3.14 * (20 **2))

class Rectangulo(Figura):
    def area(self):
        print(10 * 15)

def mostrar_area(area_figura):
    area_figura.area()

circulo = Circulo()
rectangulo = Rectangulo()

mostrar_area(circulo)
mostrar_area(rectangulo)

'''
Crea una clase abstracta Figura con el siguiente método abstracto:

area(): que debe devolver el área de la figura.
Crea dos subclases Círculo y Rectángulo que hereden de Figura y sobrescriban el método area():

Círculo: Usa la fórmula π * radio^2 para calcular el área.
Rectángulo: Usa la fórmula base * altura para calcular el área.
Crea un método mostrar_area() que reciba un objeto de la clase Figura y llame al método area() para imprimir el área de la figura.

'''
