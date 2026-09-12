//Cortázar Tinajero Luis Enrique
//
//
//
// Vamos a desarrollar el código para la potencia 15:
// Es decir:
#include <iostream>

double potencia15Contando(double x, int& mults) {
    mults = 0;

    double x2  = x * x;      mults++;   // 1 → x^2
    double x3  = x2 * x;     mults++;   // 2 → x^3
    double x6  = x3 * x3;    mults++;   // 3 → x^6
    double x12 = x6 * x6;    mults++;   // 4 → x^12
    double x15 = x12 * x3;   mults++;   // 5 → x^15

    return x15;
}

int main() {
    double x = 2;
    int mults = 0;

    double r = potencia15Contando(x, mults);

    std::cout << "x^15 = " << r << std::endl;
    std::cout << "Multiplicaciones: " << mults << std::endl;

    return 0;
}
