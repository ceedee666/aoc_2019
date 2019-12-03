from functools import reduce
from itertools import product


def calculate_intersection_distance(path_1, path_2):
    coordinates_1 = convert_path_to_coordinates(split_direction_and_distance(path_1))
    coordinates_2 = convert_path_to_coordinates(split_direction_and_distance(path_2))

    expanded_segments_1 = expand_segments(convert_coordinates_to_segments(coordinates_1))
    expanded_segments_2 = expand_segments(convert_coordinates_to_segments(coordinates_2))

    intersections = filter(
                            lambda i: i != (0,0),
                                calculate_intersections(expanded_segments_1, expanded_segments_2))

    return min(
            map(
                lambda i: abs(i[0]) + abs(i[1]), intersections))

def convert_path_to_coordinates(step_list):
    coordinates = [(0,0)]
   
    for step in step_list:
        coordinates.append(calculate_coordinate(step, coordinates[-1]))

    return coordinates

# convert ['R1', 'U12', 'L99', 'D1'] --> [('R',1), ('U',12), ('L',99), ('D',1)] 
def split_direction_and_distance(path):
    return [{ 'dir' : step[0], 'dist' : int(step[1:])} for step in path]

def calculate_coordinate(step, current_coordinate):
    new_coordinate = ()
    if step['dir'] == 'U':
        new_coordinate = (current_coordinate[0], current_coordinate[1] + step['dist'])
    elif step['dir'] == 'D':
        new_coordinate = (current_coordinate[0], current_coordinate[1] - step['dist'])
    elif step['dir'] == 'R':
        new_coordinate = (current_coordinate[0] + step['dist'], current_coordinate[1])
    elif step['dir'] == 'L':
        new_coordinate = (current_coordinate[0] - step['dist'], current_coordinate[1])

    return new_coordinate

def convert_coordinates_to_segments(coordinates):
    return list(zip(coordinates[:-1], coordinates[1:]))

def expand_segments(segments):
    return [expand_segment(segment) for segment in segments]

def expand_segment(segment):
    x1,y1 = segment[0]
    x2,y2 = segment[1]
    if x1 == x2:
        start, end, step = calculate_range_params(y1, y2)
        return tuple((x1, y) for y in range(start, end, step))
    elif y1 == y2: 
        start, end, step = calculate_range_params(x1, x2)
        return tuple((x, y1) for x in range(start, end, step))

def calculate_range_params(start, end):
    if start > end:
        step = -1
        end -= 1
    else:
        step = 1
        end += 1
    return(start,end,step)

def calculate_intersections(segments_1, segments_2):
    return list(
            reduce(
                lambda s1, s2: s1.union(s2), 
                    [set(c[0]).intersection(set(c[1])) for c in product(segments_1, segments_2)]))




if __name__ == "__main__":
    with open("day_03/input.txt") as f:
        path1 = f.readline().split(',')
        path2 = f.readline().split(',')
    
    print("Result for part 1:", calculate_intersection_distance(path1, path2))