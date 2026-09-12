// Cortázar Tinajero Luis Enrique.
//
//
//
// Partiendo del ordenamiento bubble sort, al mejorar la cantidad de pasos para ordenar. Sea el arreglo :
// [8,5,1,9,3]......ejemplo de la clase.
#include <iostream>
#include <vector>

using namespace std;

// Función auxiliar para imprimir un vector
void imprimir(const vector<int>& A) {
    cout << "[ ";
    for (int x : A) cout << x << " ";
    cout << "]";
}

void insertionSortPasoAPaso(vector<int> A) {
    int n = A.size();
    
    cout << "Arreglo original: ";
    imprimir(A);
    cout << "\n\n";
    
    // Empezamos desde j = 1 (segundo elemento, índice 0 en C++)
    for (int j = 1; j < n; j++) {
        int key = A[j];      // La "llave" o elemento a insertar
        int i = j - 1;       // Índice del último elemento del subarreglo ordenado
        
        // Mostrar el estado ANTES de insertar
        cout << "--- Iteracion j=" << j << " ---\n";
        cout << "Key a insertar: " << key << "\n";
        
        // Bucle interno: desplazar elementos mayores que key hacia la derecha
        while (i >= 0 && A[i] > key) {
            A[i + 1] = A[i];
            i--;
        }
        
        // Insertar la key en su posición correcta
        A[i + 1] = key;
        
        // Mostrar el estado DESPUÉS de insertar
        cout << "Subarreglo ordenado despues: ";
        imprimir(vector<int>(A.begin(), A.begin() + j + 1));
        cout << "\nEstado actual del arreglo: ";
        imprimir(A);
        cout << "\n\n";
    }
}

int main() {
    // Ejemplo exacto de la pizarra
    vector<int> arreglo = {8, 5, 1, 9, 2, 3};
    
    insertionSortPasoAPaso(arreglo);
    
    return 0;
}
