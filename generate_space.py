#Cortázar Tinajero Luis Enrique
#Esté es un programa para calcular si un determinado,   
#  de vectores generan a un R⁴.

#Abriendo libreria de "Objetos Matemáticos"
import numpy as np
#Definir los vectores como columnas de la matriz
A = np.array([
    [3,1,5,3],
    [1,2,5,1],  
   [1,-1,-1,0],
      [1,1,3,0]
      ])
#Calculando el determinante = np.linalg.det(A)
print("Determinante de la matriz: ", determinante) 

if np.abs(determinante)< 1e-10:
    print("Los vectores No son linealmente independientes y NO generan R⁴.")
else:
    print("Los vectores son linealmente independientes y generan R⁴. ")
    

