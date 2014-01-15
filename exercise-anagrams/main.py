
class AnagramsSet:
    def __init__(self):
        self.anagrams = set()

    def add(self, word):
        sorted_word = ''.join(sorted(word))
        # Note: I don't need to store all the words because the solution is the
        # *numbers* of sets found. I only need to store the sorted word.
        # `self.anagrams` should be a simple set containing the sorted words.
        # This way, the memory usage is much lower.
        if sorted_word not in self.anagrams:
            self.anagrams.add(sorted_word)

    def __len__(self):
        return len(self.anagrams)


def lookup_anagrams_count(filepath):
    anagrams_set = AnagramsSet()

    with open(filepath) as f:
        for line in f:
            word = line.strip()
            anagrams_set.add(word)

    return len(anagrams_set)


def main():
    print lookup_anagrams_count('words1.txt')


if __name__ == '__main__':
    main()


### Unit tests

def test_3_sets_of_anagrams():
    assert lookup_anagrams_count('words1.txt') == 3


def test_empty_file():
    assert lookup_anagrams_count('words2.txt') == 0

def test_no_anagrams_found():
    assert lookup_anagrams_count('words3.txt') == 8
