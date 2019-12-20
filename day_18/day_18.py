import collections
import string

MAX_VAL = 100000

START = '@'
WALL = '#'
EMPTY = '.'
DOORS = string.ascii_uppercase
KEYS = string.ascii_lowercase



def find_start_positions(maze):
    all_maze_indices = [(x,y) for x in range(len(maze)) for y in range(len(maze[0]))]
    return list(filter(lambda i: maze[i[0]][i[1]] == START, all_maze_indices))

def reachable_indices(maze, pos):
    positions = [(pos[0] + 1, pos[1]),
                 (pos[0] - 1, pos[1]),
                 (pos[0], pos[1] + 1), 
                 (pos[0], pos[1] - 1)]
    return list(filter(lambda p: 0 <= p[0] < len(maze) and 0 <= p[1] < len(maze[0]), positions))

def find_reachable_keys(maze, start_position, current_keys):
    queue = collections.deque([start_position])

    distance = {start_position : 0}

    reachable_keys = {}
    while queue:
        pos = queue.popleft()

        for next_pos in reachable_indices(maze, pos):
            next_pos_type = maze[next_pos[0]][next_pos[1]]

            if next_pos_type == WALL or next_pos in distance:
                continue
            
            distance[next_pos] = distance[pos] + 1

            if next_pos_type in DOORS and next_pos_type.lower() not in current_keys:
                continue

            if next_pos_type in KEYS and next_pos_type not in current_keys:
                reachable_keys[next_pos_type] = (next_pos, distance[next_pos])
            else:
                queue.append(next_pos)

    return reachable_keys

cache = {}
def shortest_path(maze, start_position, current_keys):
    sorted_keys = tuple(sorted(current_keys))
    if (start_position, sorted_keys) in cache:
        return cache[(start_position, sorted_keys)]
    
    if len(cache) % 10 == 0:
        print(len(cache), " - ", sorted_keys)

    reachable_keys = find_reachable_keys(maze, start_position, current_keys)
    if len(reachable_keys) == 0:
        # done!
        result = 0
    else:
        poss_paths = []
        for key, (pos, dist) in reachable_keys.items():
            poss_paths.append(dist + shortest_path(maze, pos, current_keys + [key]))
        result = min(poss_paths)

    cache[(start_position, sorted_keys)] = result
    return result

if __name__ == "__main__":
    with open("day_18/maze.txt") as f:
        maze = [l.strip() for l in f.readlines()]

    start = find_start_positions(maze)[0]

    print("The shortest path to collect all of the keys is", shortest_path(maze, start, []), "steps.")