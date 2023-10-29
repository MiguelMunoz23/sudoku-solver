class sudokuSolver:
    def __init__(self, board):
        # Sudoku board
        self.board = board

        # List of all blank cell coordinates
        self.blankCells = self.getAllBlankCells()

        # Index of the current blank cell that is being filled
        self.iBlankCell = 0

        # Current row index of blank cell
        self.iRow = self.blankCells[self.iBlankCell][0]
        # Current column index of blank cell
        self.iCol = self.blankCells[self.iBlankCell][1]

    def solve(self):
        # Recalculate iRow and iCol
        self.iRow = self.blankCells[self.iBlankCell][0]
        self.iCol = self.blankCells[self.iBlankCell][1]

        # 1. Assign a number to the current blank cell
        self.board[self.iRow][self.iCol] += 1

        # If a cell is already 9, go back one more
        if self.board[self.iRow][self.iCol] == 10:
            self.goBack()

        self.currNum = self.board[self.iRow][self.iCol]

        # 2. Check if guess is a valid number
        if self.isValid():
            # Go to next blank cell
            self.iBlankCell += 1

            if self.iBlankCell >= len(self.blankCells):
                return True

            # Repeat steps 1 and 2
            self.solve()

        elif self.currNum < 9:
            self.solve()

        else:
            self.goBack()
        return False

    def goBack(self):
        # Set current guess to 0
        self.board[self.iRow][self.iCol] = 0

        # Go to previous guess and add 1
        if self.iBlankCell > 0:
            self.iBlankCell -= 1
        self.solve()

    def getAllBlankCells(self):
        # Go through each row and look for all 0's for every column
        # Then, append the coordinates as lists in the format of [rowNum, colNum]
        # This function returns a list with n-coordinates, where n is the number of empty cells
        return [[rowNum, colNum] for rowNum, row in enumerate(self.board) for colNum, number in enumerate(row) if number == 0]

    def isValid(self):
        validRow = self.checkRow()
        validCol = self.checkCol()
        validBox = self.checkBox()

        return validRow and validCol and validBox

    def checkRow(self):
        currRow = self.board[self.iRow]

        # Go through all columns in the current row
        for colNum in range(len(currRow)):
            # If the number is in the row and it's not the number itself
            if currRow[colNum] == self.currNum and colNum != self.iCol:
                return False
        # If the number was not in the row
        return True

    def checkCol(self):
        # Get the column list of the current position
        columnList = [row[self.iCol] for row in self.board]

        # Go through all row in the current column
        for rowNum in range(len(columnList)):
            # If the number is in the row and it's not the number itself
            if self.board[rowNum][self.iCol] == self.currNum and rowNum != self.iRow:
                return False
        # If the number was not in the column
        return True

    def checkBox(self):
        # Limits in the x-axis
        x0 = (self.iRow // 3) * 3
        x1 = x0 + 3

        # Limits in the y-axis
        y0 = (self.iCol // 3) * 3
        y1 = y0 + 3

        # Go through the box-limits in x and y axis
        for x in range(x0, x1):
            for y in range(y0, y1):
                # If the number is in the box and it's not the number itself
                if self.board[x][y] == self.currNum and x != self.iRow and y != self.iCol:
                    return False
        return True

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

    print("-" * 25)

    # Print the solution
    print("Solution\n")
    solver.printBoard()
