#Cortázar Tinajero Luis Enrique

#Paradigmas de la programación en python

"""Programación Imperativa
"""

""" Descripción: Se basa en comandos o declaraciones que cambian el estado del programa
"""
#El mejor ejemplo el es uso de búcles y asignaciones de variables

suma = 0
for i in range(1, 6):
    suma += i
print(suma)




#Programación Funcional:
""" Se basa en funciones puras y evita el estado mutable y los efectos secundarios}
"""
#El ejemplo es el uso de funciones de orden superior, como map filter y reduce.

from functools import reduce
numeros = [1, 2, 3, 4, 5]
suma = reduce(lambda x, y: x + y, numeros)
print(suma)

