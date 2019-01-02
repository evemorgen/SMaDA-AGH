from time import time
from typing import List, Optional
from dataclasses import dataclass
from car import Car
import yaml


def load_config(filename):
    with open(filename, 'r') as yml_file:
        return yaml.load(yml_file)


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

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end and self.car == other.car



class Timeline:
    def __init__(self):
        self.timeline: List[TimeRange] = []

    def add_timespan(self, start: float, end: float = None, duration: float = None, vin=None) -> bool:
        if end is not None and end > start:
            raise ValueError("End must be greater than the start")
        #self._clear_old_events()
        new_range = TimeRange(start, end if end is not None else start + duration, vin)
        if any(map(lambda r: r.overlap(new_range) > 0, self.timeline)):
            return False
        self._insert_timespan(new_range)
        return True

    def cancel_timespan(self, start, end=None, duration=None, vin=None) -> bool:
        to_remove = TimeRange(start, end if end is not None else start + duration, vin)
        self.timeline = [e for e in self.timeline if e != to_remove]
        return True


    def _insert_timespan(self, new_r: TimeRange) -> None:
        if self.timeline == []:
            self.timeline = [new_r]
        elif len(self.timeline) == 1 and new_r.end < self.timeline[0].start:
            self.timeline.insert(0, new_r)
        elif len(self.timeline) == 1 and new_r.start > self.timeline[0].end:
            self.timeline.append(new_r)
        else:
            for r1, r2 in zip(self.timeline, self.timeline[1:]):
                if new_r.end < r1.start:
                    self.timeline.insert(0, new_r)
                    break
                elif new_r.start > r1.end and new_r.end < r2.start:
                    self.timeline.insert(self.timeline.index(r1)+1, new_r)
                    break

    def _clear_old_events(self, when=None):
        if when is None:
            when = time()
        self.timeline = [e for e in self.timeline if e.start > when]

    def __repr__(self):
        return f"Timeline{self.timeline}"

