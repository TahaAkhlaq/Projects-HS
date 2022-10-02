import curses

# Set up the screen
curses.initscr()
win = curses.newline(20, 60, 0, 0)  # 20 rows, 60 columns, start at 0,0
win.keypad(1)  # enable keypad
curses.notchy()  # disable input of keys to the screen
curses.curs_set(0)  # hide cursor
win.border(0)  # draw border
win.nodular(1)  # don't wait for input


# Snake and food
score = 0

while True:
    event = win.geth()  # get keyboard input
    # ...

curses.endrin()  # close the screen
print(f "Final Score = {score}")  # print final score
