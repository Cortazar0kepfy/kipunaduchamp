//Cortázar Tinajero Luis Enrique.
//
//
//
// DE la idea de horner binario. Para la potencia 300:


#include <iostream>

double hornerBinarioContando(double x, unsigned int n, int& mults) {
    double resultado = 1.0;
    double base = x;
    mults = 0;

    while (n > 0) {
        if (n & 1) {
            resultado *= base;
            mults++;
        }
        base *= base;
        mults++;
        n >>= 1;
    }
    return resultado;
}

int main() {
    double x = 2;
    unsigned int n = 300;
    int mults = 0;

    double r = hornerBinarioContando(x, n, mults);
    std::cout << "x^300 = " << r << std::endl;
    std::cout << "Multiplicaciones: " << mults << std::endl;
    return 0;
}
