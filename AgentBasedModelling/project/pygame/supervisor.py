import math
import time
import logging

from typing import List

from car import Car

Waypoint = List[int]


class Supervisor:
    def __init__(self, grid, screen):
        self.grid = grid
        self.reservation_id = 0
        self.screen = screen

    def __repr__(self):
        return f"Supervisor(num_of_vec={len(self.grid.cars)})"

    def reserve_road(self, car: Car) -> int:
        cells = self.cells_from_waypoints(car.waypoints, car)
        now = time.time()
        duration = 3
        results = [cell.timeline.add_timespan(now + t, duration=duration, vin=car.vin) for cell, t in cells]
        logging.debug(f"car:{car.vin} is trying to reserve cells: {cells} at {now} with following results: {results}")
        if not all(results):
            logging.debug(f"car: {car.vin} cancelling reservation for {now}")
            for cell, t in cells:
                cell.timeline.cancel_timespan(now + t, duration=duration, vin=car.vin)

        self.reservation_id += 1
        return (self.reservation_id, all(results))

    def route_len(self, route, until):
        return sum([math.sqrt((route[j][0] - route[j + 1][0]) ** 2 + (route[j][1] - route[j][1]) ** 2) for j in range(until)])

    def points_len(self, p1, p2):
        p1x, p1y = p1
        p2x, p2y = p2
        return math.sqrt((p1x - p2x)**2 + (p1y - p2y)**2)

    def cells_from_waypoints(self, road, car):
        cells = set()
        points_to_add = []
        for i in range(len(road) - 1):
            w1, w2 = road[i], road[i + 1]
            w1x, w1y = w1
            w2x, w2y = w2
            points = [((int(w1x + i * (w2x - w1x) / 10)), int(w1y + i * (w2y - w1y) / 10)) for i in range(10)]
            points_to_add = points_to_add + points
            for point in points:
                for cell in self.grid.g:
                    if cell.rect.collidepoint(point) and cell not in [c for c, _ in cells]:
                        cells.add((cell, (self.route_len(road, i) + self.points_len(road[i], point)) / car.velocity / 60))

        self.grid.add_points_to_draw(points_to_add)
        return cells
