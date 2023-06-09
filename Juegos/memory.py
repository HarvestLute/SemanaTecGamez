"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
#Nueva variable para la cantidad de taps
taps = 0
tiles_ocultas = 64


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    #Se declara taps como global y se incrementa en 1 cada vez que se hace un tap
    global taps, tiles_ocultas
    taps += 1
    spot = index(x, y)
    mark = state['mark']
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        #se restan 2 tiles ocultas al total si se consiguio formar la pareja
        tiles_ocultas -= 2
        state['mark'] = None
        #Si se descubren todas las tiles, el juego reporta que se ha terminado
    if tiles_ocultas == 0:
        print("Game over")


def draw():
    """Draw image and tiles."""
    global tiles_ocultas
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        #Se modifico la posicion inicial del texto en x y y
        goto(x + 25, y + 2)
        color('black')
        #Se agrego align center para centrar el texto en
        write(tiles[mark], align="center", font=('Arial', 30, 'normal'))

    
    up()
    goto(-180, 180)
    color('black')
    write(f'Taps: {taps}', font=('Arial', 16, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
