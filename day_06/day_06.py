import operator

from collections import defaultdict
from functools import reduce

def convert_input_to_orbit(input):
    orbit_list = [s.strip().split(')') for s in input.split()]
    orbit_dict = defaultdict(list)
    for o in orbit_list:
        orbit_dict[o[1]].append(o[0])
    return orbit_dict

def number_of_direct_orbits(orbit_dict):
    return len(orbit_dict.keys())

def number_of_all_orbits(orbit_dict):
    number_of_orbits = 0
    all_orbits_dict = all_orbit_paths(orbit_dict)
    for k in all_orbits_dict.keys():
        number_of_orbits += len(all_orbits_dict[k])
    return number_of_orbits

def all_orbit_paths(orbit_dict):
    all_orbits = defaultdict(list)
    for o in orbit_dict.keys():
        all_orbits[o] = path_to_com(o, orbit_dict)
    return all_orbits

def path_to_com(o, orbit_dict):
    path = []
    current_object = o
    while not 'COM' in path:
        current_object = orbit_dict[current_object][0]
        path.append(current_object)

    return path

def min_number_of_orbital_transfers(o1, o2, orbit_dict):
    all_orbits = all_orbit_paths(orbit_dict)
    o1_path_to_com = all_orbits[o1]
    o2_path_to_com = all_orbits[o2]
    common_object = set(o1_path_to_com).intersection(set(o2_path_to_com))
    for o in common_object:
        o1_path_to_com.remove(o)
        o2_path_to_com.remove(o)
    return len(o1_path_to_com) + len(o2_path_to_com)

if __name__ == "__main__":
    with open("day_06//input.txt") as f:
        orbit_dict = convert_input_to_orbit(f.read())
    
    print("The total number of orbits is: ", number_of_all_orbits(orbit_dict))
    print("The minimal number of transfers to get to Santa is: ", min_number_of_orbital_transfers('YOU', 'SAN', orbit_dict))
