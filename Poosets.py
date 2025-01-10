#Cortázar Tinajero Luis Enrique 


#LMA

#  



#


"""Con el objetivo de profundizar en la programación
y el álgebra de Cantor-Dedekin...
"""

"""Este programa pretende dar las operaciones entre conjuntos
mediante una clase Set''''''
"""

class Conjunto:
    def __init__(self, elementos):
        self.elementos = set(elementos)

    def union(self, otro_conjunto):
        return Conjunto(self.elementos | otro_conjunto.elementos)

    def interseccion(self, otro_conjunto):
        return Conjunto(self.elementos & otro_conjunto.elementos)

    def diferencia(self, otro_conjunto):
        return Conjunto(self.elementos - otro_conjunto.elementos)

    def __str__(self):
        return f"{{ {', '.join(map(str, self.elementos))} }}"

# Ejemplo de uso:
conjunto1 = Conjunto([1, 2, 3, 4])
conjunto2 = Conjunto([3, 4, 5, 6])

print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)

union = conjunto1.union(conjunto2)
print("Unión:", union)

interseccion = conjunto1.interseccion(conjunto2)
print("Intersección:", interseccion)

diferencia = conjunto1.diferencia(conjunto2)
print("Diferencia:", diferencia)

