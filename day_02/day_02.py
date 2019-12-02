HCF = 99
ADD = 1
PART2_MAGIC_NUMBER = 19690720

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

def calculate_noun_and_verb(program):
    for noun in range(100):
        for verb in range(100):
            new_program = list(program)
            new_program[1] = noun
            new_program[2] = verb

            result = execute_intcode(new_program)
            if result[0] == PART2_MAGIC_NUMBER:
                return noun,verb


if __name__ == "__main__":
    with open("day_02/input_02.txt") as f:
        input = list(map(int,f.readline().split(',')))

    program_part_1 = list(input)
    program_part_1[1] = 12
    program_part_1[2] = 2
    result = execute_intcode(program_part_1)
    print("Result for part 1:", result[0])

    noun,verb = calculate_noun_and_verb(input)
    print("Result for part 2:", 100 * noun + verb)