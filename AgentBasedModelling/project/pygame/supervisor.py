import math
import time
import logging

from typing import List

from car import Car

from pygame import sprite, rect

Waypoint = List[int]


class Supervisor:
    def __init__(self, grid, screen):
        self.grid = grid
        self.reservation_id = 0
        self.screen = screen

    def __repr__(self):
        return f"Supervisor(num_of_vec={len(self.grid.cars)})"

    def reserve_road(self, car: Car, current_time: int) -> int:
        cells = self.cells_from_waypoints(car.waypoints, car)
        now = current_time
        duration = 50 / car.velocity
        results = [cell.timeline.add_timespan(now + t, duration=duration, vin=car.vin) for cell, t in cells]
        logging.debug(f"car:{car.vin} is trying to reserve cells: {cells} at {now} with following results: {results}")
        if not all(results):
            logging.debug(f"car: {car.vin} cancelling reservation for {now}")
            for cell, t in cells:
                cell.timeline.cancel_timespan(now + t, duration=duration, vin=car.vin)

        self.reservation_id += 1
        return (self.reservation_id, all(results))

    def route_len(self, route, until):
        return sum([self.points_len(route[j], route[j + 1]) for j in range(until)])

    def points_len(self, p1, p2):
        p1x, p1y = p1
        p2x, p2y = p2
        return math.hypot(p1x - p2x, p1y - p2y)

    def cells_from_waypoints(self, road, car):
        cells = set()
        points_to_add = []
        for i in range(len(road) - 1):
            w1, w2 = road[i], road[i + 1]
            w1x, w1y = w1
            w2x, w2y = w2
            prec = math.floor(self.points_len(w1, w2) / 10)
            points = [((int(w1x + i * (w2x - w1x) / prec)), int(w1y + i * (w2y - w1y) / prec)) for i in range(prec)]
            points_to_add = points_to_add + points
            for point in points:
                for cell in self.grid.g: # rak driven development   
                    potential_dist = (car.rect.size[1] + cell.rect.size[0]) / 2
                    if self.points_len(cell.rect.center, point) < potential_dist and cell not in [c for c, _ in cells]:
                        cells.add((cell, (self.route_len(road, i) + self.points_len(road[i], point)) / car.velocity))

        self.grid.add_points_to_draw(points_to_add)
        return cells
