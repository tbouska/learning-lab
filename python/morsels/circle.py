import math


class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.radius})"

    @property
    def radius(self):
        return self.__radius

    @property
    def diameter(self):
        return 2*self.radius

    @property
    def area(self):
        return math.pi*(math.pow(self.radius, 2))

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        else:
            self.__radius = value

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @area.setter
    def area(self, value):
        raise AttributeError("Cannot set attribute area")


if __name__ == "__main__":
    c = Circle(1.5)
    dir(c)
    print(c)
    c.radius = 3
    print(c)
    c.area = 30
    print(c)
