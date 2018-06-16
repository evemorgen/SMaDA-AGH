import numpy as np
import csv
import math
import random
import matplotlib.pyplot as plt
from scipy.misc import toimage
from itertools import product

from core.utils import constants

# constants
NUM_OF_FEATURES = 4
WIDTH = 5
HEIGHT = 5
max_iters = 5000
radius = WIDTH / 2.0
learning_rate = constants['learning_factor']
minimal_change = 0.001


class LemmeOut(Exception):
    pass


def load_data(filename):
    p = []
    c = []

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            p.append([float(x) for x in row[0:NUM_OF_FEATURES]])
            c.append(row[4])
    return p, c


def distance(map, x):
    reshaped = x.reshape(
        (1, 1, -1)
    )
    squared = (map - reshaped) ** 2
    return np.sqrt(np.sum(squared, 2))


def generate_result_map(pat, cls, map):
    result_map = np.zeros([HEIGHT, WIDTH, 3], dtype=np.float32)
    iris_map = {
        'Iris-setosa':     (0, [1, 0, 0]),
        'Iris-virginica':  (1, [0, 1, 0]),
        'Iris-versicolor': (2, [0, 0, 1])
    }

    for i, pattern in enumerate(pat):

        eucli_map = distance(map, pattern)

        x = np.argmin(np.amin(eucli_map, 1), 0)
        y = np.argmin(eucli_map, 1)[int(x)]

        if result_map[x][y][iris_map[cls[i]][0]] <= 0.5:
            result_map[x][y] += np.asarray(iris_map[cls[i]][1])
        i += 1

    return np.flip(result_map, 0)


py_patterns, classes = load_data('../data/training_data/iris.data')
patterns = np.asarray(py_patterns, dtype=np.float32)

map = np.random.uniform(size=(HEIGHT, WIDTH, NUM_OF_FEATURES))
old_map = np.zeros(
    (HEIGHT, WIDTH, NUM_OF_FEATURES)
)

coords = np.zeros(
    [HEIGHT, WIDTH, 2],
    dtype=np.int32
)

for i in range(HEIGHT):
    for j in range(WIDTH):
        coords[i][j] = [i, j]

max_iterations = max_iters * len(patterns)
bmu = np.zeros([2], dtype=np.int32)

time = 1

try:
    for n in range(max_iters):
        shuffle = random.sample(
            range(len(patterns)),
            len(patterns)
        )

        for i in range(len(patterns)):
            current_change = np.sqrt(
                np.sum(np.sum((old_map - map) ** 2, 2))
            )

            if current_change <= minimal_change:
                raise LemmeOut
            else:
                pattern = patterns[shuffle[i]]
                eucli_map = distance(map, pattern)

                bmu[0] = np.argmin(np.amin(eucli_map, 1), 0)
                bmu[1] = np.argmin(eucli_map, 1)[int(bmu[0])]

                eucli_bmu = distance(coords, bmu)

                old_map = np.copy(map)

                for i, j in product(range(HEIGHT), range(WIDTH)):
                    dist = eucli_bmu[i][j]
                    if dist <= radius:
                        theta = math.exp(-(dist ** 2) / (2 * (radius ** 2)))
                        map[i][j] = map[i][j] + theta * learning_rate * (pattern - map[i][j])

                learning_rate = constants['learning_factor'] * math.exp(-1.0 * time / (max_iters * len(patterns)))
                radius = (WIDTH / 2.0) * math.exp(-1.0 * time / ((max_iters * len(patterns)) / math.log(radius)))

                time += 1
        if n % (max_iters / 10) == 0:
            print("done course no #{}".format(n))
except LemmeOut:
    pass


output = generate_result_map(patterns, classes, map)
#print(output)
print(map)

# Iris-Setosa - RED
# Iris-Virginica - GREEN
# Iris-Versicolor - BLUE

toimage(output).save('map.jpg')
