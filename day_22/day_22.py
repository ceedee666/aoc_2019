from functools import reduce

DEAL_WITH_INC = "deal with increment"
DEAL_NEW_STACK = "deal into new stack"
CUT = "cut"

def deal_into_new_stack(stack):
    return tuple(reversed(stack))

def cut(stack, index):
    if index > 0:
        return tuple(stack[index:] + stack[0:index])
    else:
        return tuple(stack[index:] + stack[0:len(stack)+index])
    
def deal_with_increment(stack, increment):
    position_dict = {(pos * increment) % len(stack) : val for pos, val in enumerate(stack)}
    return tuple(position_dict[k] for k in sorted(position_dict.keys()))

def parse_instruction(instruction):
    if DEAL_WITH_INC in instruction:
        return (DEAL_WITH_INC, int(instruction.split()[-1]))
    elif DEAL_NEW_STACK in instruction:
        return (DEAL_NEW_STACK, 0)
    else:
        return (CUT, int(instruction.split()[-1]))


def parse_instructions(instructions):
    return [parse_instruction(i) for i in instructions]

def perform_shuffle(stack, instruction):
    operation = instruction[0]
    value = instruction[1]
    if DEAL_NEW_STACK == operation:
        return deal_into_new_stack(stack)
    elif DEAL_WITH_INC == operation:
        return deal_with_increment(stack, value)
    elif CUT == operation:
        return cut(stack, value)

def shuffle(stack, instructions, rounds = 1):
    for i in range(rounds):
        if i % 100000 == 1:
            print("*", end= "", flush= True)
        stack = reduce(lambda s, i: perform_shuffle(s,i), instructions, stack)
    return stack


if __name__ == "__main__":
    with open("day_22/shuffle_instructions.txt") as f:
        instructions = f.readlines()

    instructions = parse_instructions(instructions)
    stack = shuffle(range(10007), instructions)

    print("After shuffling the deck of 10007 cards, the position of card 2019 is:", stack.index(2019))
