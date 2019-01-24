import pygame
from time import time
from dataclasses import dataclass
from math import sqrt
from itertools import product
from utils import Timeline

from typing import Dict, Any, List, Tuple
Config = Dict[str, Any]
Triple = Tuple[int, int, int]


@dataclass
class Cell:
    rect: pygame.Rect
    timeline: Timeline

    def draw_cell(self, screen: pygame.Surface, current_time: int, filled: bool = False,):
        # now = time()
        if self.timeline.within_reserved(current_time):
            if filled:
                pygame.draw.rect(screen, (255, 0, 255, 128), self.rect, 0)
            else:
                pygame.draw.rect(screen, (255, 0, 0, 128), self.rect, 0)
        elif filled:
            pygame.draw.rect(screen, (255, 255, 255), self.rect, 0)
        else:
            pygame.draw.rect(screen, (255, 255, 255), self.rect, 1)

    def __eq__(self, other):
        return self.rect == other.rect and self.timeline == other.timeline

    def __hash__(self):
        return hash(str(self))


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
        self.points = None
        self.g: List[Cell] = [Cell(pygame.Rect(self.start_x + spacing_x * x, self.start_y + spacing_y * y, spacing_x, spacing_y), Timeline())
                              for x, y in product(range(0, self.x_lines + 1), range(0, self.y_lines + 1))]

    def draw_grid(self, screen: pygame.Surface, current_time: int) -> None:
        # FIXME remote after debugging
        # if self.points is not None:
        #     for point in self.points:
        #         pygame.draw.circle(screen, (255, 0, 0), point, 3)
        for cell in self.g:
            if pygame.sprite.spritecollideany(cell, self.cars) is None:
                cell.draw_cell(screen, current_time,  False)
            else:
                cell.draw_cell(screen, current_time, True)

    # FIXME remove after debugging
    def add_points_to_draw(self, points):
        self.points = points
