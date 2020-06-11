# Mesures
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 800
SUDOKU_WIDTH = 600
SUDOKU_HEIGHT = 663
CELL_SIZE = 62
GRID_SIZE = CELL_SIZE * 9

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (197, 197, 197)
LIGHT_BLUE = (96, 216, 232)
GREEN = (52, 246, 163)
BUTTON_COLOR = (73, 73, 73)
HIGHLIGHTED_BUTTON = (189, 189, 189)
RED = (195, 121, 121)

# Boards
test_board = [[0 for x in range(9)] for x in range(9)]
board_1 = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
           [6, 0, 0, 1, 9, 5, 0, 0, 0],
           [0, 9, 8, 0, 0, 0, 0, 6, 0],
           [8, 0, 0, 0, 6, 0, 0, 0, 3],
           [4, 0, 0, 8, 0, 3, 0, 0, 1],
           [7, 0, 0, 0, 2, 0, 0, 0, 6],
           [0, 6, 0, 0, 0, 0, 2, 8, 0],
           [0, 0, 0, 4, 1, 9, 0, 0, 5],
           [0, 0, 0, 0, 8, 0, 0, 7, 9]]

# Posistions
grid_pos = (90, 30)
