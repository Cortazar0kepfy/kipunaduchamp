#Akata.

import turtle
import random
#Configuración  del entorno gráfico.
turtle.bgcolor("lightblue") #Fondo azul cielo.
tortuga = turtle.Turtle()
tortuga.color("Red")
tortuga.pensize(3)
tortuga.speed(0)
"""Esto quiere decir que Aumenta la velocidad
del dibujo que muestra el entorno gráfico.
"""
tortuga.left(90)
def arbol(i: float, angulo: float):
    if i < 10.00:
        return
    else:
        tortuga.color(random.choice(["purple", "blue", "cyan","magenta", "white"]))
        tortuga.forward(i)
        tortuga.left(angulo)
        arbol(3.0 * i / 4.25, angulo)
        tortuga.right(2 * angulo)
        arbol(3.0 * i / 4.25, angulo)
        tortuga.left(angulo)
        tortuga.backward(i)
"""Función para dibujar particulas mágicas
"""
def particula(x, y):
    tortuga.penup()
    tortuga.goto(x, y)
    tortuga.pendown()
    tortuga.color(random.choice(["gold", "yellow", "white", "cyan"]))
    tortuga.begin_fill()
    tortuga.circle(random.randint(1,5))
    tortuga.end_fill()

"""Dibuja el árbol principal con ramas coloridas.
"""
arbol(100,30)
#Agregar particulas mágicas alrededor del árbol.
for _ in range(20):
    particula(random.randint(-70, 70), random.randint(50, 150))
turtle.done()

