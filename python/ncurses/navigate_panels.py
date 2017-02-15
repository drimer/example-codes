"""
Example that creates three different panels with a window in each. Each
window has a title on it, and provides a way to navigate through the panels.
"""

import curses
from contextlib import contextmanager
from curses import panel

NLINES = 10
NCOLS = 40


@contextmanager
def ncurses_screen():
    screen = curses.initscr()
    yield screen
    curses.endwin()


def main():
    with ncurses_screen() as screen:
        curses.start_color()
        curses.cbreak()
        curses.noecho()
        screen.keypad(True)

        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)

        my_wins = init_wins(3)
        my_panels = [panel.new_panel(win) for win in my_wins]

        my_panels[0].set_userptr(my_panels[1])
        my_panels[1].set_userptr(my_panels[2])
        my_panels[2].set_userptr(my_panels[0])
        panel.update_panels()

        screen.attron(curses.color_pair(4))
        screen.addstr(
            curses.LINES - 2, 0,
            "Use TAB to browser through windows. F1 to exit."
        )
        screen.attroff(curses.color_pair(4))

        top = my_panels[2]
        while True:
            ch = screen.getch()
            if ch == curses.KEY_F1:
                break

            if ch == ord('9'):
                top = top.userptr()
                top.top()

            panel.update_panels()
            curses.doupdate()


def init_wins(n):
    y = 2
    x = 10
    wins = []
    for i in range(n):
        new_win = curses.newwin(NLINES, NCOLS, y, x)
        wins.append(new_win)
        label = 'This is window {}'.format(i + 1)
        win_show(new_win, label, i + 1)

        y += 3
        x += 7

    return wins


def win_show(win, label, label_color):
    starty, startx = win.getbegyx()
    height, width = win.getmaxyx()

    win.border(0, 0)

    win.addch(2, 0, curses.ACS_LTEE)
    win.hline(2, 1, curses.ACS_HLINE, width - 2)
    win.addch(2, width - 1, curses.ACS_RTEE)

    print_in_middle(win, 1, 0, width, label, curses.color_pair(label_color))


def print_in_middle(win, starty, startx, width, string, color):
    y, x = win.getyx()
    x = startx or x
    y = starty or y
    width = width or 80
    temp = (width - len(string)) / 2
    x = startx + int(temp)
    win.attron(color)
    win.addstr(y, x, string)
    win.attroff(color)

    win.refresh()


main()
