import itertools
import logging


class PathNotFoundException(Exception):
    pass


class WrongWay(Exception):
    pass


class Cell(object):

    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    def __eq__(self, other):
        if isinstance(other, tuple):
            return self.coords == other

        return self.coords == (other.x, other.y)

    def __repr__(self):
        return '(%s, %s, "%s")' % (self.x, self.y, self.value)

    @property
    def coords(self):
        return (self.x, self.y)

    @property
    def transitable(self):
        return self.value in ('0', 'G')

    def is_goal(self):
        return self.value == 'G'

    def get_adjacent_coords(self):
        adj_coords = (
            (self.x + 1, self.y),
            (self.x - 1, self.y),
            (self.x, self.y + 1),
            (self.x, self.y - 1),
        )
        return adj_coords


class Maze(object):

    def __init__(self, string):
        self.maze_string = string

        self.grid = string.split()
        self.width = len(self.grid[0])
        self.height = len(self.grid)

        self.start = (0, 0)
        self.path = [self.start]

        all_coords = itertools.product(range(self.height), range(self.width))
        self.not_visited = set(all_coords) - set([self.start])
        self.end = self.find_goal_coords()

        self.validate()

    def find_goal_coords(self):
        before_goal = self.maze_string[:self.maze_string.find('G')]
        x = (len(before_goal) - before_goal.count('\n')) / self.width
        y = (len(before_goal) - before_goal.count('\n')) % self.width
        return (x, y)

    def __repr__(self):
        return self.maze_string

    def validate(self):
        row_sizes = set([len(row) for row in self.maze_string.split()])
        assert len(row_sizes) == 1
        assert self.end is not None

        valid_chars = ('G', '0', '#')
        all_chars = ''.join(self.grid)
        assert all(c in valid_chars for c in all_chars)

    def get_cell(self, x, y, default=None):
        invalid_coords = (
            x >= self.height
            or y >= self.width
            or x < 0
            or y < 0
        )
        if invalid_coords:
            return default

        value = self.grid[x][y]
        cell = Cell(x, y, value)
        return cell

    def possible_next_cells(self):
        cur_coords = self.path[-1]
        cur_cell = self.get_cell(cur_coords[0], cur_coords[1])

        candidates = []
        for new_coords in cur_cell.get_adjacent_coords():
            cell = self.get_cell(new_coords[0], new_coords[1])
            if cell is None:
                continue

            if cell.transitable and new_coords in self.not_visited:
                candidates.append(cell)

        return candidates

    def compute_path_into_steps(self):
        steps = []
        for prev, new in zip(self.path[:-1], self.path[1:]):
            if new[0] > prev[0]:
                steps.append('D')
            elif new[0] < prev[0]:
                steps.append('U')
            elif new[1] > prev[1]:
                steps.append('R')
            elif new[1] < prev[1]:
                steps.append('L')
            else:
                logging.warning(
                    'list_of_coords_to_steps: No difference between two steps.'
                )

        return ''.join(steps)

    def solve(self):
        while True:
            if len(self.not_visited) == 0:
                break

            consecutive_found = False
            candidates = self.possible_next_cells()
            if not candidates:
                self.path.pop()
                continue
            next_cell = candidates[0]
            self.path.append(next_cell.coords)
            self.not_visited.discard(next_cell.coords)
            consecutive_found = True

            if next_cell == self.end:
                return self.compute_path_into_steps()
                #return self.path

            if not consecutive_found:
                self.path.pop()
                if self.path == []:
                    break

        return self.compute_path_into_steps()

    def new_walker(self):
        return MazeWalker(self)


class MazeWalker(object):

    def __init__(self, maze):
        self.maze = maze
        self.cur_coords = (0, 0)

    def step(self, direction):
        assert direction in ('U', 'D', 'L', 'R')

        cur_coords = self.cur_coords
        logging.debug('Maze: %s', self.maze)
        logging.debug('=> Walking towards %s from %s', direction, cur_coords)

        if direction == 'U':
            new_coords = (cur_coords[0] - 1, cur_coords[1])
        elif direction == 'D':
            new_coords = (cur_coords[0] + 1, cur_coords[1])
        elif direction == 'L':
            new_coords = (cur_coords[0], cur_coords[1] - 1)
        elif direction == 'R':
            new_coords = (cur_coords[0], cur_coords[1] + 1)
        else:
            raise Exception('Wrong step format: %s' % direction)

        new_cell = self.maze.get_cell(new_coords[0], new_coords[1])
        if new_cell is None or new_cell.value not in ('0', 'G'):
            raise WrongWay(
                'Invalid step taken in direction "%s" from location %s' % (
                    direction, cur_coords
                )
            )

        self.cur_coords = new_coords

    def get_current_cell(self):
        return self.maze.get_cell(*self.cur_coords)
