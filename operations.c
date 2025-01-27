//Cortázar Tinajero Luis Enrique
//
//
#include <stdio.h>


int main () {
	char operador;
	double primerNumero, segundoNumero;

	printf("Introduce un operador(+, - *, /) : ");
	scanf("%c", &operador);

	printf("Introduce dos numeros: ");
	scanf("%lf %lf",&primerNumero, &segundoNumero);

	switch (operador) {
		case '+':
		 	printf("%.2lf + %.2lf = %.2lf\n", primerNumero, segundoNumero, primerNumero + segundoNumero);
			break;
		case '-':
			printf("%.2lf - %2.lf = %.2lf\n", primerNumero, segundoNumero, primerNumero - segundoNumero);
			break;
		case '*':
			printf("%.2lf * %.2lf = %.2lf\n", primerNumero, segundoNumero, primerNumero*segundoNumero);
			break;
		case '/':
			if (segundoNumero != 0)
				printf("%.2lf / %.2lf = %.2lf\n", primerNumero, segundoNumero, primerNumero / segundoNumero);
			else
				printf("Error!División por cerono es permitida.\n");
			break;
		default:
			printf("Error! Operador no es corecto.\n");
	}
	return 0;
}

