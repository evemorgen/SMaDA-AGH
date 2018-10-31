import re
from typing import List
from multimethod import multimethod


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.z})"


class Face:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1, self.p2, self.p3 = (p1, p2, p3)
        self.edges = []

    def get_edges():
        pass

    def __repr__(self):
        return f"Face({self.p1}, {self.p2}, {self.p3}),"


class Edge:
    pass


class Solid:
    def __init__(self, faces: List[Face]):
        self.faces = faces

    def __repr__(self):
        return f"Solid(\n" + "".join([f"    {face}\n" for face in self.faces]) + ")"


def import_data(filename):
    lines = open(filename, 'r').read()
    # --- SOLID [12968383250903502554]---
    solids = re.split("--- SOLID \[\d*\]---", lines)
    return [
        Solid([
            Face(
                *[Point(*point.split(";")) for point in face.split("\n") if len(point) != 0]
            ) for face in solid.split("\n\n") if face != ""
        ]) for solid in solids if solid != ""
    ]


@multimethod  # noqa: F811
def distance(a: Point, b: Point) -> float:
    print("POINTS")


@multimethod  # noqa: F811
def distance(a: Face, b: Face) -> float:
    print("FACES")


@multimethod  # noqa: F811
def distance(a: Face, b: Point) -> float:
    print("FACE-POINT")


@multimethod  # noqa: F811
def distance(a: Solid, b: Solid) -> float:
    print("SOLIDS")


@multimethod  # noqa: F811
def distance(a: Edge, b: Point) -> float:
    print("EDGE-POINT")


@multimethod  # noqa: F811
def distance(a: Edge, b: Edge) -> float:
    print("EDGES")


@multimethod  # noqa: F811
def distance(a: Edge, b: Face) -> float:
    print("EDGE-FACE")


solids = import_data('solid_data.txt')

distance(solids[0], solids[1])
distance(solids[0].faces[0], solids[0].faces[1])
