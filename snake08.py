"""
Snake Part 08

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

snake_lines = [center_line, center_line, center_line]
snake_columns = [center_column, center_column - 1, center_column - 2]

for i in range(0, len(snake_lines)):
    screen.addch(snake_lines[i], snake_columns[i], curses.ACS_CKBOARD)

screen.addch(5, 5, curses.ACS_DIAMOND)  # food

screen.refresh()

# wait for keyboard input and check the result!

growth_counter = 0

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

    # Delete tail only if no growth is to be applied
    if growth_counter % 4 != 0:
        screen.addch(snake_lines[-1], snake_columns[-1], " ")
        snake_lines.pop()
        snake_columns.pop()

    # create new head (old head position + delta)
    snake_lines.insert(0, snake_lines[0] + line_delta)
    snake_columns.insert(0, snake_columns[0] + column_delta)

    screen.addch(snake_lines[0], snake_columns[0], curses.ACS_CKBOARD)

    growth_counter += 1
