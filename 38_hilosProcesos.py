#Cortázar Tinajero Luis Enrique.

"""Modulo de hilos, procesos, sistema,  matemática y tiempo.
"""

"""Threading.Thread:Para crear hilos
"""
from threading import Thread
from multiprocessing import Process
import os
import math
import time

#=======================================

"""Multiprocessing.Process:Par crear procesos.
"""

#os....  : Para obtener información del sistema, como el número de procesaodres.

"""math:Para realizar cálculos matemáticas.
"""


"""time:Para medir el tiempo de ejecución.
"""

#Función....
"""Esta función simplemente calcula la raíz cuadrada
de números del 0 al 4,000,000.Es un tarea pesada
pero que sirve para medir el rendimiento
de los hilos y procesos.
"""

def calc():
    for i in range(0,4000000):
        math.sqrt(i)

    

#Lista de hilos

threads = []

#Procesadores en mi máquina.
cpus = os.cpu_count()
print("Número de procesadores: ", cpus)
#Inscribir hilos en la lista.

for i in range(cpus):
    print("Registrando el hilo %d" % i)
    threads.append(Thread(target=calc))

start = time.time()
#Iniciar todos los hilos (son seriales)
for thread in threads:
    thread.start()

#Esperar a que terminen los hilos......zxz


for thread in threads:
    thread.join()

end = time.time()
#Restar los tiempos
print("Se tardo: ",end-start)



#Lista de procesos.

procesos = []
for i in range(cpus):
    print("registrando el proceso %d" % i)
    procesos.append(Process(target=calc))

start = time.time()

#Iniciar procesos en Paralelo.
for proceso in procesos:
    proceso.start()


#Terminar procesos.
for proceso in procesos:
    proceso.join()

end = time.time()
print("Se tardo: ", end-start)




