"""
Snake Part 07B

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

head_line = center_line
head_column = center_column

mid_line = center_line
mid_column = center_column - 1

tail_line = center_line
tail_column = center_column - 2

screen.addch(head_line, head_column, curses.ACS_CKBOARD)  # snake body 1
screen.addch(mid_line, mid_column, curses.ACS_CKBOARD)  # snake body 2
screen.addch(tail_line, tail_column, curses.ACS_CKBOARD)  # snake body 3
screen.addch(5, 5, curses.ACS_DIAMOND)  # food

screen.refresh()

# wait for keyboard input and check the result!

while True:
    key = screen.getch()

    # Determine the change which needs to be applied due to the keystroke
    line_delta = 0
    column_delta = 0

    if key == curses.KEY_UP:
        line_delta = -1
    elif key == curses.KEY_DOWN:
        line_delta = 1
    elif key == curses.KEY_LEFT:
        column_delta = -1
    elif key == curses.KEY_RIGHT:
        column_delta = 1
    else:
        pass  # ignore all other keys

    # Apply the change to the snake
    screen.addch(tail_line, tail_column, " ")

    tail_line = mid_line
    tail_column = mid_column

    mid_line = head_line
    mid_column = head_column

    head_line += line_delta
    head_column += column_delta

    screen.addch(head_line, head_column, curses.ACS_CKBOARD)
