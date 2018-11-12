from typing import Optional
from math import sqrt

from geom import Point


class Vector:
    def __init__(self, p1: Point, p2: Optional[Point] = None):
        if p2 is not None:
            self.x: float = p2.x - p1.x
            self.y: float = p2.y - p1.y
            self.z: float = p2.z - p1.z
        else:
            self.x: float = p1.x
            self.y: float = p1.y
            self.z: float = p1.z

    def __add__(self, other: 'Vector'):
        return Vector(Point(self.x + other.x, self.y + other.y, self.z + other.z))

    def __sub__(self, other: 'Vector'):
        return Vector(Point(self.x - other.x, self.y - other.y, self.z - other.z))

    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(Point(self.x * other, self.y * other, self.z * other))

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(Point(self.x / other, self.y / other, self.z / other))

    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y}, z={self.z})"


def dot(v1: Vector, v2: Vector) -> float:
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z


def cross(v1: Vector, v2: Vector) -> Vector:
    return Vector(
        Point(v1.z * v2.y, v1.x * v2.z, v1.y * v2.x),
        Point(v1.y * v2.z, v1.z * v2.x, v1.x * v2.y)
    )
