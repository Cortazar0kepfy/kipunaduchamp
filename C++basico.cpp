//Cortázar Tinajero Luis Enrique


//función para calcular el promedio de un arreglo de calificaciones
float calcularPromedio(int calificaciones[], int tamaño) {
	int suma = 0;
	for (int i = 0; i < tamaño; i++) {
		suma += calificaciones[i];
	}
	return static_cast<float>(suma) / tamaño;
}

//Arreglo de calificaciones........
//.
int main() {
	//Arreys
	int calificaciones[] = {85,90,78,92,88};
	int tamaño = sizeof(calificaciones) / sizeof(calificaciones[0]);
//Calcular el promedio
	float promedio = calcularPromedio(calificaciones, tamaño);
	//Mostrar el promedio..
	std::cout <<"El promedio de las calificaciones es: "<<promedio << std::endl;
	
	return 0;
}

