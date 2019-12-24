from day_24 import *

def test_calculate_next_state():
    current = parse_lines(["....#", \
                           "#..#.", \
                           "#..##", \
                           "..#..", \
                           "#...."])

    next = parse_lines(["#..#.", \
                        "####.",\
                        "###.#",\
                        "##.##",\
                        ".##.."])
    calculated_state = calculate_next_state(current)
    assert calculated_state == next

    current = next
    next = parse_lines(["#####", \
                        "....#", \
                        "....#", \
                        "...#.", \
                        "#.###"])
    calculated_state = calculate_next_state(current)
    assert calculated_state == next

    current = next
    next = parse_lines(["#....", \
                        "####.", \
                        "...##", \
                        "#.##.", \
                        ".##.#"])
    calculated_state = calculate_next_state(current)
    assert calculated_state == next

    current = next
    next = parse_lines(["####.", \
                        "....#", \
                        "##..#", \
                        ".....", \
                        "##..."])
    calculated_state = calculate_next_state(current)
    assert calculated_state == next

def test_first_state_occuring_twice():
    state = parse_lines(["....#", \
                         "#..#.", \
                         "#..##", \
                         "..#..", \
                         "#...."])
    
    result = parse_lines([".....", \
                         ".....", \
                         ".....", \
                         "#....", \
                         ".#..."])

    assert first_state_occuring_twice(state)[0] == result


def test_biodiversity_rating():
    state = parse_lines([".....", \
                         ".....", \
                         ".....", \
                         "#....", \
                         ".#..."])
    assert biodiversity_rating(state) == 2129920