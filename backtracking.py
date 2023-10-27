def print_sudoku_board(sudoku_board):
    print("Initial Board\n")
    for row_num, row in enumerate(sudoku_board):
        for pos, number in enumerate(row):
            print(number, end=' ')
            if pos == 8:
                print()
                break
            elif (pos + 1) % 3 == 0:
                print('|', end=' ')
        if (row_num + 1) % 3 == 0 and row_num != 8:
            print("-" * 22)

    print()
    print('-'*25)

    return None


sudoku_board = [
    ['-', 5, 2, '-', '-', 6, '-', '-', '-'],
    [1, 6, '-', 9, '-', '-', '-', '-', 4],
    ['-', 4, 9, 8, '-', 3, 6, 2, '-'],
    [4, '-', '-', '-', '-', '-', 8, '-', '-'],
    ['-', 8, 3, 2, '-', 1, 5, 9, '-'],
    ['-', '-', 1, '-', '-', '-', '-', '-', 2],
    ['-', 9, 7, 3, '-', 5, 2, 4, '-'],
    [2, '-', '-', '-', '-', 9, '-', 5, 6],
    ['-', '-', '-', 1, '-', '-', 9, 7, '-']
]


def backtracking(sudoku_board):
    print("Solution\n")
    for row_num, row in enumerate(sudoku_board):
        for col_num, number in enumerate(row):
            if number == '-':
                sudoku_board[row_num][col_num] = 1

    print_sudoku_board(sudoku_board)


print_sudoku_board(sudoku_board)
backtracking(sudoku_board)
