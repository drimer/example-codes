Given a string with no line breaks return a list of strings such that
each substring adheres to a maximum line length. Break on word
boundaries.

def split_lines(input_string, length):
    """
    >>> split_lines("i am a big lovely string", 6)
    ["i am a", "big", "lovely", "string"]
    """

What is the time and space complexity of your solution? How would you
test this code? What edge cases should you consider?

If the candidate does well, you then continue: instead of breaking on
word boundaries, we want to break words with a hyphen:

def split_lines(input_string, length):
    """
    >>> split_lines("i am a big delicious string", 6)
    ["i am a", "big d-", "elici-", "ous s-", "tring"]
    """

What is the time and space complexity of your solution? How would you
test this code? What edge cases should you consider?
