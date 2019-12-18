from intcode_computer import *

from itertools import groupby

SCAFFOLD = 35
OPEN = 46
NEW_LINE = 10

def parse_img(camera_img):
    return [list(g) for k,g in groupby(camera_img, lambda x: x == 10) if not k]

def print_img(camera_img):
    for row in camera_img:
        print("".join("#" if c == SCAFFOLD else "." for c in row))

def is_intersection(row, col, camera_img):
    x = row[0]
    y = col[0]
    if camera_img[x][y] != SCAFFOLD:
        return False

    if x > 0 and x != len(camera_img) - 1 and y > 0 and y != len(camera_img[0]) - 1:
        if camera_img[x - 1][y] == SCAFFOLD and \
           camera_img[x + 1][y] == SCAFFOLD and \
           camera_img[x][y - 1] == SCAFFOLD and \
           camera_img[x][y + 1] == SCAFFOLD:
            return True
    return False


def locate_intersection(camera_img):
    intersections = []
    for row in enumerate(camera_img):
        for col in enumerate(camera_img[row[0]]):
            if is_intersection(row, col, camera_img):
                intersections.append((row[0], col[0]))
    return intersections


def calculate_alignment_params(camera_img):
    intersections = locate_intersection(camera_img)
    return sum(map(lambda e: e[0] * e[1], intersections))




if __name__ == "__main__":
    program = parse_incode_file("day_17/int_code_program.txt")

    camera_img = execute_intcode_and_collect_output(program)
    camera_img = parse_img(camera_img)

    print("The current camera image:")
    print_img(camera_img)

    print("The sum of the alignment parameters is:", calculate_alignment_params(camera_img))


