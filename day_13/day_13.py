from intcode_computer import *
from collections import defaultdict
from functools import reduce

EMPTY = 0
WALL = 1 
BLOCK = 2 
H_PAD = 3
BALL = 4 

def execute_arcade_game_step(program, joystic_pos = 0):
    instruction_pointer = 0
    all_output = []
    relative_base = 0
    hcf = False
    
    while not hcf:
        i = [joystic_pos]
        program, output, instruction_pointer, relative_base, hcf = execute_intcode(program, i, instruction_pointer, relative_base)
        all_output += output
    return all_output

def add_tile_to_screen(screen, pos, tile):
    screen[pos] = tile
    return screen

def count_tiles(output, tile):
    tiles = [output[i:i + 3] for i in range(0, len(output), 3)]
    screen = defaultdict(int)
    screen = reduce(lambda a, t: add_tile_to_screen(screen, (t[0],t[1]), t[2]), tiles, screen)
    return len(list(filter(lambda t: t == tile, screen.values())))

if __name__ == "__main__":
    program = parse_incode_file("./day_13/intcode_game.txt")
    tile_count = count_tiles(execute_arcade_game_step(program), BLOCK)
    print("There are", tile_count, "block tiles are on the screen when the game exits")

    program = parse_incode_file("./day_13/intcode_game.txt")
    program[0] = 2
    output = execute_arcade_game_step(program)
    1+1