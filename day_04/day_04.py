from functools import reduce
from collections import defaultdict

LOW = 264360
HIGH = 746325

def password_candidates_part_2(range):
    return list(
            filter(exactly_two_adjacent_digits,
                filter(at_least_two_adjacent_digits, 
                    filter(increasing_digits,range))))

def password_candidates_part_1(range):
    return list(
                filter(at_least_two_adjacent_digits, 
                    filter(increasing_digits,range)))

def increasing_digits(value):
    l = list(str(value))
    return l == sorted(l)

def at_least_two_adjacent_digits(value):
    return reduce(check_same_digit, list(str(value)), ("", False))[1]

def exactly_two_adjacent_digits(value):
    l = list(str(value))
    digits = defaultdict(int)
    for digit in l:
        digits[digit] += 1
    return 2 in digits.values()

def check_same_digit(acc, digit):
    if (digit == acc[0]) or (acc[1] == True):
        return digit, True
    else:
        return digit, False

if __name__ == "__main__":
    print("Number of password candidates (Part 1):", len(password_candidates_part_1(range(LOW, HIGH+1))))
    print("Number of password candidates (Part 2):", len(password_candidates_part_2(range(LOW, HIGH+1))))
