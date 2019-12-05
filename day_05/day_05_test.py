import pytest
import day_05

def test_execute_intcode_day_2():
    assert day_05.execute_intcode([1,0,0,0,99])[0] == [2,0,0,0,99]
    assert day_05.execute_intcode([2,3,0,3,99])[0] == [2,3,0,6,99]
    assert day_05.execute_intcode([2,4,4,5,99,0])[0] == [2,4,4,5,99,9801]
    assert day_05.execute_intcode([1,1,1,4,99,5,6,0,99])[0] == [30,1,1,4,2,5,6,0,99]
    assert day_05.execute_intcode([1,9,10,3,2,3,11,0,99,30,40,50])[0] == [3500,9,10,70,2,3,11,0,99,30,40,50]

def test_execute_intcode_day_5():
    # Part 1
    assert day_05.execute_intcode([1002,4,3,4,33])[0] == [1002,4,3,4,99]
    assert day_05.execute_intcode([1101,100,-1,4,0])[0] == [1101,100,-1,4,99]

    # Part 2
    # Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not)
    assert day_05.execute_intcode([3,9,8,9,10,9,4,9,99,-1,8], 8)[1] == [1]
    assert day_05.execute_intcode([3,9,8,9,10,9,4,9,99,-1,8], 9)[1] == [0]

    #Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not)
    assert day_05.execute_intcode([3,9,7,9,10,9,4,9,99,-1,8], 7)[1] == [1]
    assert day_05.execute_intcode([3,9,7,9,10,9,4,9,99,-1,8], 9)[1] == [0]

    #Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
    assert day_05.execute_intcode([3,3,1108,-1,8,3,4,3,99], 8)[1] == [1]
    assert day_05.execute_intcode([3,3,1108,-1,8,3,4,3,99], 5)[1] == [0]
    #Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
    assert day_05.execute_intcode([3,3,1107,-1,8,3,4,3,99], 7)[1] == [1]
    assert day_05.execute_intcode([3,3,1107,-1,8,3,4,3,99], 9)[1] == [0]

    # Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:
    assert day_05.execute_intcode([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 0)[1] == [0]
    assert day_05.execute_intcode([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 5)[1] == [1] 
    assert day_05.execute_intcode([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 0)[1] == [0]  
    assert day_05.execute_intcode([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 5)[1] == [1]

    # Here's a larger example:
    # The program uses an input instruction to ask for a single number.
    # The program will then output 999 if the input value is below 8, 
    # output 1000 if the input value is equal to 8, 
    # or output 1001 if the input value is greater than 8.
    example_program = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

    assert day_05.execute_intcode(example_program, 7)[1] == [999]
    assert day_05.execute_intcode(example_program, 8)[1] == [1000]
    assert day_05.execute_intcode(example_program, 9)[1] == [1001] 




def test_analyse_opcode():
    assert day_05.analyse_opcode(1002) == (2,0,1,0)

def test_calc_operand_address():
    assert day_05.calc_operand_address(1, day_05.PARA_MODE['POS'], [4,3,2,1]) == 3
    assert day_05.calc_operand_address(1, day_05.PARA_MODE['IMM'], [4,3,2,1]) == 1

def test_calc_next_ip():
    assert day_05.calc_next_ip(0, day_05.OPCODES['JIF']) == 3
    assert day_05.calc_next_ip(0, day_05.OPCODES['JIT']) == 3
    assert day_05.calc_next_ip(0, day_05.OPCODES['INP']) == 2
    assert day_05.calc_next_ip(0, day_05.OPCODES['OUT']) == 2
    assert day_05.calc_next_ip(0, day_05.OPCODES['ADD']) == 4