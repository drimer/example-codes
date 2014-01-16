import nose
import re


def split_lines(text, length):
    if max([len(word) for word in text.split()]) > length:
        raise ValueError('Careful! There is a word longer than your max '
                         'length!')

    split_lines = []
    while text:
        text = text.lstrip(' ')
        match = re.match(r'([\w\ ]){%s}(\Z)?' % length, text)
        if match:
            line = match.group()
            if ' ' in line:
                line = ' '.join(line.split(' ')[:-1])
        else:
            line = text
        split_lines.append(line)
        text = text.lstrip(line)

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


@nose.tools.raises(ValueError)
def test_word_longer_than_max_length_fails():
    split_lines('This is a text with an extremly long word', 3)
