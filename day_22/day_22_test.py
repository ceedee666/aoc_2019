from day_22 import *

def test_parse_instructions_file():
    with open("day_22/shuffle_instructions.txt") as f:
        instructions = f.readlines()
    instructions = parse_instructions(instructions)
    assert instructions[0] == (DEAL_WITH_INC, 55)
    assert instructions[1] == (CUT, -6984)
    assert instructions[2] == (DEAL_NEW_STACK, 0)

def test_deal_into_new_stack():
    assert deal_into_new_stack(tuple(range(10))) == (9,8,7,6,5,4,3,2,1,0)

def test_cut():
    result = cut(tuple(range(10)), 3)
    assert result == (3, 4, 5, 6, 7, 8, 9, 0, 1, 2)

    result = cut(tuple(range(10)), -4)
    assert result == (6, 7, 8, 9, 0, 1, 2, 3, 4, 5) 

def test_deal_with_increment():
    result = deal_with_increment(tuple(range(10)), 3)
    assert result == (0, 7, 4, 1, 8, 5, 2, 9, 6, 3)  

def test_shuffle():
    instructions = ["deal with increment 7", \
                    "deal into new stack", \
                    "deal into new stack" ] 
    instructions = parse_instructions(instructions)
    assert shuffle(tuple(range(10)), instructions) == (0, 3, 6, 9, 2, 5, 8, 1, 4, 7)
    
    instructions = ["deal into new stack", \
                    "cut -2", \
                    "deal with increment 7", \
                    "cut 8", \
                    "cut -4", \
                    "deal with increment 7", \
                    "cut 3", \
                    "deal with increment 9", \
                    "deal with increment 3", \
                    "cut -1" ]
    instructions = parse_instructions(instructions)
    assert shuffle(tuple(range(10)), instructions) == (9, 2, 5, 8, 1, 4, 7, 0, 3, 6)
