from unittest.case import TestCase

from src.common import Maze, MazeWalker, WrongWay
from src.solver import solve_maze
from src.validator import validate_maze_solution


class TestSimpleMaze(TestCase):

    def setUp(self):
        self.maze = '0##\n00G'
        self.solution = 'DRR'

    def test_solve_maze_successfully_solves_it(self):
        actual_solution = solve_maze(self.maze)
        self.assertEqual(self.solution, actual_solution)

    def test_validation_successfully_validates_maze(self):
        is_valid = validate_maze_solution(
            self.maze,
            self.solution
        )
        self.assertTrue(is_valid)


class TestComplexMaze(TestCase):

    def setUp(self):
        self.maze = '0#####\n0#000#\n000#0#\n####0#\n####0G'
        self.solution = 'DDRRURRDDDR'

    def test_too_short_solution_is_not_valid(self):
        is_valid = validate_maze_solution(self.maze, 'RRD')
        self.assertFalse(is_valid)

    def test_solve_maze_successfully_solves_it(self):
        actual_solution = solve_maze(self.maze)
        self.assertEqual(self.solution, actual_solution)

    def test_validation_successfully_validates_maze(self):
        is_valid = validate_maze_solution(
            self.maze,
            self.solution
        )
        self.assertTrue(is_valid)

    def test_wrong_solution_on_complex_maze(self):
        is_valid = validate_maze_solution(self.maze, 'DDRR')
        self.assertFalse(is_valid)


class TestMultiPathMaze(TestCase):

    def setUp(self):
        self.maze = '00#0###00\n00#000000\n0000#0#00\n00###0#00\n00###0G00'
        self.solution = 'RDDRRURRDDDR'

    def test_solve_maze_returns_valid_path(self):
        solution = solve_maze(self.maze)
        self.assertTrue(validate_maze_solution(self.maze, solution))

    def test_validate_possible_solution(self):
        is_valid = validate_maze_solution(
            self.maze,
            self.solution
        )
        self.assertTrue(is_valid)

    def test_validate_wrong_solution(self):
        is_valid = validate_maze_solution(self.maze, 'DDD')
        self.assertFalse(is_valid)


class TestMazeCreation(TestCase):

    def test_creation_with_irregular_shape_raises_exception(self):
        self.assertRaises(Exception, Maze, '0\n00#\n0')

    def test_creation_with_wrong_characters_raises_exception(self):
        self.assertRaises(Exception, Maze, 'RR#\nRG#\n###')


class TestMazeWalkerSteps(TestCase):

    def setUp(self):
        self.maze = Maze('0#0\n0##\nG##')
        self.walker = MazeWalker(self.maze)

    def test_step_into_a_wall_raises_exception(self):
        self.assertRaises(WrongWay, self.walker.step, 'R')

    def test_step_out_of_the_maze(self):
        self.assertRaises(WrongWay, self.walker.step, 'U')

    def test_setp_to_a_valid_cell_updates_position(self):
        self.walker.step('D')
        self.assertEqual(
            self.walker.get_current_cell().coords,
            (1, 0)
        )
