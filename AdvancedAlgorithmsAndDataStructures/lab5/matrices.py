import json
import time
import math
import multiprocessing
from pandas import DataFrame

from typing import List, Tuple
from functools import reduce

matrix = List[List[float]]


def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print('%r - %s ms' % (method.__name__, te - ts))
        return result

    return timed


def mul_s(x: matrix, y: matrix) -> matrix:
    return [[sum(a * b for a, b in zip(x_row, y_col)) for y_col in zip(*y)] for x_row in x]


@timeit
def mul_all(m_list: List[matrix]) -> matrix:
    return reduce(mul_s, m_list)


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def generate_tasks(to_multiply):
    return list(chunks(to_multiply, 2))


def mul_st(tup: Tuple[matrix, matrix]):
    if len(tup) == 2:
        return mul_s(*tup)
    else:
        return tup[0]


@timeit
def after_pool(m_list, pool):
    tasks = generate_tasks(m_list)
    while len(tasks) != 1:
        result = pool.map(mul_st, tasks)
        tasks = generate_tasks(result)
    return mul_st(result)


def mul_all_p(m_list: List[matrix]) -> matrix:
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    return after_pool(m_list, pool)


def flatten_matrix(m_list: List[matrix]) -> List[float]:
    return sum(m_list, [])


x = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
y = [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]
z = [[1, 2], [3, 4], [5, 6], [7, 8]]

matrices = json.load(open('matrix.json', 'r'))
s1, p1 = mul_all([x, y, z]), mul_all_p([x, y, z])
assert s1 == p1
s2, p2 = mul_all(matrices), mul_all_p(matrices)
assert all([math.isclose(s, p) for s, p in zip(flatten_matrix(s2), flatten_matrix(p2))])
print(DataFrame(s2))
