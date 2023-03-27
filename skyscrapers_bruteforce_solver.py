from skyscraperspuzzles import *

SIZE = 4


def find_empty_cell(board):
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] == 0:
                return row, col
    return None


def get_skyscrapers_count_north(value, board, cell_row, cell_col):
    max_value = 0
    count = 0
    for row in range(cell_row):
        curr_value = board[row][cell_col]
        if curr_value > max_value:
            count += 1
            max_value = curr_value
    if value > max_value:
        count += 1
    return count


def get_skyscrapers_count_west(value, board, cell_row, cell_col):
    max_value = 0
    count = 0
    for col in range(cell_col):
        curr_value = board[cell_row][col]
        if curr_value > max_value:
            count += 1
            max_value = curr_value
    if value > max_value:
        count += 1
    return count


def get_skyscrapers_count_east(value, board, cell_row):
    max_value = value
    count = 1
    for col in range(SIZE-2, -1, -1):
        curr_value = board[cell_row][col]
        if curr_value > max_value:
            count += 1
            max_value = curr_value
    return count


def get_skyscrapers_count_south(value, board, cell_col):
    max_value = value
    count = 1
    for row in range(SIZE-2, -1, -1):
        curr_value = board[row][cell_col]
        if curr_value > max_value:
            count += 1
            max_value = curr_value
    return count


def is_valid_value(value, borders, board, cell_row, cell_col):
    # check column
    for row in range(SIZE):
        if board[row][cell_col] == value:
            return False

    # check row
    for col in range(SIZE):
        if board[cell_row][col] == value:
            return False

    # check borders
    # check north view
    n_border = borders[0][cell_col]
    if n_border:
        n_count = get_skyscrapers_count_north(value, board, cell_row, cell_col)
        if n_count > n_border:
            return False

    # check west view
    w_border = borders[3][cell_row]
    if w_border:
        w_count = get_skyscrapers_count_west(value, board, cell_row, cell_col)
        if w_count > w_border:
            return False

    # check east view
    if cell_col == SIZE-1:
        e_border = borders[1][cell_row]
        if e_border:
            e_count = get_skyscrapers_count_east(value, board, cell_row)
            if e_count > e_border:
                return False

    # check south view
    if cell_row == SIZE-1:
        s_border = borders[2][cell_col]
        if s_border:
            s_count = get_skyscrapers_count_south(value, board, cell_col)
            if s_count > s_border:
                return False

    return True


def print_board(borders, board):
    n_view = borders[0]
    e_view = borders[1]
    s_view = borders[2]
    w_view = borders[3]
    # Print north view first
    for n_col in range(SIZE):
        if not n_col:
            print("   ", n_view[n_col], end="")
        else:
            print(" |", n_view[n_col], end="")
    print("")
    # Print board along with west and east views
    for row in range(SIZE):
        print(w_view[row], end=" | ")
        for col in range(SIZE):
            print(board[row][col], end=" | ")
        print(e_view[row])
    # Print south view last
    for s_col in range(SIZE):
        if not s_col:
            print("   ", s_view[s_col], end="")
        else:
            print(" |", s_view[s_col], end="")
    print("")


def solve(borders, board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
    cell_row, cell_col = empty_cell
    for value in range(1, SIZE + 1):
        if is_valid_value(value, borders, board, cell_row, cell_col):
            board[cell_row][cell_col] = value
            if solve(borders, board):
                return True
            board[cell_row][cell_col] = 0
    return False


def main():
    input_borders = skyscrapers_borders_2
    input_board = skyscrapers_board_2
    print("Input board:")
    print_board(input_borders, input_board)
    solve(input_borders, input_board)
    print("\nSolved board:")
    print_board(input_borders, input_board)


main()
