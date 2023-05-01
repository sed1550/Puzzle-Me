from skyscraperspuzzles import *

SIZE = 4
recursion_counter = 0
changed_value_counter = 0


def check_north_view(value, border_value, board, cell_row, cell_col):
    max_value = 0
    count = 0
    for row in range(SIZE):
        curr_value = board[row][cell_col]
        if row == cell_row:
            curr_value = value
        if not curr_value:
            break
        if curr_value > max_value:
            count += 1
            max_value = curr_value
        if row == SIZE-1 and count != border_value:
            return False

    if count > border_value:
        return False
    return True


def check_south_view(value, border_value, board, cell_row, cell_col):
    max_value = 0
    count = 0
    for row in range(SIZE-1, -1, -1):
        curr_value = board[row][cell_col]
        if row == cell_row:
            curr_value = value
        if not curr_value:
            break
        if curr_value > max_value:
            count += 1
            max_value = curr_value
        if row == 0 and count != border_value:
            return False

    if count > border_value:
        return False
    return True


def check_west_view(value, border_value, board, cell_row, cell_col):
    max_value = 0
    count = 0
    for col in range(SIZE):
        curr_value = board[cell_row][col]
        if col == cell_col:
            curr_value = value
        if not curr_value:
            break
        if curr_value > max_value:
            count += 1
            max_value = curr_value
        if col == SIZE-1 and count != border_value:
            return False

    if count > border_value:
        return False
    return True


def check_east_view(value, border_value, board, cell_row, cell_col):
    max_value = 0
    count = 0
    for col in range(SIZE-1, -1, -1):
        curr_value = board[cell_row][col]
        if col == cell_col:
            curr_value = value
        if not curr_value:
            break
        if curr_value > max_value:
            count += 1
            max_value = curr_value
        if col == 0 and count != border_value:
            return False

    if count > border_value:
        return False
    return True


def is_valid_value(value, borders, board, cell_row, cell_col):
    # print("Value")
    # print(value)
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
        if not check_north_view(value, n_border, board, cell_row, cell_col):
            return False

    # check west view
    w_border = borders[3][cell_row]
    if w_border:
        if not check_west_view(value, w_border, board, cell_row, cell_col):
            return False

    # check east view
    e_border = borders[1][cell_row]
    if e_border:
        if not check_east_view(value, e_border, board, cell_row, cell_col):
            return False

    # check south view
    s_border = borders[2][cell_col]
    if s_border:
        if not check_south_view(value, s_border, board, cell_row, cell_col):
            return False

    return True


def get_possible_values_list(borders, board, row, col):
    possible_values = []
    for value in range(1, SIZE+1):
        if is_valid_value(value, borders, board, row, col):
            possible_values.append(value)
    return possible_values


def record_possible_values_for_empty_cells(borders, board):
    possible_values_tracker = {}
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] == 0:
                possible_values_list = get_possible_values_list(borders, board, row, col)
                possible_values_tracker[(row, col)] = possible_values_list
    return possible_values_tracker


def find_least_possible_values_cell(board, possible_values_tracker):
    # initialize default values
    least_number_of_possible_values = SIZE
    cell_position = None
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] == 0:
                current_cell_possible_values_list = possible_values_tracker[(row, col)]
                current_possible_values_num = len(current_cell_possible_values_list)
                if current_possible_values_num <= least_number_of_possible_values:
                    least_number_of_possible_values = current_possible_values_num
                    cell_position = row, col
    return cell_position


def solve_with_mrv(borders, board):
    # print_board(borders, board)
    global recursion_counter, changed_value_counter
    recursion_counter += 1
    possible_values_tracker = record_possible_values_for_empty_cells(borders, board)
    empty_cell = find_least_possible_values_cell(board, possible_values_tracker)
    if not empty_cell:
        return True
    empty_cell_pv_list = possible_values_tracker.get(empty_cell)
    empty_cell_row, empty_cell_col = empty_cell
    for value in empty_cell_pv_list:
        board[empty_cell_row][empty_cell_col] = value
        if solve_with_mrv(borders, board):
            return True
        changed_value_counter += 1
        board[empty_cell_row][empty_cell_col] = 0
    return False


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


def main():
    input_borders = skyscrapers_borders_5h2
    input_board = skyscrapers_board_5h2
    global SIZE
    SIZE = len(input_board)
    print("Input board:")
    print_board(input_borders, input_board)
    solve_with_mrv(input_borders, input_board)
    print("\nSolved board:")
    print_board(input_borders, input_board)
    print("Recursion counter:", recursion_counter)
    print("Value change counter:", changed_value_counter)


main()
