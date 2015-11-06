from StringIO import StringIO
from unittest import TestCase

from total_price import calculate_total_price


class CalculateTotalPriceTest(TestCase):
    def test_that_sums_all_values(self):
        file_str = (
            'First Product 2 300\n'
            'Second Product 4 500\n'
            '\n'
            'Third Product 1 200\n'
            'A comment\n'
        )
        input_file = StringIO(file_str)
        price = calculate_total_price(input_file)

        expected_price = 2 * 300 + 4 * 500 + 1 * 200
        self.assertEqual(expected_price, price)
