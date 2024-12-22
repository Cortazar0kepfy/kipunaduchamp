#Cortázar Tinajero Luis Enrique......


#Función para dividr dos números con manejo de errores.
def dividir(numerador, denominador):
    try:
        #Intentamos realizar la division
        resultado = numerador / denominador
    except ZeroDivisionError:
        return "Error: División por cero no permitida. "
    except TypeError:
        return "Error: Las entradas deben ser números. "
    else:
        return f"El resultdo es : {resultado}"
    finally:
        print("Ejecución del bloque finally. ")
        

print(dividir(10, 2)) #Caso normal
print(dividir(10, 0)) #División por cero.
print(dividir(10, "a")) #Entrada de un string.

