//Cortázar Tinajero Luis Enrique.





    


#include <stdio.h> // Incluye la librería estándar de entrada y salida

int main() { // Define la función principal donde inicia la ejecución del programa
    int filas, columnas; // Declara variables para almacenar el número de filas y columnas de las matrices
    printf("Introduce el número de filas y columnas: "); // Imprime un mensaje solicitando el número de filas y columnas
    scanf("%d %d", &filas, &columnas); // Lee el número de filas y columnas ingresado por el usuario

    int matriz1[filas][columnas], matriz2[filas][columnas], suma[filas][columnas]; // Declara tres matrices de las dimensiones especificadas

    printf("Introduce los elementos de la primera matriz:\n"); // Imprime un mensaje solicitando los elementos de la primera matriz
    for (int i = 0; i < filas; i++) { // Itera a través de las filas
        for (int j = 0; j < columnas; j++) { // Itera a través de las columnas
            scanf("%d", &matriz1[i][j]); // Lee cada elemento de la primera matriz
        }
    }

    printf("Introduce los elementos de la segunda matriz:\n"); // Imprime un mensaje solicitando los elementos de la segunda matriz
    for (int i = 0; i < filas; i++) { // Itera a través de las filas
        for (int j = 0; j < columnas; j++) { // Itera a través de las columnas
            scanf("%d", &matriz2[i][j]); // Lee cada elemento de la segunda matriz
        }
    }

    for (int i = 0; i < filas; i++) { // Itera a través de las filas
        for (int j = 0; j < columnas; j++) { // Itera a través de las columnas
            suma[i][j] = matriz1[i][j] + matriz2[i][j]; // Suma los elementos correspondientes de las dos matrices y almacena el resultado en la matriz suma
        }
    }

    printf("La suma de las matrices es:\n"); // Imprime un mensaje indicando que se mostrará la suma de las matrices
    for (int i = 0; i < filas; i++) { // Itera a través de las filas
        for (int j = 0; j < columnas; j++) { // Itera a través de las columnas
            printf("%d ", suma[i][j]); // Imprime cada elemento de la matriz suma
        }
        printf("\n"); // Imprime un salto de línea al final de cada fila
    }

    return 0; // Indica que el programa terminó correctamente
}                                                                                                                                                                                                                        

