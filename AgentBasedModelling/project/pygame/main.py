import pygame
from math import pi, sin, cos, sqrt
from copy import copy
from random import choice


def random_car():
    return "pictures/car{}.png".format(choice(range(1, 6)))


pygame.init()

display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

car_image = pygame.image.load(random_car())
background_image = pygame.transform.scale(pygame.image.load('pictures/background.png'), (display_width, display_height))
screen.blit(background_image, [0, 0])

path1 = [
    (50, 325), #(100, 325),
    (150, 325), #(200, 325),
    (250, 325), #(300, 325),
    (350, 325), #(400, 325), 
    (450, 300), (470, 245), (470, 175), (470, 125),
    (470, 75), (470, 25), (470, -25)
]


class Car(pygame.sprite.Sprite):
    def __init__(self, path, dir):
        pygame.sprite.Sprite.__init__(self)
        self.image = car_image
        self.rect = self.image.get_rect()
        image_x, image_y = car_image.get_rect().size
        self.oryginal = copy(self.image)
        self.dir = 0
        self.velocity = 5
        self.waypoints = path
        self.waypoint_idx = 1
        self.current_waypoint = self.waypoints[1]
        self.rect.x, self.rect.y = self.waypoints[0]
        self.rect.x -= car_image.get_rect().size[0] / 2
        self.rect.y -= car_image.get_rect().size[1] / 2
        self.turn(dir)

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
        current_heading = pygame.math.Vector2(self.velocity, self.velocity)
        current_heading.rotate_ip(self.dir)
        #to_rotate = waypoint_vector.angle_to(current_heading)
        to_rotate = current_heading.angle_to(waypoint_vector)
        print(waypoint_vector, current_heading, to_rotate, self.waypoint_idx)
        self.turn(to_rotate)

    def update(self):
        self.towards_waypoint()
        self.rect.x += cos(self.dir * pi / 180.0) * self.velocity
        self.rect.y += sin(self.dir * pi / 180.0) * self.velocity
        if sqrt((self.rect.x - self.current_waypoint[0]) ** 2 + (self.rect.y - self.current_waypoint[1]) ** 2) < 30:
            self.next_waypoint()


all_sprites = pygame.sprite.Group()
car = Car(path1, 90)
all_sprites.add(car)
n = 1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    screen.blit(background_image, [0, 0])
    all_sprites.update()
    #car.update()

    all_sprites.draw(screen)
    pygame.draw.rect(screen, (255, 0, 0), car.rect, 5)
    for x, y in path1:
        pygame.draw.rect(screen, (255, 0, 0), (x, y, 10, 10), 5)

    pygame.display.flip()
    clock.tick(5)
