from functools import reduce
import operator
import math

ASTEROID = '#'

def pipeline(data, fns):
    return reduce(lambda d, f: f(d),
                  fns,
                  data)

def calculate_slope(point_a, point_b):
    x1, y1 = point_a
    x2, y2 = point_b
    return ((y2 - y1) / (x2 - x1), x1 > x2) if x1 != x2 else math.inf

def coordinates_form_line(input_line, y):
    return list(map(lambda i: (i[0], y, i[1]), enumerate(input_line)))

def build_asteroid_map(input):
    lines = map(lambda i: coordinates_form_line(i[1], i[0]),  enumerate(input))
    return list(filter(lambda c: c[2] == ASTEROID, reduce(operator.add, lines, [])))

def line_of_sight(source, asteroid_map):
    new_asteroid_map = list(asteroid_map)
    new_asteroid_map.remove(source)
    return list(map(lambda target: calculate_slope(source[0:2], target[0:2]), new_asteroid_map))

def lines_of_sight(asteroid_map):
    los = list(map(lambda asteroid: (asteroid, line_of_sight(asteroid, asteroid_map)), asteroid_map))
    return los

def direct_lines_of_sight(lines_of_sight):
    dlos = list(map(lambda e: (e[0], len(set(e[1]))), lines_of_sight))
    return dlos

def find_best_position(direct_lines_of_sight):
    best_pos = reduce(lambda p1, p2: p1 if p1[1] > p2[1] else p2,direct_lines_of_sight) 
    return best_pos

def best_pos(input):
    best_pos = pipeline(input, [build_asteroid_map,
                                lines_of_sight,
                                direct_lines_of_sight,
                                find_best_position])
    return best_pos

if __name__ == "__main__":
    with open("day_10/input.txt") as f:
        input = f.readlines()

    print("The best location for a new monitoring station:", best_pos(input))