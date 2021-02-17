"""
Snake Part 09

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

# Let curses wait 100 ms for reading the next character. If no character
# was entered, getch() will return -1, otherwise the recent character.
# -> This cycle is used to implement the update/life-cycle of the game.
# cfr https://docs.python.org/3/library/curses.html#curses.window.timeout
screen.timeout(100)

# Determine center position for the snake head
screen_height, screen_width = screen.getmaxyx()  # NB: 2 return values!
center_line = int(screen_height / 2)             # NB: Conversion to int (not needed in python2)
center_column = int(screen_width / 2)

# draw some items on the screen
# first argument: line
# second: column

# snake at any position [0] refers to the line and [1] to the column
snake = [[center_line, center_column], [center_line, center_column - 1], [center_line, center_column - 2]]

for segment in snake:
    screen.addch(segment[0], segment[1], curses.ACS_CKBOARD)

screen.addch(5, 5, curses.ACS_DIAMOND)  # food

screen.refresh()

# wait for keyboard input and check the result!

growth_counter = 0
previous_line_delta = 0
previous_column_delta = 1  # move to left initially

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

    # if no movement: continue to move into same direction
    if line_delta == 0 and column_delta == 0:
        line_delta = previous_line_delta
        column_delta = previous_column_delta

    # Delete tail only if no growth is to be applied
    if growth_counter % 4 != 0:
        screen.addch(snake[-1][0], snake[-1][1], " ")
        snake.pop()

    # create new head (old head position + delta)
    snake.insert(0, [snake[0][0] + line_delta, snake[0][1] + column_delta])

    screen.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

    growth_counter += 1

    previous_column_delta = column_delta
    previous_line_delta = line_delta
