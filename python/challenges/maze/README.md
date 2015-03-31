# Introduction

The aim of the assignment is to work out routes through a maze to find a goal.

# Mazes

Mazes are expressed using the following syntax:

* `0` = clear path
* `#` = wall
* `G` = the goal

They are always rectangular but their size varies. The player will always start in the top left corner of the maze 
which will always be a clear path square.

A very simple example of a maze is:
     
    0###
    00G#
    ####

# Solutions

Solutions are expressed as a string of characters using the following syntax:

* `U` = up
* `D` = down
* `L` = left
* `R` = right

The solution to the above example would be:
    
    DRR

# The Assignment

To assignment is to create two functions:

1. `solve_maze(maze_string)` - takes in a string representation of a maze with rows separated by newlines (`\n`). It should
returns the solution to the maze as a string in the format described above.

2. `validate_maze_solution(maze_string, solution)` - takes in a string representation of a maze along with a solution and 
returns `True` if the solution is valid (and `False` otherwise).
   
# More Detailed Examples

A maze with a single route:

    0#####
    0#000#
    000#0#
    ####0#
    ####0G
    
    # Solution
    DDRRURRDDDR

A maze with multiple routes (note, your code only needs to provide a single possible solution):
    
    00#0###00
    00#000000
    0000#0#00
    00###0#00
    00###0G00
    
    # Possible solution
    DDDDRUURRURRDDDR