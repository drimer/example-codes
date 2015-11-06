#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

CURRENCY_SYMBOLS = '$£'


def get_price_from_file_line(line):
    splitted = line.split()
    if len(splitted) >= 2:
        currency_price_str = splitted[-1]
        quantity_str = splitted[-2]
        price_str = currency_price_str.lstrip(CURRENCY_SYMBOLS)

        try:
            price = float(price_str)
            quantity = float(quantity_str)

            if quantity >= 0:
                return price * quantity
        except ValueError:
            return None

    return None


def calculate_total_price(input_file):
    total_price = 0

    for line in input_file:
        price = get_price_from_file_line(line)
        if price is not None:
            total_price += price

    return total_price


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str,
                        help='Text file containing the bill')
    return parser.parse_args()


def main(opts):
    with open(opts.input_file, 'r') as f:
        total_price = calculate_total_price(f)
    print 'Total price %.2f' % total_price


if __name__ == '__main__':
    opts = parse_args()
    main(opts)
