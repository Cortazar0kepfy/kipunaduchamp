#Cortázar Tinajero Luis Enrique.
import multiprocessing as mp 
import numpy as np
import time


def func(i, param1, param2, param3):
    #Calcular un [A] 
    result = param1**2 + param2 + param3
    #Se retrasa.
    #Por 2 segundos.
    time.sleep(2)
    return (i,result)

def resultado(result):
    #Se inscriben en lista global
    global results
    results.append(result)


if __name__ == "__main__":
    #Matrix(Matriz de 10x3 nuúmeros al azar.
    params = np.random.random((10,3))*100.0
    results = []
    ts = time.time()

    #Un grupo de procesos (pool)
    pool = mp.Pool(mp.cpu_count())
    #loop de primera dimensión del arreglo.
    for i in range(0, params.shape[0]):
        #Correr asincrónamente my_function con argumentos
        # y cuando termine correr resultado.
        #=====================================
        pool.apply_async(func, args = (i,params[i,0], params[i,1], params[i,2]), callback=resultado)
        
