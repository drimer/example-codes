def split_lines(text, length):
    return [text]


if __name__ == '__main__':
    print split_lines('This is a fairly long string', 6)


### Unit tests

def test_shortest_than_maximum():
    assert split_lines('Short', 10) == ['Short']


def test_text_of_exactly_max_length():
    assert split_lines('Short', 5) == ['Short']
