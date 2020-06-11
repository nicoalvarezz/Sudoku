import pygame
from sudoku_settings import HIGHLIGHTED_BUTTON, BUTTON_COLOR


class Button:
    def __init__(self, x, y, width, height, text=None, color=BUTTON_COLOR, highlighted_color=HIGHLIGHTED_BUTTON, function=None, params=None):
        self.image = pygame.Surface((width, height))
        self.pos = (x, y)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.text = text
        self.color = color
        self.highlighted_color = highlighted_color
        self.function = function
        self.params = params
        self. highlighted = False

    def update_button(self, mouse):
        if self.rect.collidepoint(mouse):
            self.highlighted = True
        else:
            self.highlighted = False

    def draw_button(self, screen):
        if self.highlighted:
            self.image.fill(self.highlighted_color)
        else:
            self.image.fill(self.color)
        screen.blit(self.image, self.pos)
