from intcode_computer import *
from functools import reduce
import random

NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4

HIT_WALL = 0
MOVED = 1
FOUND = 2

WALL = "#"
EMPTY = "."
OXYGEN = "o"

def explore(program):
    area_map = {}
    dist_map = {}
    starting_pos = (0,0)

    area_map[starting_pos] = EMPTY
    dist_map[starting_pos] = 0

    instruction_pointer = 0
    relative_base = 0
    hcf = False
    found = False
    
    while not hcf and not found:
        direction = random.randint(1,4)
        new_pos = move_in_dir(starting_pos, direction)
        program, output, instruction_pointer, relative_base, hcf = execute_intcode(program, [direction], instruction_pointer, relative_base)
        
        if output[0] == HIT_WALL:
            area_map[new_pos] = WALL
        elif output[0] == MOVED:
            area_map[new_pos] = EMPTY
            dist_map = update_dist_map(dist_map, new_pos)
            starting_pos = new_pos
        elif output[0] == FOUND:
            area_map[new_pos] = OXYGEN
            dist_map = update_dist_map(dist_map, new_pos)
            found = True

    return area_map, dist_map, new_pos

def update_dist_map(dist_map, new_pos):
    distances = []
    north_pos = move_in_dir(new_pos, NORTH)
    south_pos = move_in_dir(new_pos, SOUTH)
    east_pos  = move_in_dir(new_pos, EAST)
    west_pos  = move_in_dir(new_pos, WEST)

    if north_pos in dist_map.keys():
        distances.append(dist_map[north_pos] + 1)
    elif south_pos in dist_map.keys():
        distances.append(dist_map[south_pos] + 1)
    elif east_pos in dist_map.keys():
        distances.append(dist_map[east_pos] + 1)
    elif west_pos in dist_map.keys():
        distances.append(dist_map[west_pos] + 1)
    
    if new_pos in dist_map.keys():
        distances.append(dist_map[new_pos])
    
    dist_map[new_pos] = min(distances)
    return dist_map

def move_in_dir(pos, direction):
    if direction == NORTH:
        new_pos = (pos[0], pos[1]-1)
    elif direction == SOUTH:
        new_pos = (pos[0], pos[1]+1)
    elif direction == WEST:
        new_pos = (pos[0]-1, pos[1])
    elif direction == EAST:
        new_pos = (pos[0]+1, pos[1])
    return new_pos

def print_map(area_map, dist_map):
    max_x = reduce(lambda a,k: k[0] if k[0] > a else a, area_map.keys(), 0)
    max_y = reduce(lambda a,k: k[1] if k[1] > a else a, area_map.keys(), 0)
    min_x = reduce(lambda a,k: k[0] if k[0] < a else a, area_map.keys(), 0)
    min_y = reduce(lambda a,k: k[1] if k[1] < a else a, area_map.keys(), 0)

    print("Budaries x:", min_x, ",", max_x, " y:", min_y, ",", max_y)

    for x in range(min_x, max_x+1):
        line = ""
        for y in range(min_y, max_y+1):
            if (x,y) in area_map.keys():
                if area_map[(x,y)] == WALL:
                    line += "\u2588" * 5
                elif area_map[(x,y)] == OXYGEN:
                    line += "*" + pad_int(dist_map[(x,y)]) + "*"
                elif (x,y) == (0,0):
                    line += "X" * 5
                else: 
                    line += " " + pad_int(dist_map[(x,y)]) + " "
            else:
                line += " " * 5
        print(line)

def pad_int(value):
    s = str(value)
    if len(s) == 1:
        return " "+s+" "
    if len(s) == 2:
        return " "+s
    if len(s) == 3:
        return s

if __name__ == "__main__":
    program = parse_incode_file("./day_15/remote_control_intcode.txt")
    area_map, dist_map, oxygen_pos = explore(program)

    print_map(area_map, dist_map)

    print("The minimum number of moves to get from (0,0) to", oxygen_pos, "are", dist_map[oxygen_pos])