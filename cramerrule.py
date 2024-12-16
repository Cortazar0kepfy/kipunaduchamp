#Cortázar Tinajero Luis Enrique 
#Metodo de Cramer para sistemas de ecuaciones asignado a un curso mutante de python-lineal.


#Preparamos los objetos matemáticos(utilizando numpy-)

import numpy as np


def determinante(matriz):
    return np.linalg.det(matriz)

# . .    .    .    .  . . . . . . . .  . . .  . . . . ..  . .. # . . . . . . . . . 


def regla_de_cramer(matriz, vector):
    n = len(vector)
    det_matriz = determinate(matriz)
    soluciones = []
    for i in range(n):
        matriz_modificada = matriz.copy()
        matriz_modificada[:, i] = vector
        det_modificada = determinante(matriz_modificada)
        soluciones.append(det_modificada / det_matriz)
        return soluciones
# Ejemplo ilustrativo . . .  . . .   . .      . .... .  
A = np.array([
    [2,3, -1],
    [4,-1,6],
    [-3,2,3]
    ])


b = np.array([5, 10, -1])

             
soluciones = regla_de_cramer(A, b)
print("Soluciones del sistema por Cramer: ", soluciones)



            
