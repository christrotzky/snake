# cfr https://docs.python.org/3/howto/curses.html
# cfr https://docs.python.org/3/library/curses.html

import random
import curses

screen = curses.initscr()
curses.start_color()    # Initialize the color handling
curses.curs_set(0)      # Set the input cursor to invisible

# Create a new window to have a (more or less) fixed size on all systems
screen_height, screen_width = screen.getmaxyx() # TODO: should this be updated when the window gets resized?
game_height = min(20, screen_height)
game_width = min(50, screen_width)
window = curses.newwin(game_height, game_width, 0, 0) # Create a subwindow at top left position (0, 0)
window.keypad(True)     # Let curses handle multibyte escape sequences for us

window.box(curses.ACS_VLINE, curses.ACS_HLINE)

# Initialize color pairs
food_color_pair = 1
snake_color_pair = 2
game_over_pair = 3
curses.init_pair(food_color_pair, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(snake_color_pair, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(game_over_pair, curses.COLOR_WHITE, curses.COLOR_RED)

# Initialize character attributes to reuse them later
food_attributes = curses.ACS_DIAMOND | curses.A_NORMAL | curses.color_pair(food_color_pair)
snake_attributes = curses.ACS_CKBOARD | curses.A_BOLD | curses.color_pair(snake_color_pair)
game_over_attributes = curses.A_BOLD | curses.color_pair(game_over_pair)

# Let curses wait 100 ms for reading the next character. If no character
# was entered, getch() will return -1, otherwise the recent character.
# -> This cycle is used to implement the update/life-cycle of the game.
# cfr https://docs.python.org/3/library/curses.html#curses.window.timeout
window.timeout(100)

snake_position_x = int(game_width / 4)
snake_position_y = int(game_height / 2)
snake = [ # TODO: switch X and Y as this is very confusing!
    [snake_position_y, snake_position_x],     # head
    [snake_position_y, snake_position_x - 1], # first tail element
    [snake_position_y, snake_position_x - 2]  # second tail element
]

food = [int(game_height / 2), int(game_width / 2)]
window.addch(food[0], food[1], food_attributes)

key = curses.KEY_RIGHT

# TODO: increase speed to make it more difficult over time
while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key

    touchedTopOrBottom = snake[0][0] in [1, game_height - 1]
    touchedLeftOrRight = snake[0][1] in [1, game_width -1]
    touchedSnake = snake[0] in snake[1:]

    if touchedTopOrBottom or touchedLeftOrRight or touchedSnake:
        # game over
        window.addstr(int(game_height / 2) - 1, 0,
                      "    Game Over\n    Score: " + str(len(snake) * 2) + "\n    ENTER to exit.",
                      game_over_attributes)
        # wait until the user enters the enter key
        while True:
            if window.getch() == curses.KEY_ENTER:
                curses.endwin()
                quit()
                break

    # create a new head with positions of the current head
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_UP:
        new_head[0] -= 1
    elif key == curses.KEY_DOWN:
        new_head[0] += 1
    elif key == curses.KEY_LEFT:
        new_head[1] -= 1
    elif key == curses.KEY_RIGHT:
        new_head[1] += 1
    else:
        # TODO: add error handling here? or simply ignore it?
        pass

    snake.insert(0, new_head)

    if snake[0] == food:
        # szenario: food found, so let's increate the size
        # of the snake by 1
        food = None
        while food is None:
            new_food = [
                # always keep 1 character as border in order to
                # allow collision detection
                random.randint(2, game_height - 2),
                random.randint(2, game_width - 2)
            ]
            food = new_food if new_food not in snake else None
        window.addch(food[0], food[1], food_attributes)
    else:
        # erase the last tail element in order to let the snake
        # retain its current size (scenario: no food found)
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')

    window.addch(snake[0][0], snake[0][1], snake_attributes)