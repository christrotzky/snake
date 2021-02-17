"""
Snake Part 06

Author:  Chris Trotzky
         https://www.ChrisTrotzky.de

License: Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
         http://creativecommons.org/licenses/by-sa/4.0/
"""
import curses

# initialize the curses module and keep a variable
# for interaction with the screen
screen = curses.initscr()
screen.keypad(True)     # Let curses handle multibyte escape sequences for us

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
screen.addch(5, 5, curses.ACS_DIAMOND)  # food
# screen.refresh()

# wait for keyboard input and check the result!
key = screen.getch()

if key == curses.KEY_UP:
    screen.addch(center_line - 1, center_column, curses.ACS_CKBOARD)
    screen.addch(center_line, center_column - 2, " ")
elif key == curses.KEY_DOWN:
    screen.addch(center_line + 1, center_column, curses.ACS_CKBOARD)
    screen.addch(center_line, center_column - 2, " ")
elif key == curses.KEY_LEFT:
    pass  # makes no sense as the snake is entirely horizontal -> ignore
elif key == curses.KEY_RIGHT:
    screen.addch(center_line, center_column + 1, curses.ACS_CKBOARD)
    screen.addch(center_line, center_column - 2, " ")
else:
    # for all other keys, use the same code as in the key_right case
    # (the snake has a natural movement into the current direction)
    screen.addch(center_line, center_column + 1, curses.ACS_CKBOARD)
    screen.addch(center_line, center_column - 2, " ")

# let's wait for the next keystroke before exit
screen.getch()

# safely shut down the application as described in the Python doc
curses.nocbreak()
screen.keypad(False)
curses.echo()
curses.endwin()
