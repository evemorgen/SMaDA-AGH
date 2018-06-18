import curses
import yaml
import math
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint
from itertools import cycle
from time import time
import sys

sys.path.append('../')

from core.network import load_network

board = {
    'height': 20,
    'width': 40
}

mooves = [
KEY_RIGHT,
KEY_RIGHT,
KEY_RIGHT,
KEY_RIGHT
]

moove = cycle(mooves)


def init_gui():
    curses.initscr()
    win = curses.newwin(board['height'], board['width'], 0, 0)
    win.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(1)
    return win


def violated_boundary_conditions(snake):
    return (snake[0][0] == 0 or
    snake[0][1] == 0 or
    snake[0][0] == board['height'] - 1 or
    snake[0][1] == board['width'] - 1 or
    snake[0] in snake[1:])


def calculate_head(snake, key):
    snake.insert(0, (
        snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1),
        snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)
    ))


def get_input(player, event, key):
    dir = {
        KEY_UP: {KEY_LEFT: -1, KEY_UP: 0, KEY_RIGHT: 1},
        KEY_LEFT: {KEY_DOWN: -1, KEY_LEFT: 0,KEY_UP: 1},
        KEY_RIGHT: {KEY_UP: -1, KEY_RIGHT: 0, KEY_DOWN: 1},
        KEY_DOWN: {KEY_RIGHT: -1, KEY_DOWN: 0, KEY_LEFT: 1}
    }

    opposite = {
        KEY_DOWN: KEY_UP,
        KEY_UP: KEY_DOWN,
        KEY_LEFT: KEY_RIGHT,
        KEY_RIGHT: KEY_LEFT
    }

    if player:
        if event != -1 and event != opposite[key]:
            return event, dir[key][event]
        else:
            return key, dir[key][key]
    else:
        return next(moove)


def init_state(player, gui, snek):
    if player:
        delay = 100
    elif gui and not player:
        delay = 100
    else:
        delay = 0
    return (
        KEY_RIGHT, # init direction
        0, # score
        delay,
        snek if snek is not None else [(10, 10), (10, 9), (10, 8), (10, 7), (10, 6)], # snek init
        (randint(1,board['height']-1), randint(1,board['width']-1)), # food
    )


def new_food(snake):
    food = (randint(1, board['height'] - 2), randint(1, board['width'] - 2)) # Calculating next food's coordinates
    return food if food not in snake else new_food(snake)


def eat_food(snake, food):
    return snake[0] == food


def extract_features(snake, board, score, food, key, action):
    directions = {
        KEY_DOWN: {'front': (1, 0), 'left': (0, 1), 'right': (0, -1)},
        KEY_UP: {'front': (-1, 0), 'left': (0, -1), 'right': (0, 1)},
        KEY_LEFT: {'front': (0, -1), 'left': (1, 0), 'right': (-1, 0)},
        KEY_RIGHT: {'front': (0, 1), 'left': (-1, 0), 'right': (1, 0)}
    }
    head = snake[0]
    head_front = (head[0] + directions[key]['front'][0], head[1] + directions[key]['front'][1])
    head_left = (head[0] + directions[key]['left'][0], head[1] + directions[key]['left'][1])
    head_right = (head[0] + directions[key]['right'][0], head[1] + directions[key]['right'][1])

    obstacle_front = int(violated_boundary_conditions([head_front] + snake[1:]))
    obstacle_left = int(violated_boundary_conditions([head_left] + snake[1:]))
    obstacle_right = int(violated_boundary_conditions([head_right] + snake[1:]))

    food_angle = math.atan2(abs(head[0] - food[0]), abs(head[1] - food[1]))
    #distance = food_distance(snake, food) / (math.sqrt(board['width'] ** 2 + board['height'] ** 2) / 2)

    return obstacle_front, obstacle_left, obstacle_right, action, food_angle


def draw(win, snake, food, delay, score, last=None):
    win.addch(food[0], food[1], '*')
    if last is not None:
        win.addch(last[0], last[1], ' ')
        win.addch(snake[0][0], snake[0][1], '#')
        win.border(0)
        win.addstr(0, 2, 'Score : ' + str(score) + ' ') # Printing 'Score' and
        win.addstr(0, 27, ' SNAKE ') # 'SNAKE' strings
        win.timeout(delay) # Increases the speed of Snake as its length increases

def draw_features(win, features, board):
    win.addstr(board['height']-1, 2, str({'f': features[0], 'l': features[1], 'r': features[2], 'a': features[3]}))


def random_action(prev_action, features):
    action = randint(0, 2) - 1
    dir = {
        KEY_UP: {-1: KEY_LEFT, 0: KEY_UP, 1: KEY_RIGHT},
        KEY_LEFT: {-1: KEY_DOWN, 0: KEY_LEFT, 1: KEY_UP},
        KEY_RIGHT: {-1: KEY_UP, 0: KEY_RIGHT, 1: KEY_DOWN},
        KEY_DOWN: {-1: KEY_RIGHT, 0: KEY_DOWN, 1: KEY_LEFT}
    }

    return dir[prev_action][action], action

def neural_action(prev_action, features):
    dir = {
        KEY_UP: {-1: KEY_LEFT, 0: KEY_UP, 1: KEY_RIGHT},
        KEY_LEFT: {-1: KEY_DOWN, 0: KEY_LEFT, 1: KEY_UP},
        KEY_RIGHT: {-1: KEY_UP, 0: KEY_RIGHT, 1: KEY_DOWN},
        KEY_DOWN: {-1: KEY_RIGHT, 0: KEY_DOWN, 1: KEY_LEFT}
    }

    left = network.test(features[:-1] + (-1,))
    front = network.test(features[:-1] + (0,))
    right = network.test(features[:-1] + (1,))


    if left == max(left, front, right):
        return dir[prev_action][-1], -1
    elif front == max(left, front, right):
        return dir[prev_action][0], 0
    else:
        return dir[prev_action][1], 1


def neural_action2(prev_action, features):
    dir = {
        KEY_UP: {-1: KEY_LEFT, 0: KEY_UP, 1: KEY_RIGHT},
        KEY_LEFT: {-1: KEY_DOWN, 0: KEY_LEFT, 1: KEY_UP},
        KEY_RIGHT: {-1: KEY_UP, 0: KEY_RIGHT, 1: KEY_DOWN},
        KEY_DOWN: {-1: KEY_RIGHT, 0: KEY_DOWN, 1: KEY_LEFT}
    }

    left = network.test(features[:-2] + (features[-1], -1))
    front = network.test(features[:-2] + (features[-1], 0))
    right = network.test(features[:-2] + (features[-1], 1))


    if left == max(left, front, right):
        return dir[prev_action][-1], -1
    elif front == max(left, front, right):
        return dir[prev_action][0], 0
    else:
        return dir[prev_action][1], 1


def food_distance(snek, food):
    head = snek[0]
    return math.sqrt((head[0] - food[0]) ** 2 + (head[1] - food[1]) ** 2)

def snek(player=False, gui=False, snek=None, action=random_action):
    win = init_gui()
    key, score, delay, snake, food = init_state(player, gui, snek)

    win.addch(food[0], food[1], '*') # Prints the food

    while key != 27: # While Esc key is not pressed
        prevKey = key # Previous key pressed
        prev_dist = food_distance(snake, food)
        prev_score = score

        features = extract_features(snake, board, score, food, key, key)

        event = win.getch()
        if player:
            key, choosen_action = get_input(player, event, key)
        else:
            key, choosen_action = action(prevKey, features)

        if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]: # If an invalid key is pressed
            key = prevKey

        features = extract_features(snake, board, score, food, key, choosen_action)

        calculate_head(snake, key)

        last = None
        if eat_food(snake, food):
            food = new_food(snake)
            score += 1
        else:
            last = snake.pop()  # [1] If it does not eat the food, length stays same

        new_dist = food_distance(snake, food)

        if violated_boundary_conditions(snake):
            result = -1
        elif violated_boundary_conditions(snake) and (new_dist < prev_dist or score > prev_score):
            result = 0.5
        elif not violated_boundary_conditions(snake) and (new_dist < prev_dist) or score > prev_score:
            result = 1
        else:
            result = -0.5

        features = extract_features(snake, board, score, food, key, choosen_action)
        learning_data.append((*features, result))

        prev_score = score

        if violated_boundary_conditions(snake):
            break

        if gui:
            draw(win, snake, food, delay, score, last)
            draw_features(win, features, board)


    curses.endwin()
    return score

learning_data = []

def learn():
    start_time = time()
    while len(learning_data) < 1000:
        score = snek(player=True, gui=True)
    end_time = time()

    print(end_time - start_time)

    with open('snek-learning1.yaml', 'w') as file:
        yaml.dump(learning_data, file)

#network = load_network('snek-survive.yaml')
network = load_network('snek-play-awesome.yaml')

def test():
    for _ in range(5):
        score = snek(player=False, gui=True, action=neural_action2)

#learn()
test()
