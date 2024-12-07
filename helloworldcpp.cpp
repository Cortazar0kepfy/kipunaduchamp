#include <iostream>
#include <string>

// Función para saludar
void saludar(const std::string& nombre){

    std::cout << "Hola, " << nombre << "!" << std::endl;
}

int main()
{
    // Variables
    int edad = 25;
    std::string nombre = "Juan";
    saludar(nombre);

    if (edad >= 18) {
        std::cout << "Eres mayor de edad." << std::endl;
    } else {
        std::cout << "Eres menor de edad." << std::endl;
    }

    // Bucle
    for (int i = 0; i < 5; i++) {
        std::cout << "Iteración " << i << std::endl;
    }

    int notas[] = {10, 20, 30, 40, 50};
    for (int i = 0; i < 5; i++) {
        std::cout << "Nota " << i << ": " << notas[i] << std::endl;
    }

    return 0;
}





