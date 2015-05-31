import mock
import unittest
from contextlib import contextmanager

import source


@contextmanager
def spy_objects_method(obj, method_name):
    original_method = getattr(obj, method_name)
    setattr(obj, method_name, mock.Mock(wraps=original_method))
    yield
    setattr(obj, method_name, original_method)


class TestDrawOnCanvas(unittest.TestCase):

    def setUp(self):
        self.line = source.Line()
        self.canvas = source.Canvas()

    def test_that_visible_figure_is_drawn(self):
        self.line.visible = True
        with spy_objects_method(self.canvas, 'draw'):
            source.draw_figure_on_canvas(self.line, self.canvas)
            self.assertTrue(self.canvas.draw.called)

    def test_that_invisible_figure_is_not_drawn(self):
        self.line.visible = False
        with spy_objects_method(self.canvas, 'draw'):
            source.draw_figure_on_canvas(self.line, self.canvas)
            self.assertFalse(self.canvas.draw.called)
