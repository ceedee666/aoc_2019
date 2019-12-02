def execute_intcode(program):
    return []

if __name__ == "__main__":
    with open("2/input_02.txt") as f:
        program = f.readline().split(',')
        result = execute_intcode(program)

        print("Result for part 1:", result[0])