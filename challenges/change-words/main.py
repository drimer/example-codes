def can_be_consecutive(first, second):
    different_chars = 0
    for i, char in enumerate(first):
        if char != second[i]:
            different_chars += 1
            if different_chars > 1:
                return False

    return True


def words_sequence(start, end, dictionary='dictionary.txt'):
    if len(start) != len(end):
        return []

    with open(dictionary, 'r') as f:
        language = [line.strip() for line in f.readlines()]

    sequence = [start]
    language.remove(start)
    while language:
        consecutive_found = False
        for word in language:
            if can_be_consecutive(sequence[-1], word):
                sequence.append(word)
                language.remove(word)
                consecutive_found = True

                if word == end:
                    return sequence

        if not consecutive_found:
            sequence.pop()
            if sequence == []:
                break

    return sequence


### Unit tests

def test_nonexistent_sequence():
    seq = words_sequence('shirt', 'worst', dictionary='test_dict_1.txt')
    assert not seq, 'From "shirt" to "worst", found:\n%s' % seq


def test_nonexistent_sequence_different_lengths():
    seq = words_sequence('dummy', 'different')
    assert not seq, 'From "dummy" to "different", found:\n%s' % seq


def test_existing_sequence():
    seq = words_sequence('shirt', 'store')
    expected = ['shirt', 'short', 'shore', 'store']
    assert seq == expected, (
        'From "short" to "store", found:\n%sExpected: %s' % (seq, expected))

def test_existing_sequence_with_back_journeys():
    seq = words_sequence('short', 'store')
    expected = ['short', 'shore', 'store']
    assert seq == expected, (
        'From "short" to "store", found:\n%sExpected: %s' % (seq, expected))
