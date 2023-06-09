"""Pacman, classic arcade game.

Exercises

1. Change the board.
2. Change the number of ghosts.
3. Change where pacman starts.
4. Make the ghosts faster/slower.
5. Make the ghosts smarter.
"""

from random import choice
from turtle import *

from freegames import floor, vector

state = {'score': 0}
path = Turtle(visible=False)
writer = Turtle(visible=False)
aim = vector(5, 0)
pacman = vector(-40, -80)
ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]
"""Se cambia el tablero"""
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
# fmt: on


def square(x, y):
    """Draw square using path at (x, y)."""
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()


def offset(point):
    """Return offset of point in tiles."""
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index


def valid(point):
    """Return True if point is valid in tiles."""
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0


def world():
    """Draw world using path."""
    bgcolor('navy')
    path.color('skyblue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(5, 'gold')

"""Función para hacer los fantasmas más listos"""                
def ghost_move(point, course):
    if valid(point + course):
            point.move(course)
    else:
        """Se mueve a la derecha""""
        if point.x < pacman.x:
            movimiento = [vector(10, 0), vector(0, 10)] if point.y < pacman.y else [vector(10, 0), vector(0, -10)]
        else:
            """Se mueve a la izquierda"""
            movimiento = [vector(-10, 0), vector(0, 10)] if point.y < pacman.y else [vector(-10, 0), vector(0, -10)]
        up()
        
        """Selecciona aleatoriamente a donde moverse"""
        plan = choice(movimiento)
        course.x = plan.x
        course.y = plan.y
    goto(point.x + 10, point.y + 10)
    dot(20, 'red')

def move():
    "Move pacman and all ghosts."
    writer.undo()
    writer.write(state['score'])

    clear()

    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        #opciones:
        else:
            option1 = vector(5, 0)
            option2 = vector(-5, 0)
            option3 = vector(0, 5)
            option4 = vector(0, -5)

        
            if abs(pacman.x - point.x) > abs(pacman.y - point.y):
                #elige opcion 2 
                if pacman.x < point.x:
                    plan = option2
                #elige opcion 1 
                elif pacman.x > point.x:
                    plan = option1
                
                course.x = plan.x
                course.y = plan.y
                
                if valid(point + course):
                    point.move(course)
                else:
                    if pacman.y < point.y:
                        plan = option4
                    #elige opcion 3 
                    elif pacman.y > point.y:
                        plan = option3

                    
            
            elif abs(pacman.x - point.x) < abs(pacman.y - point.y):
                #elige opcion 4
                if pacman.y < point.y:
                    plan = option4
                #elige opcion 3
                elif pacman.y > point.y:
                    plan = option3
                
                course.x = plan.x
                course.y = plan.y
                
                if valid(point + course):
                    point.move(course)
                else:
                    #elige opcion 2
                    if pacman.x < point.x:
                        plan = option2
                    #elige opcion 1
                    elif pacman.x > point.x:
                        plan = option1
                    

            
            
            elif pacman.x == point.x:
                #elige opcion 4
                if pacman.y < point.y:
                    plan = option4
                #elige opcion 3
                elif pacman.y > point.y:
                    plan = option3
                    
               
            elif pacman.y == point.y:
                #elige opcion 2
                if pacman.x < point.x:
                    plan = option2
                #elige opcion 1
                elif pacman.x > point.x:
                    plan = option1
                    
            course.x = plan.x
            course.y = plan.y

        up()
        
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')

    update()
    """Se cambian los parametros para hacer que se muevan más rapido"""
    for point, course in ghosts:
        if abs(pacman - point) < 5:
            return

    ontimer(move, 10) #cambia la velocidad


def change(x, y):
    """Change pacman aim if valid."""
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
done()
