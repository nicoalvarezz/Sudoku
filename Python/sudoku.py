import pprint


def view_matrix(grid):
    """Function to print the grid"""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end=" ")
        print()


def empty_space(grid):
    """Funtion to find emty space in the grid"""
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j)

    return None


def possible(grid, row, col, num):
    """Function to check if a certain value for a certain position is correct"""

    # Check row
    for i in range(0, len(grid)):
        if grid[row][i] == num:
            return False

    # Check column
    for i in range(0, len(grid)):
        if grid[i][col] == num:
            return False

    box_row = (row // 3) * 3 # Find smaller row
    box_col = (col // 3) * 3 # Find smaller column

    # Check smaller grid
    for i in range(3):
        for j in range(3):
            if grid[box_row + i][box_col + j] == num:
                return False

    return True


def solve(grid):
    find = empty_space(grid)
    if find:
        row, col = find # Ger empty space
    else:
        return True

    # Loop through grid
    for i in range(1, 10):
        # Find the number that must replace 0
        if possible(grid, row, col, i):
            grid[row][col] = i

            # Backtracking Recursion
            if solve(grid):
                return True
            grid[row][col] = 0

    return False

# Main Program
grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

pp = pprint.PrettyPrinter(width=41, compact=True)
pp.pprint(grid)
solve(grid)
print()
pp.pprint(grid)
