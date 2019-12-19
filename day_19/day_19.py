from intcode_computer import *

X_START = 0
Y_START = 1000

cache = {}

def is_coordinate_affected_by_beam(x,y):
    if (x,y) not in cache:
        program = parse_incode_file("day_19/int_code_program.txt")
        cache[(x,y)] = execute_intcode_and_collect_output(program, [x, y])[0]

    return cache[(x,y)]

def print_beam(coordinates, size):
    image = "".join("#" if c[2] == 1 else "." for c in coordinates)
    image = [ image[i:i+size] for i in range(0, len(coordinates), len(coordinates) // size) ]

    list(map(print, image))

def affected_coordinates(size):
    coordinates = [(x, y, is_coordinate_affected_by_beam(x,y)) for x in range(size) for y in range(size)]

    print_beam(coordinates, size)

    affected_coordinates = list(filter(lambda c: c[2] == 1, coordinates))
    return affected_coordinates

def find_last_affected_x(y):
    x = X_START
    while is_coordinate_affected_by_beam(x,y) == 0:
        x += 1
    while is_coordinate_affected_by_beam(x,y) == 1:
        x += 1
    return x - 1

def ship_boundaries(x,y):
    return [(x-99, y), (x,y), (x-99, y+99), (x, y+99)]

def does_ship_fit(boundaries):
    if False in map(lambda b: b[1] >= 0, boundaries):
        return False

    checked_coordinates = map(lambda b: is_coordinate_affected_by_beam(b[0],b[1]), boundaries)
    if 0 in checked_coordinates:
        return False
    else:
        return True
    
def fit_ship_in_beam():
    y = Y_START 
    fit = False

    while not fit:
        if y % 10 == 0:
            print("*", end='', flush=True)

        x = find_last_affected_x(y)
        boundaries = ship_boundaries(x,y)
        fit = does_ship_fit(boundaries)
        y += 1


    return boundaries




if __name__ == "__main__":
    
    print("In the 50x50 area closest to the emitter", len(affected_coordinates(50)), "are affected by the beam.")
    print("Santas ship fits at the following coordinates: ", fit_ship_in_beam())

