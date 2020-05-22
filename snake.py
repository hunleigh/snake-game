import random
import curses

s = curses.initscr()
curses.curs_set(0)  # initialise to 0 so it doesn't show on the screen
sh, sw = s.getmaxyx()
win = curses.newwin(sh, sw, 0, 0)  # create new window starting at top left
win.keypad(1)
win.timeout(100)

# snake initial conditions

x_s = int(sh/4)
y_s = int(sw/2)

snake = [
    [y_s, x_s],
    [y_s, x_s - 1],
    [y_s, x_s - 2]
]

cur_key = curses.KEY_RIGHT

# initialise food at center

food = [int(sh/2), int(sw/2)]

win.addch(int(food[0]), int(food[1]), curses.ACS_PI)  # add food to the screen

"""
start game
"""
while True:
    next_key = win.getch()
    cur_key = cur_key if next_key == -1 else next_key

    # game ends if snake goes to the edges or in itself
    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if cur_key == curses.KEY_DOWN:
        new_head[0] += 1
    if cur_key == curses.KEY_UP:
        new_head[0] -= 1
    if cur_key == curses.KEY_LEFT:
        new_head[1] -= 1
    if cur_key == curses.KEY_RIGHT:
        new_head[0] += 1

    snake.insert(0, new_head)

    if snake[0] == food:  # if it runs into food
        food = None
        while food is None:
            new_food = [random.randint(0, sh-1), random.randint(0, sw-1)]

            food = new_food if food not in snake else None
        win.addch(int(food[0]), int(food[1]), curses.ACS_PI)
    else:
        tail = snake.pop()
        win.addch(tail[0], tail[1], ' ')

    win.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)