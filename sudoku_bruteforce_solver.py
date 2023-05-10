from sudoku_puzzles.pppuzzles import *
from sudoku_puzzles.gm_puzzles import *

ROWS = 9
COLS = 9
recursion_counter = 0
changed_value_counter = 0
dead_end_counter = 0
longest_backtrace = 0
# guess_counter = 0

is_backtracking = False
curr_backtrace_depth = 0


def find_empty_cell(board):
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 0:
                return row, col
    return None


def is_valid_entry(board, number, position):
    entry_row, entry_col = position
    # check rows
    for row in range(ROWS):
        if board[row][entry_col] == number:
            return False

    # check columns
    for col in range(COLS):
        if board[entry_row][col] == number:
            return False

    # check enclosing grid
    grid_starting_row = 3 * (entry_row//3)
    grid_starting_col = 3 * (entry_col//3)
    grid_ending_row = grid_starting_row + 3
    grid_ending_col = grid_starting_col + 3
    for row in range(grid_starting_row, grid_ending_row):
        for col in range(grid_starting_col, grid_ending_col):
            if board[row][col] == number:
                return False

    return True


def update_backtracking_metrics():
    global is_backtracking, curr_backtrace_depth, dead_end_counter, longest_backtrace
    if is_backtracking:
        if curr_backtrace_depth > longest_backtrace:
            longest_backtrace = curr_backtrace_depth
        curr_backtrace_depth = 0
        dead_end_counter += 1
        is_backtracking = False


def solve(board):
    global recursion_counter, changed_value_counter, is_backtracking, curr_backtrace_depth
    update_backtracking_metrics()
    recursion_counter += 1
    empty_position = find_empty_cell(board)
    if not empty_position:
        return True
    row, col = empty_position
    for value in range(1, 10):
        if is_valid_entry(board, value, empty_position):
            board[row][col] = value
            if solve(board):
                return True
            changed_value_counter += 1
            board[row][col] = 0
    is_backtracking = True
    curr_backtrace_depth += 1
    return False


def print_board(board):
    for row in range(ROWS):
        if row != 0 and row % 3 == 0:
            print('-' * 21)
        for col in range(COLS):
            if col != 0 and col % 3 == 0:
                print("|", end=" ")
            print(board[row][col], end=" ")
        print("")
    print("")


def main():

    input_board = gm_10
    print("Input board:")
    print_board(input_board)
    print("Solved board:")
    solve(input_board)
    print_board(input_board)
    print("Recursion counter:", recursion_counter)
    print("Value change counter:", changed_value_counter)
    print("Dead end counter: ", dead_end_counter)
    print("Longest backtrace: ", longest_backtrace)


main()
