import numpy as np
from itertools import combinations

from nonogramspuzzles import *

ROWS = 0
COLS = 0


def find_possibilities(black_groups, no_of_groups, no_of_remaining_spaces):
    possibilities = []
    no_of_slots = no_of_groups + no_of_remaining_spaces
    combs = combinations(range(no_of_slots), no_of_groups)
    # print("ITERATION")
    for combination in combs:
        possibility = []
        group_ct = 0
        for idx in range(no_of_slots):
            if group_ct < no_of_groups and idx == combination[group_ct]:
                possibility.extend(black_groups[group_ct])
                group_ct += 1
                if group_ct < no_of_groups:
                    possibility.append(-1)
                continue
            possibility.append(-1)
        # print(possibility)
        possibilities.append(possibility)
    return possibilities


def list_all_possibilities(all_groups_list, no_of_spaces):
    all_possibilities = []
    for groups in all_groups_list:
        no_of_groups = len(groups)
        # number of white spaces remaining excluding single white space between
        # black groups
        no_of_remaining_spaces = no_of_spaces - sum(groups) - no_of_groups + 1
        black_groups = [[1] * group for group in groups]  # groups of black cells
        possibilities = find_possibilities(black_groups, no_of_groups, no_of_remaining_spaces)
        all_possibilities.append(possibilities)
    return all_possibilities


def get_all_unsolved_indices(possibilities, solved_indices, is_row):
    num_possible = [len(idx) for idx in possibilities]
    return [(idx, num, is_row) for idx, num in enumerate(num_possible) if solved_indices[idx] == 0]


def is_solved_index(solved_rows, solved_cols, idx, is_row):
    if is_row:
        return solved_rows[idx]
    return solved_cols[idx]


def get_single_solution_cells(options):
    cells = []
    for idx, opts in enumerate(np.array(options).T):
        unique_opts = np.unique(opts)
        if len(unique_opts) == 1:
            cells.append((idx, unique_opts[0]))
    return cells


def remove_possibilities(possibilities, idx, value):
    return [pos for pos in possibilities if pos[idx] == value]


def update_solved_indices(board, solved_rows, solved_cols, idx, is_row):
    if is_row:
        values = board[idx]
    else:
        values = [row[idx] for row in board]
    if 0 not in values:
        if is_row:
            solved_rows[idx] = 1
        else:
            solved_cols[idx] = 1


def is_solved_board(solved_rows, solved_cols):
    return 0 not in solved_rows and 0 not in solved_cols


def solve(row_list, col_list, board):
    # define all possibilities
    row_possibilities = list_all_possibilities(row_list, len(col_list))
    col_possibilities = list_all_possibilities(col_list, len(row_list))
    # print(row_possibilities)
    solved_rows = [0] * ROWS
    solved_cols = [0] * COLS
    solved = False
    while not solved:
        unsolved_rows = get_all_unsolved_indices(row_possibilities, solved_rows, 1)
        unsolved_cols = get_all_unsolved_indices(col_possibilities, solved_cols, 0)
        # sort all unsolved rows and cols in the order of the least possibilities
        all_unsolved = sorted(unsolved_rows + unsolved_cols, key=lambda element: element[1])

        for idx, _, is_row in all_unsolved:
            if not is_solved_index(solved_rows, solved_cols, idx, is_row):
                if is_row:
                    opts = row_possibilities[idx]
                else:
                    opts = col_possibilities[idx]
                single_solu_cells = get_single_solution_cells(opts)
                for ss_idx, ss_val in single_solu_cells:
                    if is_row:
                        r_idx, c_idx = idx, ss_idx
                    else:
                        r_idx, c_idx = ss_idx, idx
                    if board[r_idx][c_idx] == 0:
                        board[r_idx][c_idx] = ss_val
                        if is_row:
                            col_possibilities[c_idx] = remove_possibilities(col_possibilities[c_idx], r_idx, ss_val)
                        else:
                            row_possibilities[r_idx] = remove_possibilities(row_possibilities[r_idx], c_idx, ss_val)
                update_solved_indices(board, solved_rows, solved_cols, idx, is_row)
                # print_board(row_list, col_list, board)
                # print(row_possibilities)
                # print(col_possibilities)
                # print("")
        solved = is_solved_board(solved_rows, solved_cols)


def print_board(row_list, col_list, board):
    row_max = max(len(row) for row in row_list)
    col_max = max(len(col) for col in col_list)
    for row in range(ROWS):
        print("| ", end="")
        for col in range(COLS):
            match board[row][col]:
                case 0: print(' ', end="")
                case 1: print('B', end="")
                case -1: print('W', end="")
            print(" | ", end="")
        for row_value in row_list[row]:
            print(row_value, end=" ")
        print("")
    print('-' + '-' * 4 * len(col_list))
    for idx in range(col_max):
        print("| ", end="")
        for col in col_list:
            if len(col) > idx:
                print(col[idx], end="")
            else:
                print(" ", end="")
            print(" | ", end="")
        print("")


def main():
    input_rows = nonogram_rows_20x20_1
    input_cols = nonogram_cols_20x20_1
    global ROWS, COLS
    ROWS = len(input_rows)
    COLS = len(input_cols)
    board = [[0 for col in range(COLS)] for row in range(ROWS)]
    print("Input board:")
    print_board(input_rows, input_cols, board)
    solve(input_rows, input_cols, board)
    print("\nSolved board:")
    print_board(input_rows, input_cols, board)


main()
