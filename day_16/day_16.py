from functools import reduce

BASE_PATTERN = [0, 1, 0, -1]


def build_repeating_pattern(pos_index, out_len):
    pattern = []
    index = 0

    while len(pattern) < out_len + 1:
        pattern += [BASE_PATTERN[index]] * (pos_index + 1)
        index = (index + 1) % len(BASE_PATTERN)

    return pattern[1:]

def calc_pos_value(i, transmission):
    pattern = build_repeating_pattern(i, len(transmission))
    value = reduce(lambda a, e: a + e[0] * e[1], zip(transmission,pattern), 0)
    value = abs(value) % 10
    return value

def correction_step(transmission):
    return [calc_pos_value(i, transmission) for i in range(len(transmission))]


def correct_transmission_with_FFT(transmission):
    return reduce(lambda a, _: correction_step(a), range(100), transmission)

def correction_step_with_partial_sum(transmission):
    s = sum(transmission)
    output = []
    for i in range(len(transmission)):
        output += [s % 10]
        s -= transmission[i]
    return output

def phase_two_optimization(transmission):
    offset = int(reduce(lambda a, v: a + str(v), transmission[:7],""))
    transmission = transmission[offset:]
    return reduce(lambda a, _: correction_step_with_partial_sum(a), range(100), transmission)[:8]


if __name__ == "__main__":
    with open("day_16/transmission.txt") as f:
        transmission = list(map(int, list(f.readline())))

    #print("The first eight digits in the final output list are:", correct_transmission_with_FFT(transmission)[:8]) 

    finale_message = transmission * 10000

    print("The eight-digit message embedded in the transmission is:", phase_two_optimization(finale_message))