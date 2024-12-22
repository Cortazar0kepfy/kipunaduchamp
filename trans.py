#Cortaza Tinajero Luis Enrique
import numpy as np
import matplotlib.pyplot as plt


#Definir una matriz de transformación
A = np.array([
    [2, 0],
    [0, 3]
])
vectors = np.array([[1, 1], [-1, 2], [3, -2]])



#Aplicar la transformación
transformed_vectors = np.dot(vectors, A.T)

#Crear una función para dibujar vectores desde el origen
def plot_vectors(vectors, color, label):
    for vector in vectors:
        plt.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color=color, label=label)
        label = None

plot_vectors(vectors, color= 'r', label='Originals')
plot_vectors(transformed_vectors, color= 'b', label='Transformados')

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='grey', lw=0.5)
plt.axvline(0, color='grey', lw=0.5)
plt.grid()
plt.legend()
plt.show()
