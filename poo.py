#Cortázar Tinajero Luis Enrique

"""Esté  programa de práctica para establecer los conocimientos básicos
"""
class Persona:
    def __init__(self, nombre, edad, peso, color):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.color = color

    def saludar(self):
        print(f"HOLA Nene mi nombre es {self.nombre}, tengo {self.edad}, peso {self.peso} y soy {self.color}")

# Crear una instancia de la clase Persona
persona = Persona("Cj", 29, "80kg", "Negro")

# Llamar al método saludar
persona.saludar()

kei = ("Te ando ofreciendo un auto para que subas a las chicas")
print(kei)


class Vehiculo:
    def __init__(self, marca, modelo, año, color, tipo_combustible, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.tipo_combustible = tipo_combustible
        self.kilometraje = kilometraje

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año de lanzamiento: {self.año}")
        print(f"Color del mamalón: {self.color}")
        print(f"Combustible mamalón del: {self.tipo_combustible}")
        print(f"Te manda a volar a: {self.kilometraje} km")

    def conducir(self, distancia):
        self.kilometraje += distancia
        print(f"Has conducido: {distancia} km. Nuevo kilometraje: {self.kilometraje} km")

# Crear una instancia de la clase Vehiculo
mi_auto = Vehiculo("Eléctrico", "Lasobas", 2025, "Azul", "Electricidad", 1500)

# Mostrar información del vehículo
mi_auto.mostrar_informacion()

# Conducir el vehículo
mi_auto.conducir(100)

