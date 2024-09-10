import random
import time
import curses
from curses import wrapper


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to this typing test! \nYou'll be given a block of text and need to type it as fast as possible.", curses.color_pair(3))
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.clear()
    stdscr.addstr(target)
    stdscr.addstr(1,0, f"WPM: {wpm}")
    for i, char in enumerate(current):
        stdscr.addstr(0, i, char, curses.color_pair(1) if char == target[i] else curses.color_pair(2))
    stdscr.refresh()

def load_text():
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def wpm_test(stdscr):
    target_text = load_text()
    curr_text = []
    wpm = 0
    start_time = time.time()

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round(len(curr_text)*60/time_elapsed/5)

        display_text(stdscr, target_text, curr_text, wpm=wpm)

        if target_text == "".join(curr_text):
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if key in ("KEY_BACKSPACE", '\b', '\x7f'):
            if curr_text:
                curr_text.pop()
        elif len(curr_text) < len(target_text):
            curr_text.append(key)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2,0, "You completed the text! Press any key to continue...")
        key = stdscr.getkey()

        if ord(key) == 27:
            break

wrapper(main)
