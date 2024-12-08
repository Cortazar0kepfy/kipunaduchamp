#Cortázar Tinajero Luis Enrique.....


def buble_sort(arr):
    n = len(arr)
    #Recorre todos los elementosdel arreglo
    for i in range(n):
        #Últimos i elementos ya están en su lugar
        for j i range(0, n-i-1):
            #Intercambiar si el elemento encontrado es mayor
            # que el siguiente elemento
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
#Prueba del algoritmo:

arr = [64, 34, 25, 12, 22, 11, 90]
print("Arreglo original: ")
print(arr)


bubble_sort(arr)
print("Arreglo ordenado: ")
print(arr)

