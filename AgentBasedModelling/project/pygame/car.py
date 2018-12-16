import pygame
import random
from copy import copy
from math import cos, sin, pi, sqrt


class Car(pygame.sprite.Sprite):
    def __init__(self, config, path=None, dir=None, image=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image or random.choice(config["sprites"]))
        self.rect = self.image.get_rect()
        self.oryginal = copy(self.image)
        self.dir = dir or 0
        self.velocity = config["velocity"]
        self.waypoints = path or random.choice(config["paths"])
        self.waypoint_idx = 1
        self.current_waypoint = self.waypoints[1]
        self.rect.x, self.rect.y = self.waypoints[0]
        self.rect.x -= self.image.get_rect().size[0] / 2
        self.rect.y -= self.image.get_rect().size[1] / 2

    def next_waypoint(self):
        self.waypoint_idx += 1
        try:
            self.current_waypoint = self.waypoints[self.waypoint_idx]
        except IndexError:
            self.kill()

    def turn(self, amount):
        oldCenter = self.rect.center
        self.dir += amount
        self.image = pygame.transform.rotate(self.oryginal, 270 - self.dir)
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
