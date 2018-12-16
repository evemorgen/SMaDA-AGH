import pygame
from dataclasses import dataclass
from math import sqrt
from itertools import product


@dataclass
class Cell:
    rect: pygame.Rect

    def draw_cell(self, screen, color, filled=False):
        if filled:
            pygame.draw.rect(screen, (color[0], color[1], color[2], 128), self.rect, 0)
        else:
            pygame.draw.rect(screen, color, self.rect, 1)


class Grid:
    def __init__(self, config, cars):
        self.cars = cars
        self.squares = config["num_of_squares"]
        self.x_lines = int(sqrt(self.squares)) - 1
        self.y_lines = int(sqrt(self.squares)) - 1
        self.start_x, self.start_y = config["start"]
        self.end_x, self.end_y = config["end"]
        self.color = config["color"]
        spacing_y = (self.end_y - self.start_y) / (self.y_lines + 1)
        spacing_x = (self.end_x - self.start_x) / (self.x_lines + 1)
        self.g = [Cell(pygame.Rect(self.start_x + spacing_x * x, self.start_y + spacing_y * y, spacing_x, spacing_y)) for x, y in product(range(0, self.x_lines + 1), range(0, self.y_lines + 1))]

    def draw_grid(self, screen):
        for cell in self.g:
            if pygame.sprite.spritecollideany(cell, self.cars) is None:
                cell.draw_cell(screen, (255, 255, 255), False)
            else:
                cell.draw_cell(screen, (255, 255, 255), True)
