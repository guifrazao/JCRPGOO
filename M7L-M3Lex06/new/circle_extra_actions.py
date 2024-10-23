import math

class CircleCircumference:
    def __init__(self, circle):
        self.circle = circle

    def execute(self):
        return 2 * math.pi * self.circle.get_radius()
