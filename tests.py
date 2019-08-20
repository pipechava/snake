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

sh, sw = s.getmaxyx()
print(s.getmaxyx())
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)