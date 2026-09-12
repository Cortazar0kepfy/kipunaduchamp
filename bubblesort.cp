#Cortázar Tinajero Luis Enrique

#include <iostream>
using namespace std;

void bubbleSort(int A[], int n) {
    // n-1 pasadas como máximo
    for (int i = 0; i < n - 1; i++) {
        // Recorre desde 0 hasta n-i-2
        for (int j = 0; j < n - i - 1; j++) {
            // Compara elementos adyacentes
            if (A[j] > A[j + 1]) {
                // Intercambio manual
                int temp = A[j];
                A[j] = A[j + 1];
                A[j + 1] = temp;
            }
        }
    }
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);

    bubbleSort(arr, n);

    cout << "Arreglo ordenado: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;

    return 0;
}
