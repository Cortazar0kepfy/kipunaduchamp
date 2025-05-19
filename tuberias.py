#Cortázar Tinajero Luis Enrique.


from multiprocessing import Process, Pipe
#Uso de tuberias para comunicación .


#Manda el vector para dicha comnunicación.


def f(extremo):
    extremo.send([0,1,2,3,4])
    extremo.close()
#Recibe el vector con la comunicación de sumar 100 a cada componente.


def g(extremo):
    a = extremo.recv()
    for i in a:
        a[i] += 100
    print(a)
    extremo.close()

#Programa principal(Algoritmo)


if __name__ == "__main__":
    #Tuberias con sus extremos.
    #===================================
    extremo1, extremo2 = Pipe()

    #Instanciar procesos(Target es la función)
    #(args son los argumentos de la función.
    proceso1 = Process(target=f,args=(extremo1,))
    proceso2 = Process(target=g, args=(extremo2,))
    
    #Comenzar procesos.
    proceso2.start()
    proceso1.start()

    #Esperar a que terminen los procesos.
    proceso1.join()
    proceso2.join()

