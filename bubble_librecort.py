#Cortázar Tinajero luis Enrique.......
# El mismo bubbleSort pero ahora con la libertad divina de escoger la cantidad n elementos que se desee ordenar


#Tomate la libertad de ordenar lo que quieras :

def bubble_sort(arr):
    n = len(arr)

    #Recorre todos los elementos del arreglo
    for i in range(n):
        #últimos i elementos ya están en su lugar
        for j in range(0, n-1-1):
            #Intercambiar si el elemento encontrado es mayor
            # que el siguiente elemneto
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

#Función para ingresar un arreglo desde el usuario "x"
# . . . . . . . 


def ingresar_arreglo():
    arr = []
    print("Introduce los elementos del arreglo, separados por espacios: ")
    entrada = input()
    arr = list(map(int, entrada.split()))
    return arr

#Prueba del algoritmo con arreglo ingresado por el usuario
arreglo_usuario = ingresar_arreglo()
print("Arreglo original: ")
print(arreglo_usuario)

bubble_sort(arreglo_usuario)
print("Arreglo Ordenado: ")
print(arreglo_usuario)
