from sudoku_puzzles.pppuzzles import *
from sudoku_puzzles.gm_puzzles import *

ROWS = 9
COLS = 9
recursion_counter = 0
changed_value_counter = 0
dead_end_counter = 0
longest_backtrace = 0
guess_counter = 0

is_backtracking = False
curr_backtrace_depth = 0


def is_valid_value(value, board, cell_row, cell_col):
    # cell_row, cell_col = position
    # check rows
    for row in range(ROWS):
        if board[row][cell_col] == value:
            return False

    # check columns
    for col in range(COLS):
        if board[cell_row][col] == value:
            return False

    # check enclosing grid
    grid_starting_row = 3 * (cell_row // 3)
    grid_starting_col = 3 * (cell_col // 3)
    grid_ending_row = grid_starting_row + 3
    grid_ending_col = grid_starting_col + 3
    for row in range(grid_starting_row, grid_ending_row):
        for col in range(grid_starting_col, grid_ending_col):
            if board[row][col] == value:
                return False

    return True


def get_possible_values_list(board, row, col):
    possible_values = []
    for value in range(1, 10):
        if is_valid_value(value, board, row, col):
            possible_values.append(value)
    return possible_values


def record_possible_values_for_empty_cells(board):
    possible_values_tracker = {}
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 0:
                possible_values_list = get_possible_values_list(board, row, col)
                possible_values_tracker[(row, col)] = possible_values_list
    return possible_values_tracker


def find_least_possible_values_cell(board, possible_values_tracker):
    # initialize default values
    least_number_of_possible_values = 9
    cell_position = None
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 0:
                current_cell_possible_values_list = possible_values_tracker[(row, col)]
                current_possible_values_num = len(current_cell_possible_values_list)
                if current_possible_values_num < least_number_of_possible_values:
                    least_number_of_possible_values = current_possible_values_num
                    cell_position = row, col
    return cell_position


def update_backtracking_metrics():
    global is_backtracking, curr_backtrace_depth, dead_end_counter, longest_backtrace
    if is_backtracking:
        if curr_backtrace_depth > longest_backtrace:
            longest_backtrace = curr_backtrace_depth
        curr_backtrace_depth = 0
        dead_end_counter += 1
        is_backtracking = False


def solve_with_mrv(board):
    global recursion_counter, changed_value_counter, guess_counter, is_backtracking, curr_backtrace_depth
    update_backtracking_metrics()
    recursion_counter += 1
    possible_values_tracker = record_possible_values_for_empty_cells(board)
    # print(possible_values_tracker)
    # print("# empty cells for current board:", len(possible_values_tracker))
    empty_cell = find_least_possible_values_cell(board, possible_values_tracker)
    if not empty_cell:
        return True
    empty_cell_pv_list = possible_values_tracker.get(empty_cell)
    empty_cell_row, empty_cell_col = empty_cell
    for idx in range(len(empty_cell_pv_list)):
        board[empty_cell_row][empty_cell_col] = empty_cell_pv_list[idx]
        if len(empty_cell_pv_list) > 1 and idx != len(empty_cell_pv_list)-1:
            guess_counter += 1
        if solve_with_mrv(board):
            return True
        changed_value_counter += 1
        board[empty_cell_row][empty_cell_col] = 0
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
    input_board = pp_12
    print("Input board:")
    print_board(input_board)
    solve_with_mrv(input_board)
    print("\nSolved board:")
    print_board(input_board)
    print("Recursion counter:", recursion_counter)
    print("Value change counter:", changed_value_counter)
    print("Guess counter: ", guess_counter)
    print("Dead end counter: ", dead_end_counter)
    print("Longest backtrace: ", longest_backtrace)


main()
