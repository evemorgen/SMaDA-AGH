import pygame
from dataclasses import dataclass
from math import sqrt
from itertools import product

from typing import Dict, Any, List, Tuple
Config = Dict[str, Any]
Triple = Tuple[int, int, int]


@dataclass
class Cell:
    rect: pygame.Rect

    def draw_cell(self, screen: pygame.Surface, color: Triple, filled: bool = False):
        if filled:
            pygame.draw.rect(screen, (color[0], color[1], color[2], 128), self.rect, 0)
        else:
            pygame.draw.rect(screen, color, self.rect, 1)


class Grid:
    def __init__(self, config: Config, cars: pygame.sprite.Group):
        self.cars = cars
        self.squares: int = config["num_of_squares"]
        self.x_lines: int = int(sqrt(self.squares)) - 1
        self.y_lines: int = int(sqrt(self.squares)) - 1
        self.start_x, self.start_y = config["start"]
        self.end_x, self.end_y = config["end"]
        self.color: Triple = config["color"]
        spacing_y: float = (self.end_y - self.start_y) / (self.y_lines + 1)
        spacing_x: float = (self.end_x - self.start_x) / (self.x_lines + 1)
        self.g: List[Cell] = [Cell(pygame.Rect(self.start_x + spacing_x * x, self.start_y + spacing_y * y, spacing_x, spacing_y))
                              for x, y in product(range(0, self.x_lines + 1), range(0, self.y_lines + 1))]

    def draw_grid(self, screen: pygame.Surface) -> None:
        for cell in self.g:
            if pygame.sprite.spritecollideany(cell, self.cars) is None:
                cell.draw_cell(screen, (255, 255, 255), False)
            else:
                cell.draw_cell(screen, (255, 255, 255), True)
