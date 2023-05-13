"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *
#Se importo toda la liberia turtle
import turtle
#Se importo math para la generacion del triangulo
import math
from freegames import vector



def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

#Se anadio el codigo que genera el rectangulo
def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

    end_fill()


# Se usa turtle para generar el circulo
def circle(start, end):
    """Draw circle from start to end."""
    t = turtle.Turtle()
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    r = 25
    t.circle(r,)

    end_fill()

#Se anadio el codigo que genera el rectangulo
def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()

#Se anadio el codigo que genera el triangulo
def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    side_length = math.sqrt((end.x - start.x)**2 + (end.y - start.y)**2)
    angle = math.degrees(math.atan2(end.y - start.y, end.x - start.x))

    setheading(angle)
    for count in range(3):
        forward(side_length)
        left(120)

    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
#Se anade el color amarillo
onkey(lambda: color('yellow'), 'Y')

onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
