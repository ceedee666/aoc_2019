import pytest
import day_05

def test_execute_intcode():
    # Day 2 tests
    assert day_05.execute_intcode([1,0,0,0,99])[0] == [2,0,0,0,99]
    assert day_05.execute_intcode([2,3,0,3,99])[0] == [2,3,0,6,99]
    assert day_05.execute_intcode([2,4,4,5,99,0])[0] == [2,4,4,5,99,9801]
    assert day_05.execute_intcode([1,1,1,4,99,5,6,0,99])[0] == [30,1,1,4,2,5,6,0,99]
    assert day_05.execute_intcode([1,9,10,3,2,3,11,0,99,30,40,50])[0] == [3500,9,10,70,2,3,11,0,99,30,40,50]

    # Day 5 tests
    assert day_05.execute_intcode([1002,4,3,4,33])[0] == [1002,4,3,4,99]
    assert day_05.execute_intcode([1101,100,-1,4,0])[0] == [1101,100,-1,4,99]

def test_analyse_opcode():
    assert day_05.analyse_opcode(1002) == (2,0,1,0)

def test_calc_operand_address():
    assert day_05.calc_operand_address(1, day_05.PARA_MODE['POS'], [4,3,2,1]) == 3
    assert day_05.calc_operand_address(1, day_05.PARA_MODE['IMM'], [4,3,2,1]) == 1

def test_calc_next_ip():
    assert day_05.calc_next_ip(0, day_05.OPCODES['INPUT']) == 2
    assert day_05.calc_next_ip(0, day_05.OPCODES['OUTPUT']) == 2
    assert day_05.calc_next_ip(0, day_05.OPCODES['ADD']) == 4