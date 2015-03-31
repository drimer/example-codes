from src.common import Maze, WrongWay


def validate_maze_solution(maze_string, solution):
    maze = Maze(maze_string)
    walker = maze.new_walker()
    for direction in solution:
        try:
            walker.step(direction)
        except WrongWay:
            return False
    current_cell = walker.get_current_cell()
    return current_cell.is_goal()
