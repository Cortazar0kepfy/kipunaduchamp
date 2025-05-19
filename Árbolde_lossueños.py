#Cortázar Tinajero Luis Enrique.



#Gráficos realizando la tortuga que pinta al caminar en las almas.
import turtle
tortuga = turtle.Turtle()
tortuga.left(80)  #Giro a la izquierda con ángulo de 80 grados.
tortuga.speed(400) #Velocidad de la tortuga.


#Con ángulos de 90 es un árbol H. Es decir:
angulo:float = 90
#El árbol se construye con recursividad.

def arbol(i:float,angulo:float):
    if i<10.00:
        return
    else:
        tortuga.forward(i) #Camina i
        tortuga.left(angulo) #Gira a la izquierda 80 grados.
        arbol(3.0*i/4.25,angulo)
        tortuga.right(2*angulo)
        arbol(3.0*i/4.25,angulok)
        tortuga.left(angulo)
        tortuga.backward(i)

