OPCODES = { 
    "ADD" : 1,
    "MUL" : 2,
    "INP" : 3,
    "OUT" : 4,
    "JIT" : 5,
    "JIF" : 6 ,
    "LES" : 7,
    "EQU" : 8,
    "HCF" : 99 }

PARA_MODE = {
    'POS' : 0,
    'IMM' : 1
}    

def execute_intcode(program, input=0):
    instruction_pointer = 0
    output = []
    hcf = False

    while not hcf:
        opcode_details = analyse_opcode(program[instruction_pointer])
        if opcode_details[0] == OPCODES["HCF"]:
            hcf = True
        else:
            operand_1_address, operand_2_address, operand_3_address = calc_operand_addresses(instruction_pointer, opcode_details, program)
            new_instruction_pointer = instruction_pointer

            if opcode_details[0] == OPCODES["ADD"]:
                program[operand_3_address] = program[operand_1_address] + program[operand_2_address]

            elif opcode_details[0] == OPCODES["MUL"]:
                program[operand_3_address] = program[operand_1_address] * program[operand_2_address]

            elif opcode_details[0] == OPCODES["INP"]:
                program[operand_1_address] = input

            elif opcode_details[0] == OPCODES["OUT"]:
                output.append(program[operand_1_address])

            elif opcode_details[0] == OPCODES["JIT"]:
                if program[operand_1_address] != 0:
                    new_instruction_pointer = program[operand_2_address]

            elif opcode_details[0] == OPCODES["JIF"]:
                if program[operand_1_address] == 0:
                    new_instruction_pointer = program[operand_2_address]

            elif opcode_details[0] == OPCODES["LES"]:
                if program[operand_1_address] < program[operand_2_address]:
                    program[operand_3_address] = 1
                else:
                    program[operand_3_address] = 0

            elif opcode_details[0] == OPCODES["EQU"]:
                if program[operand_1_address] == program[operand_2_address]:
                    program[operand_3_address] = 1
                else:
                    program[operand_3_address] = 0 

            if instruction_pointer == new_instruction_pointer:
                instruction_pointer = calc_next_ip(instruction_pointer, opcode_details[0])
            else:
                instruction_pointer = new_instruction_pointer
    return program, output

def calc_next_ip(instruction_pointer, opcode):
    if opcode in (OPCODES["INP"], OPCODES["OUT"]):
        instruction_pointer += 2
    elif opcode in (OPCODES["JIT"], OPCODES["JIF"]):
        instruction_pointer += 3
    else:
        instruction_pointer += 4
    return instruction_pointer

def calc_operand_address(instruction_pointer, mode, program ):
    operand_address = 0 
    if mode == PARA_MODE['IMM']:
        operand_address = instruction_pointer 
    else:        
        if instruction_pointer < len(program):
            operand_address = program[instruction_pointer] 
    return operand_address 

def calc_operand_addresses(instruction_pointer, opcode_details, program ):
    operand_1_address = calc_operand_address(instruction_pointer + 1, opcode_details[1], program)
    operand_2_address = calc_operand_address(instruction_pointer + 2, opcode_details[2], program)
    operand_3_address = calc_operand_address(instruction_pointer + 3, opcode_details[3], program)
    return operand_1_address, operand_2_address, operand_3_address

def analyse_opcode(opcode):
    opcode_list = list(str(opcode))
    opcode_list = pad_opcode(opcode_list)
    instruction = ''.join(opcode_list[3:])
    return (int(instruction),int(opcode_list[2]),int(opcode_list[1]),int(opcode_list[0]))

def pad_opcode(opcode_list):
    return (5 - len(opcode_list)) * ["0"] + opcode_list


if __name__ == "__main__":
    with open("day_05/input.txt") as f:
        program_part_1 = list(map(int,f.readline().split(',')))
        program_part_2 = list(program_part_1)

    print("Diagnostics code for module 1 (air condition unit): ", execute_intcode(program_part_1, 1)[1][-1])
    print("Diagnostics code for module 5 (thermal radiators): ", execute_intcode(program_part_2, 5)[1][-1])