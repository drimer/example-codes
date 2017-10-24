Description of the problem solved
=================================

A user has to reset his or her password. We'll write a script in Python, which​
takes​ ​ as​ ​ input​ ​ two​ ​ strings​ ​ (password​ ​ and​ ​ confirm​ ​ password),​ ​ and​
checks​ ​ whether:
- The​ ​ two​ ​ strings​ ​ are​ ​ similar
- The​ ​ password​ ​ has​ ​ at​ ​ least​ ​ 8 ​ ​ characters
- The​ ​ password​ ​ has​ ​ at​ ​ least​ ​ one​ ​ lowercase​ ​ letter
- The​ ​ password​ ​ has​ ​ at​ ​ least​ ​ one​ ​ uppercase​ ​ letter
- The​ ​ password​ ​ has​ ​ at​ ​ least​ ​ one​ ​ number
If​ ​ all​ ​ 5 ​ ​ above​ ​ conditions​ ​ are​ ​ met,​ ​ the​ ​ script​ ​ should​ ​print a success message
and return a 0 status code. Otherwise,​ ​ it​ ​ should​ print an error message and​ return​ a
-1 status code.

Steps to set up
===============

- Install Python 3
- (optional) Make a virtual environment: `mkvirtualenv -p $(which python3) criton`
- `pip install -r requirements.txt`

Running the app
===============

`python main.py <new-password> <new-password>`

Running the tests
=================

- `pip install -r dev_requirements.txt`
- `pytest`

