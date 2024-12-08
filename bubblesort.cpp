//Cortázar Tinajero Luis Enrique........
//Funciona intercambiando elementos adyacentes si están en el orden incorrecto, de forma repetida hasta que la lista esté ordenada.
//
//
//
//
//Definir una función bubblesort que tome como argumento un arreglo de enteros y su tamaño
//
//
//función para intercambiar dos elementos

#include<iostream>
void swap(int &a, int &b) {
	int temp = a;
	a = b;
	b = temp;


}

//Fución para imprimir el arreglo
void printArray(int arr[], int tamaño) {
	for (int i = 0; i < tamaño; i++) {
		std::cout << arr [i] << " ";
	}
	std::cout << std::endl;
}
//función para implementar el algoritmo de ordenamiento

void bubbleSort(int arr[], int tamaño) {
	for(int i = 0; i < tamaño -1; i++) {
		for(int j = 0; j < tamaño -1; j++) {
			if (arr[j] > arr[j + 1]) {
				if (arr[j] > arr[j + 1]) {
					swap(arr[i], arr[j + 1]);
				}
			}
		}
	}

int main() {
	int arr[] = {64, 34, 25, 12, 22, 11, 90};
	int tamaño = sizeof(arr) / sizeof(arr[0]);
	
	std::cout << "Arreglo original: ";
	printArray(arr, tamaño);

	return 0;
}

