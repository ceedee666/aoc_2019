import pytest
from day_10 import *


def test_calculate_slope():
    assert calculate_slope((1,3), (3,2)) == (-0.5, False)

def test_coordinates_form_line():
    assert coordinates_form_line(".#..#", 1) == [(0,1,"."), (1,1,"#"), (2,1,"."), (3,1,"."), (4,1,"#")]

def test_build_asteroid_map():
    input_str = ".#..#\n.....\n#####"
    asteroid_map = build_asteroid_map(input_str.split("\n"))
    assert len(asteroid_map) == 7
    assert asteroid_map[2] == (0,2,'#')

def test_line_of_sight():
    """Map used in test is a translation of this
    .#..#
    .....
    #####
    ....#
    ...##"""
    asteroid_map = [(0,1,'#'),(0,4,'#'),(0,2,'#'),(1,2,'#'),(2,2,'#'),(3,2,'#'),(4,2,'#'),(4,3,'#'),(3,4,'#'),(4,4,'#')]
    los = line_of_sight((0,1,'#'), asteroid_map)
    assert len(los) == 9
    assert los[8] == (0.75, False)

def test_lines_of_sight():
    """Map used in test is a translation of this
    .#..#
    .....
    #####
    ....#
    ...##"""
    asteroid_map = [(0,1,'#'),(0,4,'#'),(0,2,'#'),(1,2,'#'),(2,2,'#'),(3,2,'#'),(4,2,'#'),(4,3,'#'),(3,4,'#'),(4,4,'#')]
    
    los = lines_of_sight(asteroid_map)
    assert len(los) == 10
    assert len(los[0][1]) == 9

def test_direct_lines_of_sight():
    """Map used in test is a translation of this
    .#..#
    .....
    #####
    ....#
    ...##"""
    asteroid_map = [(0,1,'#'),(0,4,'#'),(0,2,'#'),(1,2,'#'),(2,2,'#'),(3,2,'#'),(4,2,'#'),(4,3,'#'),(3,4,'#'),(4,4,'#')]
    
    dlos = direct_lines_of_sight(lines_of_sight(asteroid_map))
    assert dlos[9][1] == 7


def test_find_best_position():
    input = ".#..#\n.....\n#####\n....#\n...##".split("\n")
    result = best_pos(input)
    assert result[0] == (3,4,"#")
    
    input = "......#.#.\n#..#.#....\n..#######.\n.#.#.###..\n.#..#.....\n..#....#.#\n#..#....#.\n.##.#..###\n##...#..#.\n.#....####".split("\n")
    result = best_pos(input)
    assert result[0] == (5,8,"#")

    input = "#.#...#.#.\n.###....#.\n.#....#...\n##.#.#.#.#\n....#.#.#.\n.##..###.#\n..#...##..\n..##....##\n......#...\n.####.###.".split("\n")
    result = best_pos(input)
    assert result[0] == (1,2,"#")

    input = ".#..#..###\n####.###.#\n....###.#.\n..###.##.#\n##.##.#.#.\n....###..#\n..#.#..#.#\n#..#.#.###\n.##...##.#\n.....#.#..".split("\n")
    result = best_pos(input)
    assert result[0] == (6,3,"#")

    input = ".#..##.###...#######\n##.############..##.\n.#.######.########.#\n.###.#######.####.#.\n#####.##.#.##.###.##\n..#####..#.#########\n"
    input += "####################\n#.####....###.#.#.##\n##.#################\n#####.##.###..####..\n..######..##.#######\n####.##.####...##..#\n"
    input += ".#####..#.######.###\n##...#.##########...\n#.##########.#######\n.####.#.###.###.#.##\n....##.##.###..#####\n.#.#.###########.###\n"
    input += "#.#.#.#####.####.###\n###.##.####.##.#..##"
    input = input.split("\n")
    result = best_pos(input)
    assert result[0] == (11,13,"#")
