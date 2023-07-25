from turtle import Turtle, Screen
import random


def generar_color_aleatorio():
    # Generar tres componentes RGB aleatorios entre 0 y 1
    r = random.random()
    g = random.random()
    b = random.random()

    return (r, g, b)


# Función para cambiar el color de la tortuga de manera aleatoria
def cambiar_color_aleatorio():
    color = generar_color_aleatorio()
    alberto.pencolor(color)  # Cambiar el color de la línea de la tortuga


alberto = Turtle()
alberto.shape("turtle")
lines = 3
for _ in range(10):
    for _ in range(lines):
        cambiar_color_aleatorio()
        alberto.forward(100)
        alberto.right(360 / lines)
    lines += 1

screen = Screen()
screen.exitonclick()
