import pytest
from day_18 import *

def test_find_start_positions():
    maze = [ \
        "#########", \
        "#b.A.@.a#", \
        "#########"]

    assert find_start_positions(maze) == [(1,5)]

def test_shortest_path():
    maze = [ \
        "#########", \
        "#b.A.@.a#", \
        "#########"]

    assert shortest_path(maze, find_start_positions(maze)[0], []) == 8

    maze = [ \
        '########################', \
        '#f.D.E.e.C.b.A.@.a.B.c.#', \
        '######################.#', \
        '#d.....................#', \
        '########################']

    assert shortest_path(maze, find_start_positions(maze)[0], []) == 86

    maze = [ \
        "########################", \
        "#...............b.C.D.f#", \
        "#.######################", \
        "#.....@.a.B.c.d.A.e.F.g#", \
        "########################"]

    assert shortest_path(maze, find_start_positions(maze)[0], []) == 132

    maze = [ \
        "#################", \
        "#i.G..c...e..H.p#", \
        "########.########", \
        "#j.A..b...f..D.o#", \
        "########@########", \
        "#k.E..a...g..B.n#", \
        "########.########", \
        "#l.F..d...h..C.m#", \
        "#################" ]

    assert shortest_path(maze, find_start_positions(maze)[0], []) == 136

    maze = [ \
        "########################", \
        "#@..............ac.GI.b#",
        "###d#e#f################",
        "###A#B#C################",
        "###g#h#i################",
        "########################"]
    assert shortest_path(maze, find_start_positions(maze)[0], []) == 81