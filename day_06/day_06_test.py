import pytest
import day_06

test_input_1 = """COM)B
                B)C
                C)D
                D)E
                E)F
                B)G
                G)H
                D)I
                E)J
                J)K
                K)L"""

test_input_2 = """COM)B
                    B)C
                    C)D
                    D)E
                    E)F
                    B)G
                    G)H
                    D)I
                    E)J
                    J)K
                    K)L
                    K)YOU
                    I)SAN"""

def test_convert_input_to_orbit():
    orbit_dict = day_06.convert_input_to_orbit(test_input_1)
    assert orbit_dict['B'] == ['COM']
    assert orbit_dict['D'] == ['C']
    assert orbit_dict['E'] == ['D']
    assert orbit_dict['F'] == ['E']
    assert orbit_dict['L'] == ['K']

def test_path_to_com():
    assert day_06.path_to_com('L', day_06.convert_input_to_orbit(test_input_1)) == ['K','J','E','D', 'C','B', 'COM']

def test_number_of_direct_orbits():
    assert day_06.number_of_direct_orbits(day_06.convert_input_to_orbit(test_input_1)) == 11

def test_number_of_all_orbits():
    assert day_06.number_of_all_orbits(day_06.convert_input_to_orbit(test_input_1)) == 42

def test_min_number_of_orbital_transfers():
    assert day_06.min_number_of_orbital_transfers('YOU', 'SAN', day_06.convert_input_to_orbit(test_input_2)) == 4