import heapq
import itertools
import logging
from collections import namedtuple


class PathNotFoundException(Exception):
    pass


class WrongWay(Exception):
    pass


Coordinates = namedtuple('Coordinates', ('x', 'y'))


class Cell(object):

    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.f = 0
        self.g = 0
        self.h = 0
        self.previous = None

    def __eq__(self, other):
        if isinstance(other, tuple):
            return self.coords == other

        return self.coords == (other.x, other.y)

    def __cmp__(self, other):
        return self.f - other.f

    def __repr__(self):
        return '(%s, %s, "%s")' % (self.x, self.y, self.value)

    @property
    def coords(self):
        return Coordinates(self.x, self.y)

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

        self.cells = {}

        self.add_cell(Cell(0, 0, string[0]))
        self.add_cell(self._build_goal_cell())

        self.path = [self.start]

        all_coords = itertools.product(range(self.height), range(self.width))
        self.not_visited = set(all_coords) - set([self.start])

        self.validate()

    @property
    def start(self):
        return self.cells[(0, 0)]

    @property
    def end(self):
        end_coords = self._find_goal_coords()
        return self.cells[end_coords]

    def add_cell(self, cell):
        self.cells[cell.coords] = cell

    def _find_goal_coords(self):
        before_goal = self.maze_string[:self.maze_string.find('G')]
        x = (len(before_goal) - before_goal.count('\n')) / self.width
        y = (len(before_goal) - before_goal.count('\n')) % self.width
        return (x, y)

    def _build_goal_cell(self):
        goal_coords = self._find_goal_coords()
        return Cell(goal_coords[0], goal_coords[1], 'G')

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
        cell = self.cells.get((x, y), None)
        if cell:
            return cell

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
        self.cells[(cell.x, cell.y)] = cell
        return cell

    def get_neighbour_cells(self, cell):
        candidates = []
        for new_coords in cell.get_adjacent_coords():
            cell = self.get_cell(new_coords[0], new_coords[1])
            if cell is None:
                continue

            if cell.transitable and new_coords in self.not_visited:
                candidates.append(cell)

        return candidates

    @staticmethod
    def __cost_estimate(begin, end):
        return abs(begin.x - end.x) + abs(begin.y - end.y)

    def solve(self):
        closed_set = set()
        open_set = [self.start]

        self.start.g = 0
        self.start.f = self.start.g + self.__cost_estimate(self.start, self.end)
        while open_set:
            current = heapq.heappop(open_set)
            if current.coords == self.end.coords:
                return reconstruct_path(self.end)

            closed_set.add(current)
            for neighbour in self.get_neighbour_cells(current):
                if neighbour in closed_set:
                    continue

                tentative_g_score = current.g + 1

                if neighbour not in open_set or tentative_g_score < neighbour.g:
                    neighbour.previous = current
                    neighbour.g = tentative_g_score
                    neighbour.f = neighbour.g + self.__cost_estimate(neighbour, self.end)
                    if neighbour not in open_set:
                        heapq.heappush(open_set, neighbour)

        return False

    def new_walker(self):
        return MazeWalker(self)


def reconstruct_path(end):
    steps = []
    current = end
    while current.previous is not None:
        previous = current.previous
        if previous.x < current.x:
            steps.insert(0, 'D')
        elif previous.x > current.x:
            steps.insert(0, 'U')
        elif previous.y < current.y:
            steps.insert(0, 'R')
        elif previous.y > current.y:
            steps.insert(0, 'L')
        else:
            logging.warning(
                'list_of_coords_to_steps: No difference between two steps.'
            )

        current = current.previous

    return ''.join(steps)

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
