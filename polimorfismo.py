#Cortázar Tinajero Luis Enrique

#El polimorfismo en Programación Orientada a Objetos:
# es un principio fundamental que permite que objetos
#   de difefentes clases sean tratados como objetos de una
#   clase en común.

"""Imagina que tienes una clase base llamada Animal que tiene un método hacer_sonido(). Luego creas diferentes clases que heredan de Animal y cada una implementa su propia versión de 
hacer sonido.
"""

class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Este método deber ser implementado por la subclse")


class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

"""Aqui, Perro y Gato son clases que heredan de Animal y cada una implementa su propio sonido.El polimorfismo permite que
trates a estos objetos de manera uniforme a través de la clase
base Animal
"""

