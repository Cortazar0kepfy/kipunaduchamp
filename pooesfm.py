#Cortázar Tinajero Luis Enrique

"""Programación Orientada de Objetos
"""


""" Se basa en objetos que contienen datos y métodos para operar sobre estos datos
"""

#El ejemplo es la definición de clase(python) y de la
# creación de instancias de objetos

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad



    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")


persona = Persona("Alice", 30)
persona.saludar()

class Persona:
    def __init__(self, nombre, edad, estatura):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura

    def saludar(self):
        print(f"hola, mi nombre es {self.nombre} y tengo {self.edad} y mido {self.estatura} cm. ")
ppesona = Persona("Roberto", 30, 1.67)
ppesona.saludar()

