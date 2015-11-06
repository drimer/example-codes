from unittest import TestCase

from double_decorator import double_result


@double_result
def decorated_function(value):
    return value


class MyTestClass(object):
    pass


class DoubleResultTest(TestCase):
    def test_that_doubles_result_of_function(self):
        value = 5
        actual_value = decorated_function(value)

        expected_value = value * 2
        self.assertEqual(expected_value, actual_value)

    def test_that_returns_same_object_when_it_cannot_be_doubled(self):
        obj = MyTestClass()
        actual_value = decorated_function(obj)

        self.assertEqual(actual_value, obj)
