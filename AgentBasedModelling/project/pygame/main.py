import pygame
import yaml
from math import pi, sin, cos, sqrt
from copy import copy
from random import choice


def load_config(filename):
    with open(filename, 'r') as yml_file:
        return yaml.load(yml_file)


class Car(pygame.sprite.Sprite):
    def __init__(self, config, path=None, dir=None, image=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image or choice(config["car"]["sprites"]))
        self.rect = self.image.get_rect()
        self.oryginal = copy(self.image)
        self.dir = dir or 0
        self.velocity = config["car"]["velocity"]
        self.waypoints = path or choice(config["car"]["paths"])
        self.waypoint_idx = 1
        print(self.waypoints)
        self.current_waypoint = self.waypoints[1]
        self.rect.x, self.rect.y = self.waypoints[0]
        self.rect.x -= self.image.get_rect().size[0] / 2
        self.rect.y -= self.image.get_rect().size[1] / 2

    def next_waypoint(self):
        self.waypoint_idx += 1
        self.current_waypoint = self.waypoints[self.waypoint_idx]

    def turn(self, amount):
        "turn some amount"
        oldCenter = self.rect.center
        self.dir += amount
        self.image = pygame.transform.rotate(self.oryginal, self.dir)
        self.rect = self.image.get_rect()
        self.rect.center = oldCenter

    def towards_waypoint(self):
        waypoint_vector = pygame.math.Vector2(
            self.current_waypoint[0] - self.rect.x - self.image.get_rect()[0],
            self.current_waypoint[1] - self.rect.center[1]
        )
        current_heading = pygame.math.Vector2(self.velocity, 0)
        current_heading.rotate_ip(self.dir)
        to_rotate = current_heading.angle_to(waypoint_vector)
        self.turn(to_rotate)

    def update(self):
        self.towards_waypoint()
        self.rect.x += cos(self.dir * pi / 180.0) * self.velocity
        self.rect.y += sin(self.dir * pi / 180.0) * self.velocity
        if sqrt((self.rect.x - self.current_waypoint[0]) ** 2 + (self.rect.y - self.current_waypoint[1]) ** 2) < 30:
            self.next_waypoint()


class Grid:
    def __init__(self, config):
        self.squares = config["num_of_squares"]
        self.x_lines = int(sqrt(self.squares)) - 1
        self.y_lines = int(sqrt(self.squares)) - 1
        self.start_x, self.start_y = config["start"]
        self.end_x, self.end_y = config["end"]
        self.color = config["color"]

    def draw_grid(self, screen):
        pygame.draw.line(screen, self.color, (self.start_x, self.start_y), (self.end_x, self.start_y))
        pygame.draw.line(screen, self.color, (self.start_x, self.end_y), (self.end_x, self.end_y))
        spacing_y = (self.end_y - self.start_y) / (self.y_lines + 1)
        for y_line in range(self.y_lines + 1):
            pygame.draw.line(
                screen,
                self.color,
                (self.start_x, self.start_y + spacing_y * y_line),
                (self.end_x, self.start_y + spacing_y * y_line)
            )
        pygame.draw.line(screen, self.color, (self.start_x, self.start_y), (self.start_x, self.end_y))
        pygame.draw.line(screen, self.color, (self.end_x, self.start_y), (self.end_x, self.end_y))
        spacing_x = (self.end_x - self.start_x) / (self.x_lines + 1)
        for x_line in range(self.x_lines + 1):
            pygame.draw.line(
                screen,
                self.color,
                (self.start_x + spacing_x * x_line, self.start_y),
                (self.start_x + spacing_x * x_line, self.end_y)
            )


pygame.init()
config = load_config("simple.yaml")
background_image = pygame.image.load(config["background"])
screen = pygame.display.set_mode(background_image.get_rect()[2:])
clock = pygame.time.Clock()
screen.blit(background_image, [0, 0])
all_sprites = pygame.sprite.Group()
car = Car(config, dir=-90)
grid = Grid(config["intersection"])
all_sprites.add(car)
n = 1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    screen.blit(background_image, [0, 0])
    all_sprites.update()

    all_sprites.draw(screen)
    pygame.draw.rect(screen, (255, 0, 0), car.rect, 5)
    grid.draw_grid(screen)
    for w in car.waypoints:
        pygame.draw.rect(screen, (255, 0, 0), w + [5, 5], 2)
    pygame.display.flip()
    clock.tick(60)
