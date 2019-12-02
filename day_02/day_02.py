HCF = 99
ADD = 1

def execute_intcode(program):
    instruction_pointer = 0
    while program[instruction_pointer] != HCF:
        operand_1_address = program[instruction_pointer + 1]
        operand_2_address = program[instruction_pointer + 2]
        target_address = program[instruction_pointer + 3]

        if program[instruction_pointer] == ADD:
            program[target_address] = program[operand_1_address] + program[operand_2_address]
        else:
            program[target_address] = program[operand_1_address] * program[operand_2_address]
        
        instruction_pointer += 4
    return program

if __name__ == "__main__":
    with open("day_02/input_02.txt") as f:
        program = list(map(int,f.readline().split(',')))
        result = execute_intcode(program)

        print("Result for part 1:", result[0])