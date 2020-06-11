import pygame
import sys
from sudoku_settings import*
from button_class import*
from class_validation import*


class Sudoku_GUI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.running = True
        self.grid = board_1
        self.selected = None
        self.mouse_pos = None
        self.state = "playing"
        self.finished = False
        self.cell_changed = False
        self.playing_buttons = []
        self.menu_buttons = []
        self.lock_cells = []
        self.incorrect_cells = []
        self.load()
        self.font = pygame.font.SysFont("arail", CELL_SIZE // 2)
        self.sudoku_validation = Sudoku_validation()

    def run(self):
        while self.running:
            if self.state == "playing":
                self.playing_events()
                self.playing_update()
                self.playing_draw()
        pygame.quit()
        sys.exit()

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # When the user clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected = self.mouse_on_grid()
                if selected:
                    self.selected = selected
                    print(selected)
                else:
                    print("not on board")
                    self.selected = None

            # When the user types a key
            if event.type == pygame.KEYDOWN:
                if self.selected != None and self.selected not in self.lock_cells:
                    if self.is_int(event.unicode):
                        # Changing the cells
                        self.grid[self.selected[1]][self.selected[0]] = int(
                            event.unicode)
                        self.cell_changed = True

    def playing_update(self):
        self.mouse_pos = pygame.mouse.get_pos()
        for button in self.playing_buttons:
            button.update_button(self.mouse_pos)

        if self.cell_changed:
            self.incorrect_cells = []
            if self.board_finished():
                # Check if the board is correct
                self.check_all_cells()
                if len(self.incorrect_cells) == 0:
                    print("Congratulations!")
                self.sudoku_validation.print_result()
                print(self.incorrect_cells)

    def playing_draw(self):
        self.screen.fill(WHITE)

        for button in self.playing_buttons:
            button.draw_button(self.screen)

        if self.selected:
            self.draw_selection(self.selected)

        self.shaded_lock_cell(self.lock_cells)
        self.sheded_incorrect_cell(self.incorrect_cells)
        self.draw_numbers()
        self.draw_grid()
        pygame.display.update()
        self.cell_changed = False

    def draw_grid(self):
        pygame.draw.rect(
            self.screen, BLACK, (grid_pos[0], grid_pos[1], SUDOKU_WIDTH - 40, SUDOKU_HEIGHT - 105), 2)
        for x in range(9):
            if x % 3 != 0:
                pygame.draw.line(self.screen, BLACK, (grid_pos[0] + (x * CELL_SIZE), grid_pos[1]),
                                 (grid_pos[0] + (x * CELL_SIZE), grid_pos[1] + 555))
                pygame.draw.line(self.screen, BLACK, (grid_pos[0], grid_pos[1] + (x * CELL_SIZE)),
                                 (grid_pos[0] + 554, grid_pos[1] + (x * CELL_SIZE)))
            else:
                pygame.draw.line(self.screen, BLACK, (grid_pos[0] + (x * CELL_SIZE), grid_pos[1]),
                                 (grid_pos[0] + (x * CELL_SIZE), grid_pos[1] + 555), 2)
                pygame.draw.line(self.screen, BLACK, (grid_pos[0], grid_pos[1] + (x * CELL_SIZE)),
                                 (grid_pos[0] + 554, grid_pos[1] + (x * CELL_SIZE)), 2)

    def draw_selection(self, pos):
        pygame.draw.rect(self.screen, LIGHT_BLUE,
                         ((pos[0] * CELL_SIZE) + grid_pos[0], (pos[1] * CELL_SIZE) + grid_pos[1], CELL_SIZE, CELL_SIZE))

    def mouse_on_grid(self):
        if self.mouse_pos[0] < grid_pos[0] or self.mouse_pos[1] < grid_pos[1]:
            return False
        if self.mouse_pos[0] > grid_pos[0] + GRID_SIZE or self.mouse_pos[1] > grid_pos[1] + GRID_SIZE:
            return False
        return ((self.mouse_pos[0] - grid_pos[0]) // CELL_SIZE, (self.mouse_pos[1] - grid_pos[1]) // CELL_SIZE)

    def load_buttons(self):
        self.playing_buttons.append(Button(90, 630, 100, 40))

    def text_to_screen(self, text, pos):
        font = self.font.render(text, False, BLACK)
        font_width = font.get_width()
        font_height = font.get_height()
        pos[0] += (CELL_SIZE - font_width) // 2
        pos[1] += (CELL_SIZE - font_height) // 2
        self.screen.blit(font, pos)

    def draw_numbers(self):
        for y_idx, row in enumerate(self.grid):
            for x_idx, num in enumerate(row):
                if num != 0:
                    pos = [(x_idx * CELL_SIZE) + grid_pos[0],
                           (y_idx * CELL_SIZE) + grid_pos[1]]
                    self.text_to_screen(str(num), pos)

    def load(self):
        self.load_buttons()

        # Setting lock cells
        for y_idx, row in enumerate(self.grid):
            for x_idx, num in enumerate(row):
                if num != 0:
                    self.lock_cells.append([x_idx, y_idx])
        print(self.lock_cells)

    def shaded_lock_cell(self, lock_cells):
        for cell in lock_cells:
            pygame.draw.rect(self.screen, GRAY, (cell[0] * CELL_SIZE + grid_pos[0],
                                                 cell[1] * CELL_SIZE + grid_pos[1], CELL_SIZE, CELL_SIZE))

    def sheded_incorrect_cell(self, incorrect_cells):
        for cell in incorrect_cells:
            pygame.draw.rect(self.screen, RED, (cell[0] * CELL_SIZE + grid_pos[0],
                                                cell[1] * CELL_SIZE + grid_pos[1], CELL_SIZE, CELL_SIZE))

    def is_int(self, string):
        try:
            int(string)
            return True
        except:
            return False

    def board_finished(self):
        for row in self.grid:
            for num in row:
                if num == 0:
                    return False
        return True

    def check_all_cells(self):
        # self.check_rows()
        # self.check_rows()
        self.check_small_square()

    def check_rows(self):
        for y_idx, row in enumerate(self.grid):
            possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for x_idx in range(9):
                if self.grid[y_idx][x_idx] in possible:
                    possible.remove(self.grid[y_idx][x_idx])
                else:
                    if [x_idx, y_idx] not in self.lock_cells and [x_idx, y_idx] not in self.incorrect_cells:
                        self.incorrect_cells.append([x_idx, y_idx])

    def check_cols(self):
        for x_idx in range(9):
            possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for y_idx, row in enumerate(self.grid):
                if self.grid[y_idx][x_idx] in possible:
                    possible.remove(self.grid[y_idx][x_idx])
                else:
                    if [x_idx, y_idx] not in self.lock_cells and [x_idx, y_idx] not in self.incorrect_cells:
                        self.incorrect_cells.append([x_idx, y_idx])

    def check_small_square(self):
        for x in range(3):
            for y in range(3):
                possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                #print("re-setting possible")
                for i in range(3):
                    for j in range(3):
                        #print(x * 3 + i, y * 3 + j)
                        x_idx = x * 3 + i
                        y_idx = y * 3 + j
                        if self.grid[y_idx][x_idx] in possible:
                            possible.remove(self.grid[y_idx][x_idx])
                        else:
                            if [x_idx, y_idx] not in self.lock_cells and [x_idx, y_idx] not in self.incorrect_cells:
                                self.incorrect_cells.append([x_idx, y_idx])
                                print("Error found by small grid check")
