import pygame

from sys import argv
from utils import load_config
from car import Car
from grid import Grid
from supervisor import Supervisor
from typing import Dict, Any, Tuple

Config = Dict[str, Any]


def init_simulation(confg: Config) -> Tuple[pygame.Surface, pygame.time.Clock, pygame.Surface]:
    pygame.init()
    background_image = pygame.image.load(config["background"])
    screen = pygame.display.set_mode(background_image.get_rect()[2:])
    clock = pygame.time.Clock()
    screen.blit(background_image, [0, 0])
    return screen, clock, background_image


def process_events() -> bool:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                import pdb; pdb.set_trace()
    return False


def spawn_cars(config: Config, rolling_counter: int, all_sprites: pygame.sprite.Group, supervisor: Supervisor) -> int:
    rolling_counter += 1
    if rolling_counter + 1 >= (framerate / config["spawn_cooldown"]):
        car = Car(config["car"], dir=-90, supervisor=supervisor)
        all_sprites.add(car)
        id, res = supervisor.reserve_road(car)
        if res is False:
            car.kill()
        return 0
    return rolling_counter + 1


def draw(screen: pygame.Surface, background: pygame.Surface,
         framerate: int, all_sprites: pygame.sprite.Group,
         clock: pygame.time.Clock, grid: Grid) -> None:

    screen.blit(background, [0, 0])
    all_sprites.update()
    grid.draw_grid(screen)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(framerate)


if __name__ == '__main__':
    config = load_config(argv[1] if len(argv) > 1 else "configs/simple.yaml")
    screen, clock, background = init_simulation(config)
    framerate = config["framerate"]
    all_sprites = pygame.sprite.Group()
    grid = Grid(config["intersection"], all_sprites)
    supervisor = Supervisor(grid=grid, screen=screen)
    rolling_counter = 0
    dead = False
    while not dead:
        dead = process_events()
        rolling_counter = spawn_cars(config, rolling_counter, all_sprites, supervisor)
        draw(screen=screen, background=background, all_sprites=all_sprites,
             grid=grid, clock=clock, framerate=framerate)
