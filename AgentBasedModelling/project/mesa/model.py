import random

from mesa import Model, Agent
from mesa.space import SingleGrid
from mesa.time import RandomActivation

ID = 1911

def load_scene(filename, grid, model):
    lines = open(filename, 'r').readlines()
    types = {
        "=": "wall",
        "c": "car"
    }
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char not in (" ", "\n"):
                grid.place_agent(
                    Walker(1911 + i + j*i, model, (j, -i), type=types[char]),
                    (j, -i)
                )


class Walker(Agent):
    def __init__(self, unique_id, model, pos, heading=(1, 0), type="arrow"):
        super().__init__(unique_id, model)
        self.type = type
        self.pos = pos
        self.heading = heading
        self.headings = {(1, 0), (0, 1), (-1, 0), (0, -1)}


class ShapesModel(Model):
    def __init__(self, N, width=20, height=10):
        self.running = True
        self.N = N    # num of agents
        self.headings = ((1, 0), (0, 1), (-1, 0), (0, -1))  # tuples are fast
        self.grid = SingleGrid(width, height, torus=False)
        self.schedule = RandomActivation(self)
        load_scene('shape_model/crossing.txt', self.grid, self)
        """
        self.grid.place_agent(
            Walker(1911, self, (4, 4), type="wall"),
            (4, 4)
        )
        self.make_walls()
        self.make_walker_agents()
        """

    def make_walls(self):
        for i in range(0, 50):
            self.grid.place_agent(
                Walker(1911, self, (i, 5), type="wall"),
                (i, 5)
            )


    def make_walker_agents(self):
        unique_id = 0
        while True:
            if unique_id == self.N:
                break
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            pos = (x, y)
            heading = random.choice(self.headings)
            # heading = (1, 0)
            if self.grid.is_cell_empty(pos):
                print("Creating agent {2} at ({0}, {1})"
                      .format(x, y, unique_id))
                a = Walker(unique_id, self, pos, heading)
                self.schedule.add(a)
                self.grid.place_agent(a, (x,   y))
                self.grid.place_agent(a, (x+1, y))
                self.grid.place_agent(a, (x, y+1))
                self.grid.place_agent(a, (x+1, y+1))
                unique_id += 1

    def step(self):
        self.schedule.step()
