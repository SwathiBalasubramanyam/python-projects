import curses
from curses import wrapper
import queue
import time


maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]


def find_shortest_path():
    DIRS = [(1,0), (-1, 0), (0, -1), (0, 1)]
    ROWS = len(maze)
    COLS = len(maze[0])
    shortest_path = None

    def _dfs(row, col, path):
        nonlocal shortest_path

        if maze[row][col] == "X":
            if not shortest_path or len(path) < len(shortest_path):
                shortest_path = path.copy()
            return


        for dir in DIRS:
            new_row = row + dir[0]
            new_col = col + dir[1]
            if 0 <= new_row < ROWS and 0<= new_col < COLS and maze[new_row][new_col] in (" ", "X"):
                backtrack = False
                if maze[new_row][new_col] == " ":
                    maze[new_row][new_col] = "#"
                    backtrack = True

                _dfs(new_row, new_col, path + [(new_row, new_col)])

                if backtrack:
                    maze[new_row][new_col] = " "

    for row_num in range(ROWS):
        for col_num in range(COLS):
            if maze[row_num][col_num] != "O":
                continue
            _dfs(row_num, col_num, [(row_num, col_num)])
            break

    return shortest_path


def print_maze(maze, stdscr, path=[]):
    blue = curses.color_pair(1)
    red = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, val in enumerate(row):
            stdscr.addstr(i,j*2, "." if (i,j) in path and val not in ("#", "O", "X") else val, red if (i,j) in path else blue)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.clear()
    print_maze(maze, stdscr, find_shortest_path())
    stdscr.refresh()
    stdscr.getch()


wrapper(main)