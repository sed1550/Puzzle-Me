ROWS = 9
COLS = 9


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


def solve_with_mrv(board):
    print("New board:")
    print_board(board)
    possible_values_tracker = record_possible_values_for_empty_cells(board)
    print(possible_values_tracker)
    empty_cell = find_least_possible_values_cell(board, possible_values_tracker)
    if not empty_cell:
        return True
    print(empty_cell)
    empty_cell_pv_list = possible_values_tracker.get(empty_cell)
    empty_cell_row, empty_cell_col = empty_cell
    for value in empty_cell_pv_list:
        board[empty_cell_row][empty_cell_col] = value
        # check is_valid_value?
        if solve_with_mrv(board):
            return True
        board[empty_cell_row][empty_cell_col] = 0
    return False


def print_board(board):
    for row in range(ROWS):
        if row != 0 and row % 3 == 0:
            print('_' * 21)
        for col in range(COLS):
            if col != 0 and col % 3 == 0:
                print("|", end=" ")
            print(board[row][col], end=" ")
        print("")


def main():
    # 2-star difficulty
    input_board = [[0, 0, 0, 2, 5, 1, 0, 0, 0],
                   [0, 0, 0, 9, 0, 6, 0, 0, 0],
                   [0, 0, 7, 0, 0, 0, 1, 0, 0],
                   [0, 0, 3, 0, 1, 0, 4, 0, 0],
                   [0, 1, 0, 8, 0, 7, 0, 9, 0],
                   [0, 7, 0, 5, 9, 4, 0, 1, 0],
                   [0, 3, 0, 0, 0, 0, 0, 2, 0],
                   [8, 0, 0, 7, 2, 5, 0, 0, 3],
                   [9, 2, 5, 0, 0, 0, 8, 7, 4]]

    print_board(input_board)
    solve_with_mrv(input_board)
    print("Solved:")
    print_board(input_board)


main()
