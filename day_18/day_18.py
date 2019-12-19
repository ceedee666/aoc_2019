START = '@'

def find_start_positions(maze):
    all_maze_indices = [(x,y) for x in range(len(maze)) for y in range(len(maze[0]))]
    return list(filter(lambda i: maze[i[0]][i[1]] == START, all_maze_indices))

if __name__ == "__main__":
    with open("maze.txt") as f:
        maze = [l.strip() for l in f.readlines()]

    starts = find_start_positions(maze)