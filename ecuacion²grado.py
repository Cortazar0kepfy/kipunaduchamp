#Cortázar Tinajero Luis Enrique

#Aplicamos la libreria math(importación).
import math

"""La ecuación de segunda grado es concebida y desarrollada a partir
de la ecuación: ax²+bx+c = 0
"""
#Generamos la función para resolver los valores a partir de (a=3, b=3, c =-2)
#Es decir :

def resolver_ecuacion_cuadratica(a,b,c):
    discriminante = b**2-4*a*c
    if discriminante > 0:
        x1 =(-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b -math.sqrt(discriminante)) / (2*a)
        return (x1,x2)
    
    elif discriminante ==0:
        x = -b / (2*a)
        return (x,)
    
    else:
        x1 = (-b + math.sqrt(discriminante * 1j)) / (2*a)
        x2 = (-b - math.sqrt(discriminante * 1j)) / (2*a)
        return (x1, x2)

#Ejemplo de uso:: :: :: :: :: :: :: :: ::
a = 2 
b = 3
c = -2

soluciones = resolver_ecuacion_cuadratica(a, b, c)
print("Las soluciones son: ", soluciones)
# .       .                    .                     . 

#Otro ejercicio de clases:

class Libro:
    def __init__(self, titulo, autor, año_publicacion, genero, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.genero = genero
        self.numero_paginas = numero_paginas

    def mostrar_informacion(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.año_publicacion}")
        print(f"Género: {self.genero}")
        print(f"Número de páginas: {self.numero_paginas}")

    def es_largo(self):
        if self.numero_paginas > 300:
            print(f"El libro '{self.titulo}' es largo rey.")
        else:
            print(f"El libro '{self.titulo}' no es un libro largo.")

# Crear una instancia de la clase Libro
mi_libro = Libro("Pedro Paramo", "Juan Rulfo", "18 de julio de 1995", "Novela", 122)

# Mostrar información del libro
mi_libro.mostrar_informacion()

# Verificar si el libro es largo
mi_libro.es_largo()



