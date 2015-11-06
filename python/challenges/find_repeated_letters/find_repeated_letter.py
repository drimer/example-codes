import re


def find_repeated_letters(string):
    matches = re.findall(r'((\w)\2{1,})', string)
    return [match[0] for match in matches]
