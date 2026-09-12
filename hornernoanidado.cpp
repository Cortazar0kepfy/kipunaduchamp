// Cortázar Tinajero Luis Enrique.......()()()(()()()()()(()()()()()()()()()()()()()()()()()()()(
//
//
//

#include <iostream>
#include <cmath>  // para std::pow

double evaluarDirecto(double x) {
    return 2 * std::pow(x, 3) - 6 * std::pow(x, 2) + 2 * x - 1;
}

int main() {
    double xVal = 3;
    std::cout << "El resultado es: " << evaluarDirecto(xVal) << std::endl;
    return 0;
}

