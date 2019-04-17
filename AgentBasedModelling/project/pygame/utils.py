import logging
import yaml
import functools

from time import time
from typing import List
from dataclasses import dataclass


def load_config(filename):
    with open(filename, 'r') as yml_file:
        return yaml.load(yml_file)


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class RoundRobin:
    def __init__(self):
        self.i = 0

    def get(self, data):
        self.i = (self.i + 1) % len(data)
        return data[self.i]


@dataclass
class TimeRange:
    start: float
    end: float
    vin: str

    def overlap(self, other: 'TimeRange'):
        latest_start = max(self.start, other.start)
        earliest_end = min(self.end, other.end)
        delta = earliest_end - latest_start
        overlap = max(0, delta)
        return overlap

    def inside(self, point):
        return self.end > point > self.start

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end and self.vin == other.vin


class Timeline:
    def __init__(self):
        self.timeline: List[TimeRange] = []

    def add_timespan(self, start: float, end: float = None, duration: float = None, vin=None) -> bool:
        if end is not None and end > start:
            raise ValueError("End must be greater than the start")
        new_range = TimeRange(start, end if end is not None else start + duration, vin)
        logging.debug(f"adding reservation for {vin} in range {new_range}")
        if any(map(lambda r: r.overlap(new_range) > 0, self.timeline)):
            logging.debug(f"reservation overlaps current timeline: {self.timeline}")
            return False
        self._insert_timespan(new_range)
        return True

    def cancel_timespan(self, start, end=None, duration=None, vin=None) -> bool:
        to_remove = TimeRange(start, end if end is not None else start + duration, vin)
        self.timeline = [e for e in self.timeline if e != to_remove]
        return True

    def within_reserved(self, timestamp):
        return any([time_range.inside(timestamp) for time_range in self.timeline])

    def _insert_timespan(self, new_r: TimeRange) -> None:
        logging.debug(f"inserting range: {new_r}")
        if self.timeline == []:
            logging.debug("fresh new timeline, one element")
            self.timeline = [new_r]
        elif len(self.timeline) == 1 and new_r.end < self.timeline[0].start:
            logging.debug("adding second range to timeline up front")
            self.timeline.insert(0, new_r)
        elif len(self.timeline) == 1 and new_r.start > self.timeline[0].end:
            self.timeline.append(new_r)
            logging.debug("adding second range to timeline behind")
        else:
            for r1, r2 in zip(self.timeline, self.timeline[1:]):
                logging.debug(f"trying {r1} and {r2}")
                if new_r.end < r1.start:
                    logging.debug("adding third and more ranges before anything else")
                    self.timeline.insert(self.timeline.index(r1), new_r)
                    break
                elif new_r.start > r1.end and new_r.end < r2.start:
                    logging.debug(f"adding third and more ranges between {r1} and {r2}")
                    self.timeline.insert(self.timeline.index(r1) + 1, new_r)
                    break
            else:
                self.timeline.append(new_r)

    def _clear_old_events(self, when=None):
        if when is None:
            when = time()
        self.timeline = [e for e in self.timeline if e.start > when]

    def __repr__(self):
        return f"Timeline{self.timeline}"


def hash_dict(func):
    """Transform mutable dictionnary
    Into immutable
    Useful to be compatible with cache
    """
    class HDict(dict):
        def __hash__(self):
            return hash(frozenset(self.items()))

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        args = tuple([HDict(arg) if isinstance(arg, dict) else arg for arg in args])
        kwargs = {k: HDict(v) if isinstance(v, dict) else v for k, v in kwargs.items()}
        return func(*args, **kwargs)
    return wrapped
