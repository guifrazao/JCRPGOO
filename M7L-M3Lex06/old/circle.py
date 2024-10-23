from point import Point
import math

class Circle:
    def __init__(self, center: Point, radius=0):
        self.__center = center
        self.__radius = radius if radius >= 0 else 0

    def get_center(self):
        return self.__center

    def set_center(self, center):
        self.__center = center

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        if radius >= 0:
            self.__radius = radius
        else:
            print("O raio não pode ser menor que zero.")

    def area(self):
        return math.pi * (self.__radius ** 2)

    def move(self, dx, dy):
        self.__center.move(dx, dy)

    def get_circle_data(self):
        return f"Círculo com centro em ({self.__center._x}, {self.__center._y}) e raio {self.__radius}"
