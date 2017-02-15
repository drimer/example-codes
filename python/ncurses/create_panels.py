"""
Example that creates three panels with a window in each. It displays
them and waits for user's input before finishing execution.
"""

import curses
from curses import panel

screen = curses.initscr()
curses.cbreak()
curses.noecho()

lines = 10
cols = 40
y = 2
x = 4

windows = [
    curses.newwin(lines, cols, y, x),
    curses.newwin(lines, cols, y + 1, x + 5),
    curses.newwin(lines, cols, y + 2, x + 10),
]

for window in windows:
    window.border(0, 0)

panels = [panel.new_panel(window) for window in windows]
panel.update_panels()
curses.doupdate()

screen.getch()
curses.endwin()
