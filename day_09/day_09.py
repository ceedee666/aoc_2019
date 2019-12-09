from intcode_computer import *

if __name__ == "__main__":
    with open("day_09/input.txt") as f:
        program = list(map(int,f.readline().split(',')))
    
    print("The BOOST key code is (part 1):", execute_intcode_and_collect_output(program, [1]) )
    print("The coordinates of the distress signal are (part 2):", execute_intcode_and_collect_output(program, [2]) )