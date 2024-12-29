#Cortázar Tinajero Luis Enrique..


#Manejo de archivos...

#Escribir un archivo
with open("archivo.txt", "w") as archivo:
    archivo.write("hola, Pedro !")
"""leer archivo
"""
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)



"""MÓDULOS Y LIBRERIAS
"""
"""Importar y utilizar estándar de python:
"""
import math
#Usar una función del módulo math
raiz_cuadrada = math.sqrt(16)
print(raiz_cuadrada)

import datetime
"""Usar el modulo datetime para obtener la fecha y hora actual
"""
sakaelsake = datetime.datetime.now()
print(sakaelsake)


