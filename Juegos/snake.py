"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *
#Se importa random para su uso en el movimiento de la comida
import random

from freegames import square, vector

food = vector(0, 0)
#Se añade el vector food move
foodMove = vector(0,0)
snake = [vector(10, 0)]
aim = vector(0, -10)
#Lista de colores para la serpiente y la comida
colors = ['black', 'blue', 'green', 'orange', 'purple']
#Se asignan los colores de la serpiente
randColorSnake = random.choice(colors)
#Se elimina el color de la serpiente asi la comida nunca tendra el mismo
colors.remove(randColorSnake)
randColorFood  = random.choice(colors)

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)
    food.move(foodMove)
  #Se utiliza el vector foodmove para darle movimiento aleatoriamente a la comida
  #Los if anidados evitan que la comida se salga de la pantalla
    if (-200 < food.x < 190):
        foodMove.x = random.choice([-10, 10])
    elif (-200 > food.x):
        food.x = -190
    elif (food.x > 190):
        food.x = 180

    if (-200 < food.y < 190):
        foodMove.y = random.choice([-10, 10])
    elif (-200 > food.y):
        food.y = -190
    elif (food.y > 190):
        food.y = 180

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        #Se reemplazan los colores originales por los generados aleatoriamente
        square(body.x, body.y, 9, randColorSnake)

    square(food.x, food.y, 9, randColorFood)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
