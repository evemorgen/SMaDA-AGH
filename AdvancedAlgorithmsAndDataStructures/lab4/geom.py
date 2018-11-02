from dataclasses import dataclass, field
from typing import List


@dataclass
class Point:
    x: float
    y: float
    z: float

    def __add__(self, other):
        import vec
        if isinstance(other, vec.Vector):
            return Point(
                self.x + other.x,
                self.y + other.y,
                self.z + other.z
            )


@dataclass
class Edge:
    p1: Point
    p2: Point


@dataclass
class Face:
    p1: Point
    p2: Point
    p3: Point

    @property
    def edges(self):
        return [
            Edge(self.p1, self.p2),
            Edge(self.p2, self.p3),
            Edge(self.p1, self.p3)
        ]


@dataclass
class Solid:
    faces: List[Face] = field(default_factory=list)
