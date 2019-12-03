import pytest
import day_03

def test_calculate_intersection_distance():
    path1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
    path2 = ['U62','R66','U55','R34','D71','R55','D58','R83']
    assert day_03.calculate_intersection_distance(path1, path2) == 159

    path1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
    path2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
    assert day_03.calculate_intersection_distance(path1, path2) == 135

def test_calculate_coordinate():
    assert day_03.calculate_coordinate({'dir':'U','dist':1}, (0,0)) == (0,1)
    assert day_03.calculate_coordinate({'dir':'D','dist':1}, (0,0)) == (0,-1)
    assert day_03.calculate_coordinate({'dir':'L','dist':1}, (0,0)) == (-1,0)
    assert day_03.calculate_coordinate({'dir':'R','dist':1}, (0,0)) == (1,0)

def test_convert_path_to_coordinates():
    steps = [{'dir':'R','dist':1}, {'dir':'U','dist':1}, {'dir':'L','dist':1}, {'dir':'D','dist':1}]
    assert day_03.convert_path_to_coordinates(steps) ==  [(0,0), (1,0), (1,1), (0,1), (0,0)] 

def test_split_direction_and_distance():
    path = ['R1', 'U12', 'L99', 'D1']
    assert day_03.split_direction_and_distance(path) ==  [{'dir':'R','dist':1}, {'dir':'U','dist':12}, {'dir':'L','dist':99}, {'dir':'D','dist':1}] 

def test_convert_coordinates_to_segments():
    coordinates = [(0,0), (1,0), (1,1), (0,1), (0,0)]
    assert day_03.convert_coordinates_to_segments(coordinates) == [((0,0), (1,0)), ((1,0), (1,1)), ((1,1), (0,1)), ((0,1), (0,0))]

def test_expand_segment():
    s1 = ((0,0), (3,0))
    s2 = ((0,-3), (0,0))
    s3 = ((0,1), (0,-2))

    assert day_03.expand_segment(s1) == ((0,0), (1,0), (2,0), (3,0))
    assert day_03.expand_segment(s2) == ((0,-3), (0,-2), (0,-1), (0,0))
    assert day_03.expand_segment(s3) == ((0,1), (0,0), (0,-1), (0,-2))

def test_expand_segements():
    s1 = ((0,0), (3,0))
    s2 = ((0,-3), (0,0))
    s3 = ((0,1), (0,-2))
    segments = (s1,s2,s3)

    assert day_03.expand_segments(segments) == [((0,0), (1,0), (2,0), (3,0)), ((0,-3), (0,-2), (0,-1), (0,0)), ((0,1), (0,0), (0,-1), (0,-2))]


def test_calculate_intersections():
    segments_a = [((1,0), (2,0), (3,0)), ((0,-3), (0,-2), (0,-1))]
    segments_b = [((1,0), (1,1)), ((1,-3),(0,-3))]
    segments_c = [((2,0), (3,0))]
    assert day_03.calculate_intersections(segments_a, segments_b) == [(1,0),(0,-3)]
    assert day_03.calculate_intersections(segments_b, segments_a) == [(1,0),(0,-3)]
    assert day_03.calculate_intersections(segments_b, segments_c) == []
    assert day_03.calculate_intersections(segments_c, segments_b) == []