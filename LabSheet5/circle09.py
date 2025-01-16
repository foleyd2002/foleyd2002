import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = math.pi * math.pow(self.radius, 2)
        return area

    def get_circumference(self):
        circumference = 2 * math.pi * self.radius
        return circumference

    def __str__(self):
        return "c{}".format(self.radius)

    def __eq__(self, other):
        return self.radius == other.radius
