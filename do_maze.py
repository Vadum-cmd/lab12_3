"""Example of maze being played."""
from maze import *


def main():
    """The main function."""
    maze = buildMaze("mazefile.txt")
    if maze.find_path():
        print("Path found....")
        print(maze)
    else:
        print("Path not found....")
        print(maze)

def read_pair_of_numbers(file):
    """Extracts an integer value pair from the given input file."""
    line = file.readline()
    num_rows, num_cols = line.split()
    return int(num_rows), int(num_cols)

def buildMaze(filename):
    """Builds a maze based on a text format in the given file."""
    file = open(filename, "r")

    # Read the size of the maze.
    num_rows, num_cols = read_pair_of_numbers(file)
    maze = Maze(num_rows, num_cols)

    # Read the starting and exit positions.
    row, col = read_pair_of_numbers(file)
    maze.set_start(row, col)
    row, col = read_pair_of_numbers(file)
    maze.set_exit(row, col)

    # Read the maze itself.
    for row in range(num_rows) :
        line = file.readline()
        for col in range(len(line)) :
            if line[col] == "*" :
                maze.set_wall(row, col)
    file.close()
    return maze

if __name__ == "__main__":
    main()
