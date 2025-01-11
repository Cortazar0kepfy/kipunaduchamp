import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def circunferencia(self):
        return 2 * math.pi * self.radio

# Uso de la clase
circulo1 = Circulo(5)
print(f"Área: {circulo1.area()}")
print(f"Circunferencia: {circulo1.circunferencia()}")


"""Cortázar Tinajero Luis Enrique
"""

