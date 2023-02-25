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
    possible_values_dict = {}
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 0:
                possible_values_list = get_possible_values_list(board, row, col)
                possible_values_dict[(row, col)] = possible_values_list


def find_least_possible_values_cell():
    for row in range(ROWS):
        for col in range(COLS):
            pass


def solve():
    pass


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
    print("Solved:")
    # solve(input_board)
    print_board(input_board)


main()
