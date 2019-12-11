from intcode_computer import *
from functools import reduce
import operator

BLACK = 0
WHITE = 1

TURN_LEFT = 0
TURN_RIGHT = 1

UP = 'U'
LEFT = 'L'
DOWN = 'D'
RIGHT = 'R'

def execute_robot_step(robot_pos, ship, program_state):
    x,y, orientation = robot_pos
    program_input = [panel_color(x,y,ship)]
    color_step_result = execute_intcode(program_state[0], program_input, program_state[2], program_state[3] )
    turn_step_result = execute_intcode(color_step_result[0], program_input, color_step_result[2], color_step_result[3])
    
    ship = paint_panel(x, y, color_step_result[1], ship)
    turn_direction = turn_step_result[1][0] if turn_step_result[1] else 0

    return move_robot(robot_pos, turn_direction), ship, turn_step_result

def paint_ship(program, start_color = BLACK):
    robot_pos = (0,0,UP)
    ship = paint_panel(0,0,[start_color],{})

    current_state = (robot_pos, ship,(program, [],0,0, False))
    while not current_state[2][4]:

        current_state = execute_robot_step(current_state[0], current_state[1], current_state[2])

    return current_state[1]


def panel_color(x,y, ship):
    color = BLACK

    if x in ship and y in ship[x]:
        color = ship[x][y]

    return color

def paint_panel(x, y, color, ship):
    if color:
        if not x in ship:
            ship[x] = {}
        if not y in ship[x]:
            ship[x][y] = {}
        ship[x][y] = color[0]

    return ship

def move_robot(robot_pos, turn_direction):
    x,y,o = robot_pos
    new_o = new_orientation(o, turn_direction)
    if new_o == LEFT:
        x -= 1
    elif new_o == RIGHT:
        x += 1   
    elif new_o == UP:
        y += 1   
    elif new_o == DOWN:
        y -= 1   
    return x,y,new_o

def new_orientation(orientation, turn_direction):
    if orientation == UP and turn_direction == TURN_LEFT:
        new_o = LEFT
    elif orientation == LEFT and turn_direction == TURN_LEFT:
         new_o = DOWN
    elif orientation == DOWN and turn_direction == TURN_LEFT:
         new_o = RIGHT
    elif orientation == RIGHT and turn_direction == TURN_LEFT:
         new_o = UP
    elif orientation == UP and turn_direction == TURN_RIGHT:
        new_o = RIGHT
    elif orientation == LEFT and turn_direction == TURN_RIGHT:
         new_o = UP
    elif orientation == DOWN and turn_direction == TURN_RIGHT:
         new_o = LEFT
    elif orientation == RIGHT and turn_direction == TURN_RIGHT:
         new_o = DOWN
    return new_o

    
def painting_dimensions(hull_painting):
    min_x = min(hull_painting.keys())
    max_x = max(hull_painting.keys())
    
    min_y = reduce(lambda a, k: min(hull_painting[k]) if min(hull_painting[k]) < a else a, hull_painting.keys(), 0)
    max_y = reduce(lambda a, k: max(hull_painting[k]) if max(hull_painting[k]) > a else a, hull_painting.keys(), 0)

    return min_x, max_x, min_y, max_y

if __name__ == "__main__":
    with open("day_11/robot_int_program.txt") as f:
        program = list(map(int,f.readline().split(',')))

    hull_painting = paint_ship(list(program))

    painted_panels = reduce(operator.add, map(lambda k: len(hull_painting[k]), hull_painting.keys()))
    print("The number of panels painted at least once is: ", painted_panels)

    print("The ship registration number is:")
    hull_painting = paint_ship(list(program), WHITE)
    min_x, max_x, min_y, max_y = painting_dimensions(hull_painting)
    
    for x in range(min_x, max_x + 1):
        print("".join("\u2588" if panel_color(x,y,hull_painting) == WHITE else " " for y in range(min_y, max_y+1)))
