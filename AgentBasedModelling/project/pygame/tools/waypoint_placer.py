import pygame
from random import randint
from sys import argv
from ast import literal_eval


background_file = argv[1]
waypoints_file = argv[2]

waypoints = [(literal_eval(l), (randint(0, 255), randint(0, 255), randint(0, 255))) for l in open(waypoints_file, "r").readlines()]

pygame.init()
background = pygame.image.load(background_file)
screen = pygame.display.set_mode(background.get_rect()[2:])
clock = pygame.time.Clock()
screen.blit(background, (0, 0))
pygame.display.flip()


running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))
    #pygame.draw.rect(screen, (255, 255, 255), [(350, 235), (250, 255)], 3)
    pygame.draw.rect(screen, (255, 255, 255), [(467, 253), (381, 272)], 3)
    for points, color in waypoints:
        for i, point in enumerate(points):
            pygame.draw.circle(screen, color, point, 5)
            if i != 0 and i != len(points):
                pygame.draw.line(screen, color, points[i - 1], point)
    pygame.display.flip()
    clock.tick(60)
