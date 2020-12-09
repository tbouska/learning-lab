#!/usr/bin/env python3
# point.py
""" This is my solution to compact Morsel """


class Point():
    """ 3D Point """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, val):
        return Point(self.x * val, self.y * val, self.z * val)

    def __rmul__(self, val):
        return Point(val * self.x, val * self.y, val * self.z)

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z


if __name__ == "__main__":
    p1 = Point(1, 2, 3)
    print(p1)
    p2 = Point(1, 2, 3)
    print(p1 == p2)
    p2.x = 4
    print(p1 == p2)
    print(p2)
    p2 = Point(4, 5, 6)
    print(p1 + p2)
    p3 = p2 - p1
    print(p3)
    p4 = p1 * 2.0
    print(p4)
    x, y, z = p1
    print(x,y,z)
