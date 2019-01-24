import pygame
import logging
import pdb

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


def precompute_waypoint_grid_relation(grid, paths):
    return [{tuple(waypoint): grid.point_in_grid(waypoint)} for path in paths for waypoint in path]


def process_events() -> Dict[str, bool]:
    events = dict()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                events["dead"] = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                events["dead"] = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                pdb.set_trace()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                events["spawn"] = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                events["slower"] = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                events["faster"] = True
    return events


def spawn_car(config: Config, rolling_counter: int, all_sprites: pygame.sprite.Group, supervisor: Supervisor, current_time: int) -> int:
    rolling_counter += 1
    if rolling_counter + 1 >= (framerate / config["spawn_cooldown"]):
        car = Car(config["car"], dir=-90, supervisor=supervisor)
        all_sprites.add(car)
        id, res = supervisor.reserve_road(car, current_time)
        logging.debug(f"Spawned car: {car} with reservation {id}:{res}")
        if res is False:
            car.kill()
        return 0
    return rolling_counter + 1


def draw(screen: pygame.Surface, background: pygame.Surface,
         framerate: int, all_sprites: pygame.sprite.Group,
         clock: pygame.time.Clock, grid: Grid, current_time: int) -> None:
    screen.blit(background, [0, 0])
    all_sprites.update()
    grid.draw_grid(screen, current_time)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(framerate)


if __name__ == '__main__':
    logging.basicConfig(format='%(funcName)s#%(lineno)-15s [%(asctime)-15s] %(message)s', level=logging.INFO)
    all_sprites = pygame.sprite.Group()
    config = load_config(argv[1] if len(argv) > 1 else "configs/simple.yaml")
    grid = Grid(config["intersection"], all_sprites)
    config['car']['paths_gridded'] = precompute_waypoint_grid_relation(grid, config["car"]["paths"])
    config['car']['paths'] = [[tuple(waypoint) for waypoint in path] for path in config['car']['paths']]
    screen, clock, background = init_simulation(config)
    framerate = config["framerate"]
    framerate_modifier = 1
    supervisor = Supervisor(grid=grid, screen=screen)
    rolling_counter = 0
    current_time = 0
    dead = False
    while not dead:
        current_time += 1
        events = process_events()
        dead = events.get("dead", False)
        if (events.get("faster", False)):
            framerate_modifier *= 1.25
        if (events.get("slower", False)):
            framerate_modifier *= 0.8
        #if events.get("spawn", False):
        #    rolling_counter = spawn_car(config, rolling_counter, all_sprites, supervisor)
        rolling_counter = spawn_car(config, rolling_counter, all_sprites, supervisor, current_time)
        draw(screen=screen, background=background, all_sprites=all_sprites,
             grid=grid, clock=clock, framerate=framerate * framerate_modifier,
             current_time=current_time)
