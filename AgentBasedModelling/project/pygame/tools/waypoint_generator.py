import sys
import pygame
from random import randint

pygame.init()
background = pygame.image.load(sys.argv[1])
screen = pygame.display.set_mode(background.get_rect()[2:])
clock = pygame.time.Clock()
screen.blit(background, (0, 0))
pygame.display.flip()

points = []
i = 0
color = (randint(0, 255), randint(0, 255), randint(0, 255))

running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            points.append(event.pos)
            print(points)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            open(f"waypoint_{i}", 'a').write(str(points) + "\n")
            points = []
            color = (randint(0, 255), randint(0, 255), randint(0, 255))

    screen.blit(background, (0, 0))
    for point in points:
        pygame.draw.circle(screen, color, point, 5)
    pygame.draw.rect(screen, (255, 255, 255), [(350, 235), (250, 255)], 3)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
