Given a file "words1.txt" with a list of unsorted lower-case words, one
per line, we want to write a program that looks for all the anagrams
existing in the list and prints out the number of the identified
groups of anagrams.

For example, the file may contain::

    there
    dare
    thing
    read
    night
    three
    dear


In which case, the expected output would be 3::

    1st set: there, three
    2nd set: dare, read, dear
    3rd set: thing, night
