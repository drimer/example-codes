

def words_sequence(start, end, dictionary='dictionary.txt'):
    pass


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
