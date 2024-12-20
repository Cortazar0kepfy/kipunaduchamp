#Cortázar Tinajero Luis Enrique.
import numpy as np
import matplotlib.pyplot as plt
#Definir a la matriz..... . . . . . . . . . .. . . . .

A = np.array([
    [2, 0],
    [0, 3]
    ])

#Definimos el vector 
vectors = np.array([[1, 1], [-1, 2], [3, -2]])


#Aplicando la translineal......)=)=)=)=)=)=)=)=)=)=)=)=)=)=)=)=
transformed_vectors = np.dot(vectors, A.T)


#Aplicando la gráfica de los vectores origninales y a transformados

plt.quiver(*vectors.T, angles= 'xy', scale_units='xy', scale=1, color = 'b', label= 'Origninals')
plt.quiver(*transformed_vectors.T, angles= 'xy', scale_units= 'xy', scale=1, color='b', label='Transformados')
plt.xlim(-10, 10)
plt.ylim(-10,10)
plt.axhline(0, color= 'Orange', lw=0.5)
plt.axvline(0, color= 'Black', lw=0.5)
plt.grid()
plt.legend()
plt.show()

