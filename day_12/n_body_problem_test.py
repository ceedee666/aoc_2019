import pytest
from n_body_problem import *

test_input = ["<x=-1, y=0, z=2>", "<x=2, y=-10, z=-7>", "<x=4, y=-8, z=8>", "<x=3, y=5, z=-1>"]
test_input_2 = ["<x=-8, y=-10, z=0>", "<x=5, y=5, z=10>", "<x=2, y=-7, z=3>","<x=9, y=-8, z=-3>"]

def test_parse_moon_locations():
    moon_locations = parse_moon_locations(test_input)
    assert moon_locations[0] == [-1, 0, 2]
    assert moon_locations[1] == [2, -10, -7]

def test_parse_init_velocities():
    initial_values = init_velocities(parse_moon_locations(test_input))
    assert initial_values[0][3:] == [0,0,0]
    assert initial_values[1][3:] == [0,0,0]   
    assert initial_values[3][3:] == [0,0,0]

def test_calculate_velocity_change():
    state = [[1,-3,7,0,0,0],[2, -5, 3,0,0,0]]
    state = calculate_velocity_change(0, 1, state)
    assert state[0][3:] == [1, -1, -1]
    assert state[1][3:] == [-1, 1, 1]

def test_simulate_motion():
    state = init_velocities(parse_moon_locations(test_input))
    
    """
    After 1 step:
    pos=<x= 2, y=-1, z= 1>, vel=<x= 3, y=-1, z=-1>
    pos=<x= 3, y=-7, z=-4>, vel=<x= 1, y= 3, z= 3>
    pos=<x= 1, y=-7, z= 5>, vel=<x=-3, y= 1, z=-3>
    pos=<x= 2, y= 2, z= 0>, vel=<x=-1, y=-3, z= 1>
    """
    state = simulate_motion(state)
    assert state[0] == [2,-1,1,3,-1,-1]
    assert state[1] == [3,-7,-4,1,3,3]
    assert state[2] == [1,-7,5,-3,1,-3]
    assert state[3] == [2,2,0,-1,-3,1]

    """
    After 2 steps:
    pos=<x= 5, y=-3, z=-1>, vel=<x= 3, y=-2, z=-2>
    pos=<x= 1, y=-2, z= 2>, vel=<x=-2, y= 5, z= 6>
    pos=<x= 1, y=-4, z=-1>, vel=<x= 0, y= 3, z=-6>
    pos=<x= 1, y=-4, z= 2>, vel=<x=-1, y=-6, z= 2>
    """
    state = simulate_motion(state)
    assert state[0] == [5,-3,-1,3,-2,-2]
    assert state[1] == [1,-2,2,-2,5,6]
    assert state[2] == [1,-4,-1,0,3,-6]
    assert state[3] == [1,-4,2,-1,-6,2]

    """
    after 10 steps:
    pos=<x= 2, y= 1, z=-3>, vel=<x=-3, y=-2, z= 1>
    pos=<x= 1, y=-8, z= 0>, vel=<x=-1, y= 1, z= 3>
    pos=<x= 3, y=-6, z= 1>, vel=<x= 3, y= 2, z=-3>
    pos=<x= 2, y= 0, z= 4>, vel=<x= 1, y=-1, z=-1>
    """
    for _ in range(8):
        state = simulate_motion(state)

    assert state[0] == [2, 1,-3,-3, -2, 1]
    assert state[1] == [1,-8, 0,-1,  1, 3]
    assert state[2] == [3,-6, 1, 3,  2,-3]
    assert state[3] == [2, 0, 4, 1, -1,-1]
    
def test_calculate_system_energy():
    state = init_velocities(parse_moon_locations(test_input_2))
    
    for _ in range(100):
        state = simulate_motion(state)

    assert calculate_system_energy(state) == 1940

def test_steps_until_repetition():
    state = init_velocities(parse_moon_locations(test_input))
    assert steps_until_repetition(state) == 2772

    state = init_velocities(parse_moon_locations(test_input_2))
    assert steps_until_repetition(state) == 4686774924