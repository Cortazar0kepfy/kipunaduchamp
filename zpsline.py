#Cortázar Tinajero Luis Enrique.


"""Se presenta un código cuyo objetivo es mostrar un el funcionamiento de la libreria numpy..
"""


import numpy as np
from Curva import Curva
"""Se presenta la libreria matplotlib.pyplot
"""
import math
#Conjunto de puntossssss
#....................
nump:np.int32 = 8
#Memoria para puntos...




puntos = np.zeros(dim*nump,dtype=np.float64)





# Parametrizaciónnnnnnnnnn
X =np.linspace(0.0,2.0*np.pi,nump+1)

#Genera valores equidistantes.......

"""Genera nump+1 puntos equidistantes en el intervalo[0,2pi[0, 2/pi].
"""
#Matematicamente significa que divide al intervalo.
"""[0, 2pi][0. 2/pi]
en partes iguales
"""


#Caracterizando la coordenada x:
puntos[0:nump] = np.cos(X[0:nump]) + 0.0*np.sin(2*X[0:nump])
#Caracterizando a la coordenada y:
puntos[nump:2*nump] = np.sin(X[0:nump]) + 0.0*np.sin(2*X[0:nump])

