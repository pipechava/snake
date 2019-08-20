import curses
import os
import random

#setup envirorment to open terminal window
os.environ.setdefault("TERM", "linux")

#initialize the screen and window size

#initialize screen
s = curses.initscr()
#set the blinking cursos in terminal, if cero then no cursor
curses.curs_set(0)

#set the values of screen height and screen width to the current size of the termianl window
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)

#escape sequence, if 1 escape sequence will be another thing, if 0 press of keys will exit program
w.keypad(1)

#speed of the snake, the less the number the faster the snake
w.timeout(50)

snk_x = sw // 4
snk_y = sh // 2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [sh // 2, sw // 2]

#adds food for the snake
w.addch(food[0], food[1], "*")

key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None

        #add new food for snake
        w.addch(food[0], food[1], "*")
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(snake[0][0], snake[0][1], "=")
