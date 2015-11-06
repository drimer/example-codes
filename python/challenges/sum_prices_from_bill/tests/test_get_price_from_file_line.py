from unittest import TestCase

from total_price import get_price_from_file_line, CURRENCY_SYMBOLS


class GetPriceFromFileLineTest(TestCase):
    def test_that_returns_none_when_line_does_not_contain_price(self):
        line = 'Apple iPhone Plus 2'
        price = get_price_from_file_line(line)

        self.assertIsNone(price)

    def test_that_returns_none_when_line_does_not_contain_quantity(self):
        line = 'First product'
        price = get_price_from_file_line(line)

        self.assertIsNone(price)

    def test_that_returns_none_when_line_contains_wrong_value_as_quantity(self):
        line = 'First product wrong %s300.00' % CURRENCY_SYMBOLS[0]
        price = get_price_from_file_line(line)

        self.assertIsNone(price)

    def test_that_returns_none_when_quantity_is_negative(self):
        line = 'First produuct -2 %s200.00' % CURRENCY_SYMBOLS[0]
        price = get_price_from_file_line(line)

        self.assertIsNone(price)

    def test_that_returns_none_with_empty_line(self):
        price = get_price_from_file_line('')

        self.assertIsNone(price)

    def test_that_returns_correct_pricec_when_line_has_price(self):
        line_price = 200.0
        line_quantity = 3
        price_str = '%s%s' % (CURRENCY_SYMBOLS[0], line_price)
        line = 'Apple iPhone Plus %s %s' % (line_quantity, price_str)
        price = get_price_from_file_line(line)

        expected_price = line_quantity * line_price
        self.assertEqual(expected_price, price)
