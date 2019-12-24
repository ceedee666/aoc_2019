from functools import reduce
from itertools import takewhile

SIZE = 5
ALIVE = '#'
EMPTY = '.'

def live_neighbor_count(current, i):
    neighbor_states = [current[i] == ALIVE for i in neighbor_indices(i)]
    alive_neighbors = list(filter(lambda s: s == True, neighbor_states))
    return len(alive_neighbors)

def calculate_next_cell_state(current, i, next):
    """ 
    Rules:
    - A bug dies (becoming an empty space) unless there is exactly one bug adjacent to it.
    - An empty space becomes infested with a bug if exactly one or two bugs are adjacent to it.
    """
    if current[i] == ALIVE:
        if live_neighbor_count(current, i) == 1:
            next[i] = ALIVE
        else:
            next[i] = EMPTY
    else:
        if live_neighbor_count(current, i) in [1,2]:
            next[i] = ALIVE
        else:
            next[i] = EMPTY
    
    return next

def calculate_next_state(current):
    return reduce(lambda next, i: calculate_next_cell_state(current, i, next), current.keys(), {})

def neighbor_indices(i):
    x,y = i
    indices = [(x-1, y),
               (x+1, y),
               (x, y-1),
               (x, y+1)]
    return filter(lambda i: 0 <= i[0] < SIZE and 0 <= i[1] < SIZE, indices)

def parse_lines(lines):
    state = {}
    for y,line in enumerate(lines):
        line = line.strip()
        for x,c in enumerate(line):
            state[x,y] = c
    return state

def first_state_occuring_twice(state):
    seen = []
    while state not in seen:
        seen.append(state)
        state = calculate_next_state(state)
    
    return state, seen

def biodiversity_rating(state):
    return reduce(lambda a, k: a + pow(2, k[1] * SIZE + k[0]) if state[k] == ALIVE else a + 0, state.keys(), 0)

if __name__ == "__main__":
    with open("day_24/input.txt") as f:
        lines = f.readlines()
        state = parse_lines(lines)


    state, seen = first_state_occuring_twice(state)
    print("The biodiversity rating for the first layout that appears twice is", biodiversity_rating(state))