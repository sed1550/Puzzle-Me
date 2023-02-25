ROWS = 9
COLS = 9


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
