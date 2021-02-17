"""
Snake Part 05

Author:  Chris Trotzky
         https://www.ChrisTrotzky.de

License: Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
         http://creativecommons.org/licenses/by-sa/4.0/
"""
import curses

# initialize the curses module and keep a variable
# for interaction with the screen
screen = curses.initscr()

# Set the input cursor to invisible
curses.curs_set(0)

# Determine center position for the snake head
screen_height, screen_width = screen.getmaxyx()  # NB: 2 return values!
center_line = int(screen_height / 2)             # NB: Conversion to int (not needed in python2)
center_column = int(screen_width / 2)

# draw some items on the screen
# first argument: line
# second: column
screen.addch(center_line, center_column, curses.ACS_CKBOARD)  # snake body 1
screen.addch(center_line, center_column - 1, curses.ACS_CKBOARD)  # snake body 2
screen.addch(center_line, center_column - 2, curses.ACS_CKBOARD)  # snake body 3
screen.addch(5, 5, curses.ACS_DIAMOND)  # foot
screen.refresh()

# wait for keyboard input (and discard the result)
screen.getch()

# safely shut down the application as described in the Python doc
curses.nocbreak()
screen.keypad(False)
curses.echo()
curses.endwin()
