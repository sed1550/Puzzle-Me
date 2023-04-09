from sudokupuzzles import *


ROWS = 9
COLS = 9
recursion_counter = 0
changed_value_counter = 0


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


def solve(board):
    global recursion_counter, changed_value_counter
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

    input_board = sudoku_3star_2
    print("Input board:")
    print_board(input_board)
    print("Solved board:")
    solve(input_board)
    print_board(input_board)
    print("Recursion counter:", recursion_counter)
    print("Value change counter:", changed_value_counter)


main()
