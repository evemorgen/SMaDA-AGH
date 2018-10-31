import re
from typing import List


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


solids = import_data('solid_data.txt')
print(solids)
