class sudokuSolver:
    def __init__(self, board):
        # Sudoku board
        self.board = board

        # List of all blank cell coordinates
        self.blankCells = []

        # Index of the current blank cell that is being filled
        self.currBlankCell = 0

    def solve(self):
        # 0. Define all empty cells
        self.blankCells = self.getAllBlankCells()

        # 1. Find empty cell
        # 2. Assign a number
        # 3. Check valid
        # 3. Repeat 1 to 3

        # 4. If not valid: Go to previous guess and add 1

    def getAllBlankCells(self):
        # Go through each row and look for all 0's for every column
        # Then, append the coordinates as lists in the format of [rowNum, colNum]
        # This function returns a list with n-coordinates, where n is the number of empty cells
        return [[rowNum, colNum] for rowNum, row in enumerate(self.board) for colNum, number in enumerate(row) if number == 0]

    def printBoard(self):
        # Go through all rows and columns
        for rowNum, row in enumerate(self.board):
            for colNum, number in enumerate(row):
                # Print all numbers with a space after them
                print(number, end=' ')

                # New line at 9th number
                if colNum == 8:
                    print()
                    break

                # Print '|' every 3 numbers
                elif (colNum + 1) % 3 == 0:
                    print('|', end=' ')

            # Print dashes every 3 rows, except for the last row
            if (rowNum + 1) % 3 == 0 and rowNum != 8:
                print("-" * 22)

        return None


if __name__ == "__main__":
    board = [
        [0, 5, 2, 0, 0, 6, 0, 0, 0],
        [1, 6, 0, 9, 0, 0, 0, 0, 4],
        [0, 4, 9, 8, 0, 3, 6, 2, 0],
        [4, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 8, 3, 2, 0, 1, 5, 9, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 2],
        [0, 9, 7, 3, 0, 5, 2, 4, 0],
        [2, 0, 0, 0, 0, 9, 0, 5, 6],
        [0, 0, 0, 1, 0, 0, 9, 7, 0]
    ]

    solver = sudokuSolver(board)

    # Print the initial board
    print("Initial Board\n")
    solver.printBoard()

    # Solve the sudoku
    solver.solve()
