import pytest
from day_14 import *

def test_parse_reactions():
    test_input = [ "10 ORE => 10 A", 
                    "1 ORE => 1 B", 
                    "7 A, 1 B => 1 C", 
                    "7 A, 1 C => 1 D", 
                    "7 A, 1 D => 1 E", 
                    "7 A, 1 E => 1 FUEL"]

    reactions = parse_reactions(test_input)
    assert reactions["FUEL"] == [1, ["A", 7], ["E", 1]]
    assert reactions["E"] == [1, ["A", 7], ["D", 1]]
    assert reactions["A"] == [10, ["ORE", 10]]

def test_calc_required_ore():
    test_input = [ "10 ORE => 10 A", 
                    "1 ORE => 1 B", 
                    "7 A, 1 B => 1 C", 
                    "7 A, 1 C => 1 D", 
                    "7 A, 1 D => 1 E", 
                    "7 A, 1 E => 1 FUEL"]
                    
    reactions = parse_reactions(test_input)
    amount = calc_ore("FUEL", reactions)
    assert amount == 31