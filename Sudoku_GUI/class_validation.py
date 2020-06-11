import pprint
from sudoku_settings import*


class Sudoku_validation:
    def __init__(self):
        self.grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                     [6, 0, 0, 1, 9, 5, 0, 0, 0],
                     [0, 9, 8, 0, 0, 0, 0, 6, 0],
                     [8, 0, 0, 0, 6, 0, 0, 0, 3],
                     [4, 0, 0, 8, 0, 3, 0, 0, 1],
                     [7, 0, 0, 0, 2, 0, 0, 0, 6],
                     [0, 6, 0, 0, 0, 0, 2, 8, 0],
                     [0, 0, 0, 4, 1, 9, 0, 0, 5],
                     [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    row = 0
    col = 0
    box_row = 0
    box_col = 0

    def empty_space(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 0:
                    return (i, j)
        return None

    def possible(self, row, col, num):
        # Cehcks if the values is possible for certain possition

        # Check row
        for i in range(0, len(self.grid)):
            if self.grid[row][i] == num:
                return False

        # Check col
        for i in range(0, len(self.grid)):
            if self.grid[i][col] == num:
                return False

        box_row = (row // 3) * 3
        box_col = (col // 3) * 3

        for i in range(3):
            for j in range(3):
                if self.grid[box_row + i][box_col + j] == num:
                    return False

        return True

    def solve(self):
        find = self.empty_space()
        if find:
            row, col = find
        else:
            return True

        for i in range(1, 10):
            if self.possible(row, col, i):
                self.grid[row][col] = i

                if self.solve():
                    return True

                self.grid[row][col] = 0

        return False

    def print_result(self):
        pp = pprint.PrettyPrinter(width=41, compact=True)
        #pp.pprint(self.grid)
        self.solve()
        print()
        pp.pprint(self.grid)


#sudoku_val = Sudoku_validation()
#sudoku_val.print_result()