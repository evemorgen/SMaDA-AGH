import re
import itertools
from math import sqrt
from multimethod import multimethod

from geom import Point, Edge, Face, Solid
from vec import Vector, cross, dot


def import_data(filename):
    lines = open(filename, 'r').read()
    solids = re.split("--- SOLID \[\d*\]---", lines)
    return [
        Solid([
            Face(
                *[Point(*[float(p) for p in point.split(";")])
                    for point in face.split("\n") if len(point) != 0]
            ) for face in solid.split("\n\n") if face != ""
        ]) for solid in solids if solid != ""
    ]


@multimethod  # noqa: F811
def distance(a: Point, b: Point) -> float:
    # https://math.stackexchange.com/questions/42640/calculate-distance-in-3d-space
    return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2)


@multimethod  # noqa: F811
def distance(a: Face, b: Face) -> float:
    # http://www.ikonstantinos.com/Konstantinos_Krestenitis_ACME2015.pdf
    ae1, ae2, ae3 = a.edges
    be1, be2, be3 = b.edges
    distances = [
        distance(a, b.p1),
        distance(a, b.p2),
        distance(a, b.p3),
        distance(b, a.p1),
        distance(b, a.p2),
        distance(b, a.p3),
        distance(ae1, be1),
        distance(ae1, be2),
        distance(ae1, be3),
        distance(ae2, be1),
        distance(ae2, be2),
        distance(ae2, be3),
        distance(ae3, be1),
        distance(ae3, be2),
        distance(ae3, be3)
    ]
    return min(distances)


@multimethod  # noqa: F811
def distance(f: Face, p: Point) -> float:
    # http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.104.4264&rep=rep1&type=pdf
    # p point projection to plane which face f lays in
    # normal Np of P1P2P3
    np = cross(Vector(f.p1, f.p2), Vector(f.p1, f.p3))

    # the angle a between normal Np and P1P0
    cosa = dot(Vector(f.p1, p), np) / (np.length() * Vector(f.p1, p).length())

    # the length of P0P0'
    p0p0l = Vector(p, f.p1).length() * cosa

    # the vector P0P0'
    p0p0p = np * ((-1) * (p0p0l) / np.length())

    # point P0' from P0 and P0P0' vector
    p0p = p + p0p0p

    # compute baricentric coordinates
    area = cross(Vector(f.p1, f.p2), Vector(f.p1, f.p3)).length() / 2
    a = cross(Vector(p0p, f.p2), Vector(p0p, f.p3)).length() / (2 * area)
    b = cross(Vector(p0p, f.p3), Vector(p0p, f.p1)).length() / (2 * area)
    c = 1 - a - b

    if 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1:
        return sqrt(dot(p0p0p, p0p0p))
    else:
        e1 = Edge(f.p1, f.p2)
        e2 = Edge(f.p2, f.p3)
        e3 = Edge(f.p1, f.p3)

        return min(distance(e1, p), distance(e2, p), distance(e3, p), distance(f.p1, p), distance(f.p2, p), distance(f.p3, p))


@multimethod  # noqa: F811
def distance(a: Solid, b: Solid) -> float:
    distances = [distance(f1, f2) for f1, f2 in itertools.product(a.faces, b.faces)]
    return min(distances)


@multimethod  # noqa: F811
def distance(e: Edge, p: Point) -> float:
    # http://geomalgorithms.com/a02-_lines.html#Distance-to-Ray-or-Segment
    v = Vector(e.p1, e.p2)
    w = Vector(e.p1, p)
    c1 = dot(w, v)
    c2 = dot(v, v)
    b = c1 / c2
    pb = Point(
        e.p1.x + b * v.x,
        e.p1.y + b * v.y,
        e.p1.z + b * v.z
    )

    if c1 <= 0:
        return distance(p, e.p1)
    if c2 <= c1:
        return distance(p, e.p2)
    return distance(p, pb)


@multimethod  # noqa: F811
def distance(e1: Edge, e2: Edge) -> float:
    # http://geomalgorithms.com/a07-_distance.html#dist3D_Segment_to_Segment()
    SMALL_NUM = 0.00000001
    u, v, w = Vector(e1.p1, e1.p2), Vector(e2.p1, e2.p2), Vector(e2.p1, e1.p1)
    a, b, c, d, e = dot(u, u), dot(u, v), dot(v, v), dot(u, w), dot(v, w)
    D = a * c - b * b
    sc, sN, sD = D, D, D
    tc, tN, tD = D, D, D

    if D < SMALL_NUM:
        sN, sD = 0.0, 1.0
        tN, tD = e, c
    else:
        sN, tN = (b * e - c * d), (a * e - b * d)
        if sN < 0.0:
            sN, tN, tD = 0.0, e, c
        elif sN > sD:
            sN, tN, tD = sD, e + b, c
    if tN < 0.0:
        tN = 0.0
        if -d < 0.0:
            sN = 0.0
        elif -d > a:
            sN = sD
        else:
            sN, sD = -d, a
    elif tN > tD:
        tN = tD
        if (-d + b) < 0.0:
            sN = 0
        elif (-d + b) > a:
            sN = sD
        else:
            sN, sD = (-d + b), a

    sc = sN / sD
    tc = tN / tD
    dP = w + (u * sc) - (v * tc)
    return dP.length()


@multimethod  # noqa: F811
def distance(a: Edge, b: Face) -> float:
    eb1, eb2, eb3 = b.edges
    return min(
        distance(a, eb1),
        distance(a, eb2),
        distance(a, eb3),
        distance(a, b.p1),
        distance(a, b.p2),
        distance(a, b.p3)
    )


if __name__ == '__main__':
    solids = import_data('solid_data.txt')
    print("solids :", distance(solids[0], solids[1]))
    print("face (1, 0, 0), (0, 1, 0), (0, 0, 0) to face (100, 0, 0.13), (0, 100, 0.13), (-100, -100, 0.13)", distance(
        Face(Point(1, 0, 0), Point(0, 1, 0), Point(0, 0, 0)),
        Face(Point(100, 0, 0.13), Point(0, 100, 0.13), Point(-100, -100, 0.13))
    ))
    """
    print("points: 0, 0, 0 to 10, 10, 10: ", distance(
        Point(0, 0, 0),
        Point(10, 10, 10)
    ))
    print("edge (1, 2, 3), (2, 4, 6) to point (10, 10, 10): ", distance(
        Edge(Point(1, 2, 3), Point(2, 4, 6)),
        Point(10, 10, 10)
    ))
    print("edge (1, 2, 3), (2, 4, 6) to edge (4, 4, 4), (5, 6, 7): ", distance(
        Edge(Point(1, 2, 3), Point(2, 4, 6)),
        Edge(Point(4, 4, 4), Point(5, 6, 7))
    ))
    print("face (0, 0, 0), (10, 10, 10), (100, 0, 0.13) to point (0, 100, 0.13): ", distance(
        Face(Point(0, 0, 0), Point(10, 10, 10), Point(100, 0, 0.13)),
        Point(0, 100, 0.13)
    ))
    print("edge (1, 2, 3), (2, 4, 6) to face (0, 0, 0), (10, 10, 10), (100, 0, 0.13): ", distance(
        Edge(Point(1, 2, 3), Point(2, 4, 6)),
        Face(Point(0, 0, 0), Point(10, 10, 10), Point(100, 0, 0.13))
    ))
    print("face (1.0, 0.0, 0), (0, 1, 0), (0, 0, 0) to face (100, 0, 0.13), (0, 100, 0.13), (-100, -100, 0.13)", distance(
        Face(Point(3, 3, 2), Point(0, 3, 2), Point(3, 0, 2)),
        Face(Point(4, 4, -2), Point(15, 18, -3), Point(22, -3, -2.5))
    ))
    """
