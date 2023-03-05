import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__x - x), abs(self.__y - y))  # hypot function calculates the length of the
    # hypotenuse of a right triangle
    # we calculate from our point to a new coordinate - given as a parameter to the function

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.a = vertice1
        self.b = vertice2
        self.c = vertice3

    def perimeter(self):
        return (
            self.a.distance_from_point(self.b) +
            self.b.distance_from_point(self.c) +
            self.a.distance_from_point(self.c)
        )


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
