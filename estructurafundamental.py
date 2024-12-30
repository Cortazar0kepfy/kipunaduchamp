#Cortázar Tinajero Luis Enrique


#Imprimir un mensaje (similar al comando unix 'echo' )

print("Hola estudiantes de la Escuela Superior de Física y matemática")
#Variables y tipos de datos   



#pues   de 01_pytonbasico.py
#Para saber el tipo de objeto que tenemos:

y = 0
print(type(y))


x =("hola")
print(type(x))


e = 4.555545453251151
print(type(e))


import math 

def resolver_ecuacion_cuadratica(a, b, c):
    discriminante = b**2-4*a*c
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return (x1, x2)
    elif discriminante == 0:
        x = -b / (2*a)
        return (x,)
    else:
        x1 = (-b + cmath.sqrt(discriminante)) / (2*a)
        x2 = (-b - cmath.sqrt(discriminante)) / (2*a)
        return (x1, x2)

a = 9
b = 81
c = 6
soluciones = resolver_ecuacion_cuadratica(a, b, c)
print("Las soluciones son:", soluciones)




