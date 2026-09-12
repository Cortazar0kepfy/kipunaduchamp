// Cortázar Tinajero Luis Enrique.
//
//
//
//
//
#include <iostream>
#include <vector>

/**
 * Evalúa un polinomio usando el esquema de Horner.
 *
 *  Lista de coeficientes [a_n, a_{n-1}, ..., a_1, a_0]
 *  x Valor a evaluar
 *  El resultado numérico de P(x)
 */
double evaluarHorner(const std::vector<double>& coeficientes, double x) {
    double resultado = 0.0;
    for (double coef : coeficientes) {
        resultado = resultado * x + coef;
    }
    return resultado;
}

int main() {
    // Ejemplo de uso:
    // Para evaluar P(x) = 2x^3 - 6x^2 + 2x - 1 en x = 3
    std::vector<double> coefs = {2, -6, 2, -1};
    double xVal = 3;

    double resultado = evaluarHorner(coefs, xVal);
    std::cout << "El resultado es: " << resultado << std::endl;  // Imprime: 5

    return 0;
}
