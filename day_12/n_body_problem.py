import itertools
import math

from functools import reduce
from copy import deepcopy


def int_value(s):
    return int(s.split("=")[1])

def parse_moon_locations(lines):
    components = [line.strip('\n<>').split(",") for line in lines]
    return [[int_value(c[0]), int_value(c[1]), int_value(c[2])] for c in components]

def init_velocities(locations):
    return [location + [0,0,0] for location in locations]

def simulate_motion(state):
    previous_state = state
    state = calculate_velocity_changes(previous_state)
    state = calculate_new_positions(state)
    return state

def calculate_velocity_change_one_axis(a,b, axis, state):
    offset = len(state[0]) // 2
    if state[a][axis] > state[b][axis]:
        state[a][offset + axis] -= 1
        state[b][offset + axis] += 1
    elif state[a][axis] < state[b][axis]:
        state[a][offset + axis] += 1
        state[b][offset + axis] -= 1
    return state

def calculate_velocity_change(a, b, state):
    return reduce(lambda s, i: calculate_velocity_change_one_axis(a, b, i, s), range(len(state[0]) // 2),state)

def calculate_velocity_changes(state):
    combinations = itertools.combinations(range(len(state)), 2)
    state = reduce(lambda a, c: calculate_velocity_change(c[0],c[1], a) , combinations, state)
    return state

def calculate_new_positions(state):
    offset = len(state[0]) // 2
    state = list(
                 map(
                     lambda s: [p + s for p,s in zip(s[0:offset],s[offset:])] + s[offset:], 
                                 state))
    return state

def absolute_values(list):
    return [abs(e) for e in list]

def calculate_system_energy(state):
    return reduce(
                lambda a, s: a + sum(s[0:3]) * sum(s[3:]), 
                map(absolute_values, state), 0)                                    

def convert_state_to_tuple(state):
    return tuple([tuple(e) for e in state])

def periode_length(state):
    previous_states = set()

    state_tuple = convert_state_to_tuple(state)

    while state_tuple not in previous_states:
        previous_states.add(state_tuple)
        state = simulate_motion(state)
        state_tuple = convert_state_to_tuple(state)

    return len(previous_states)

def lcm(x, y, z):
    lcm = int(x * y / math.gcd(x, y))
    lcm = int(lcm * z / math.gcd(lcm, z))
    return lcm

def steps_until_repetition(state):
    x_state = [[moon[0],moon[3]] for moon in state]
    y_state = [[moon[1],moon[4]] for moon in state]
    z_state = [[moon[2],moon[5]] for moon in state]
    
    return lcm(periode_length(x_state), periode_length(y_state), periode_length(z_state))

if __name__ == "__main__":
    with open("day_12/moon_locations.txt") as f:
        state = init_velocities(parse_moon_locations(f.readlines()))
        state_2 = deepcopy(state)
    for _ in range(1000):
        state = simulate_motion(state)

    print("The total energy in the system after 1000 steps is:", calculate_system_energy(state))
    print("History repeats itself after ", steps_until_repetition(state_2), "steps.")