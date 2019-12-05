
OPCODES = { 
    "ADD"       : 1,
    "MULT"      : 2,
    "INPUT"     : 3,
    "OUTPUT"    : 4, 
    "HCF"       : 99 }

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
            operand_1_address = calc_operand_address(instruction_pointer + 1, opcode_details[1], program)
            operand_2_address = calc_operand_address(instruction_pointer + 2, opcode_details[2], program)
            target_address = calc_operand_address(instruction_pointer + 3, opcode_details[3], program)
            
            if opcode_details[0] == OPCODES["ADD"]:
                program[target_address] = program[operand_1_address] + program[operand_2_address]
            elif opcode_details[0] == OPCODES["MULT"]:
                program[target_address] = program[operand_1_address] * program[operand_2_address]
            elif opcode_details[0] == OPCODES["INPUT"]:
                program[operand_1_address] = input
            elif opcode_details[0] == OPCODES["OUTPUT"]:
                output.append(program[operand_1_address])

            instruction_pointer = calc_next_ip(instruction_pointer, opcode_details[0])
    return program, output

def calc_next_ip(instruction_pointer, opcode):
    if opcode == OPCODES["OUTPUT"] or opcode == OPCODES["INPUT"]:
        instruction_pointer += 2
    else:
        instruction_pointer += 4
    return instruction_pointer

def calc_operand_address(instruction_pointer, mode, program ):
    return instruction_pointer if mode == PARA_MODE['IMM'] else program[instruction_pointer]

def analyse_opcode(opcode):
    opcode_list = list(str(opcode))
    opcode_list = pad_opcode(opcode_list)
    instruction = ''.join(opcode_list[3:])
    return (int(instruction),int(opcode_list[2]),int(opcode_list[1]),int(opcode_list[0]))

def pad_opcode(opcode_list):
    return (5 - len(opcode_list)) * ["0"] + opcode_list

if __name__ == "__main__":
    with open("day_05/input.txt") as f:
        program = list(map(int,f.readline().split(',')))
        
    print("Diagnostics code for module 1 (air condition unit): ", execute_intcode(program, 1)[1][-1])