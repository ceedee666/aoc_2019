import intcode_computer
import itertools

def compute_amplifier_output(program, phase_setting):
    output = 0
    
    for phase in phase_setting:
        current_program = list(program)
        output = intcode_computer.execute_intcode(current_program, [phase, output])[1]
    return output

def max_thruster_signal(program):
    return max([compute_amplifier_output(program, phase_setting) for phase_setting in itertools.permutations(range(5))])

def max_thruster_signal_with_feedback(program):
    thruster_signals = []
    for phase_setting in itertools.permutations(range(5,10)):
        state_amp_a = [False, list(program), [phase_setting[0]],0]
        state_amp_b = [False, list(program), [phase_setting[1]],0]
        state_amp_c = [False, list(program), [phase_setting[2]],0]
        state_amp_d = [False, list(program), [phase_setting[3]],0]
        state_amp_e = [False, list(program), [phase_setting[4]],0]

        output = 0
    
        while state_amp_e[0] != True:
            state_amp_a[2].append(output)
            state_amp_a[1], output, state_amp_a[3], state_amp_a[0] = intcode_computer.execute_intcode(state_amp_a[1], state_amp_a[2], state_amp_a[3])
            
            state_amp_b[2].append(output)
            state_amp_b[1], output, state_amp_b[3], state_amp_b[0] = intcode_computer.execute_intcode(state_amp_b[1], state_amp_b[2], state_amp_a[3])
            
            state_amp_c[2].append(output)
            state_amp_c[1], output, state_amp_c[3], state_amp_c[0] = intcode_computer.execute_intcode(state_amp_c[1], state_amp_c[2], state_amp_a[3])
           
            state_amp_d[2].append(output)
            state_amp_d[1], output, state_amp_d[3], state_amp_d[0] = intcode_computer.execute_intcode(state_amp_d[1], state_amp_d[2], state_amp_a[3])
           
            state_amp_e[2].append(output)
            state_amp_e[1], output, state_amp_e[3], state_amp_e[0] = intcode_computer.execute_intcode(state_amp_e[1], state_amp_e[2], state_amp_a[3])


        thruster_signals.append(output)
    return max(thruster_signals)
 

if __name__ == "__main__":
    with open("day_07/input.txt") as f:
        program = list(map(int,f.readline().split(',')))
    
    print("Max thruster signal: ", max_thruster_signal(program))