def calculate_fuel(mass):
    return (mass // 3) - 2

def calculate_fuel_for_modules(modules):
    return sum(map(calculate_fuel, modules))

def calculate_total_fuel(modules):
    all_masses = []
    for mass in modules:
        mass = calculate_fuel(mass)
        while mass > 0:
            all_masses.append(mass)
            mass = calculate_fuel(mass)
    return sum(all_masses)

if __name__ == "__main__":
    with open("day_01/input_01.txt") as f:
        modules = list(map(int,f.readlines()))

    print("Fuel for modules (Puzzle 1):", calculate_fuel_for_modules(modules))
    print("Total fuel (Puzzle 2):", calculate_total_fuel(modules))