import nose
import re


def split_lines(text, length):
    split_lines = []
    while text:
        text = text.lstrip(' ')
        if len(text) <= length:
            split_lines.append(text)
            break

        if text[length-2] == ' ' and text[length - 1] != ' ' and text[length] != ' ':
            line = text[:length-2]  # i.e. "is a bug" with length=6
        elif text[length-2] != ' ' and text[length - 1] != ' ' and text[length] != ' ':
            line = text[:length-1] + '-'  # i.e. "is one" with length=4
        else:
            line = text[:length]

        text = text.lstrip(line)
        split_lines.append(line)

    return split_lines


if __name__ == '__main__':
    print split_lines('This is a fairly long string', 7)


### Unit tests

def test_shortest_than_maximum():
    assert split_lines('Short', 10) == ['Short']


def test_text_of_exactly_max_length():
    assert split_lines('Short', 5) == ['Short']


def test_text_one():
    assert split_lines('This is a fairly long text', 6) == \
        ['This', 'is a', 'fairly', 'long', 'text']


def test_text_two():
    assert split_lines('I am a big delicious string', 6) == \
        ['I am a', 'big d-', 'elici-', 'ous s-', 'tring']
