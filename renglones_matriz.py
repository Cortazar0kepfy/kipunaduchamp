#Cortázar Tinajero Luis Enrique
import numpy as np
def crear_matriz():
    filar = int(input("Introduce el número de filas: "))
    columnas = int(input("Introduce el numero de columnas: "))
    matriz = []


    print("Introduce los elementos de la matriz, fila por fila:")
    for i in range(filas):
        fila = list(map(float, input(f"Introduce los elementos de la fila {i+1} separados por espacios: ").split()))
        matriz.append(fila)

    return np.array(matriz)

def suma_filas(matriz, fila1, fila2):
    matriz[fila1] += matriz[fila2]


def resta_filas(matriz, fila1, fila2):
    matriz[fila1] -= matriz[fila2]


def multiplicar_fila(matriz, fila, escalar):
    matriz[fila] *= escalar

def imprimir_matriz(matriz):
    print("Matriz actual: ")
    print(matriz)

def main():
    matriz = crear_matriz()
    imprimir_matriz(matriz)

    #Comienzo del while"

    while True:
        print("\nOperaciones disponibles:")
        print("1.Sumar filas")
        print("2. Restar filas")
        print("3. Multiplicar fila por escalar")
        print("4. salir caguamito")


        opcion = int(input("Selecciona una operación: "))


        if opcion == 1:
            fila1 = int(input("Introduce el índice de la primera fila: "))

            fila2 = int(input("Introduce el índice de la segunda fila: "))
        elif opcion ==2:
            fila1 = int(input("Introduce el índice de la primera fila: "))
            fila2 = int(input("Introduce el índice de la segunda fila: "))
            resta_filas(matriz, fila1, fila2)
            imprimir_matriz(matriz)
        
        elif opcion == 3:
            fila = int(input("Introduce el índice de la fila: "))
            escalar = float(input("Introduce el escalar: "))
            multiplicar_fila(matriz, fila , escalar)
            imprimir_matriz(matriz)
        
        elif opcion == 4:
            break
        else:
            print("Opcion no válida, Por favor, intenta de nuevo.")

    

if __name__ == "__main__":
    main()

