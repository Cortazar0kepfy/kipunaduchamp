#Cortázar Tinajero Luis Enrique

"""Importando biblioteca de lectura de entes matemáticos
"""

import numpy as np


class Matriz:
    def __init__(self, matriz):
        self.matriz = np.array(matriz)
    
    def suma(self, otra):
        return Matriz(self.matriz + otra.matriz)

    def resta(self, otra):
        return Matriz(self.matriz - otra.matriz)

    def multiplicacion(self, otra):
        return Matriz(np.dot(self.matriz, otra.matriz))
    
    def transposicion(self):
        return Matriz(self.matriz.T)

    def __repr__(self):
        return f'{self.matriz}'
    #Ejemplo de uso........

matriz1 = Matriz([[1,2], [3, 4]])
matriz2 = Matriz([[5,6], [7, 8]])


print("Matriz 1:")
print(matriz1)

print("Matriz 2:")
print(matriz2)

print("Suma:")
print(matriz1.suma(matriz2))

print("Resta:")
print(matriz1.resta(matriz2))

print("Multiplicacion:")
print(matriz1.multiplicacion(matriz2))
print("Transposición de Matriz 1:")
print(matriz1.transposicion())

    
