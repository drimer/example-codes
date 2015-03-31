from src.common import Maze


def solve_maze(maze_string):
    maze = Maze(maze_string)
    return maze.solve()
