from unittest import TestCase

from find_repeated_letter import find_repeated_letters


class FindRepeatedLetterTest(TestCase):
    def test_that_returns_empty_list_with_no_matches(self):
        string = 'abcdefghijklm'
        matches = find_repeated_letters(string)

        self.assertEqual([], matches)

    def test_that_returns_all_matches(self):
        string = 'Hello app user'
        matches = find_repeated_letters(string)

        expected_matches = ['ll', 'pp']
        self.assertEqual(expected_matches, matches)

    def test_that_type_error_is_raised_when_input_is_not_string(self):
        value = 4
        self.assertRaises(TypeError, find_repeated_letters, value)
