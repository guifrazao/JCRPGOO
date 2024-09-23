import math

class Point:
    def __init__(self, x=1, y=1):
        # Inicializa o ponto
        self._x = x
        self._y = y

    def move(self, dx, dy):
        # Movimenta o ponto
        self._x += dx
        self._y += dy

    def distance(self, other_point):
        # Calcula a distância entre dois pontos
        dx = self._x - other_point._x
        dy = self._y - other_point._y
        return math.sqrt(dx**2 + dy**2)

    def set_values(self, x, y):
        # Define novos valores para o ponto
        self._x = x
        self._y = y


class PointPrinter:
    @staticmethod
    def print_initialization(point):
        print(f"\n-> Ponto inicializado em: ({point._x}, {point._y})")

    @staticmethod
    def print_move(old_x, old_y, new_x, new_y):
        print(f"\n-> Movendo o ponto de ({old_x}, {old_y}) para ({new_x}, {new_y})")

    @staticmethod
    def print_distance(point1, point2, dist):
        print(f"\n-> Distância entre os pontos ({point1._x}, {point1._y}) e ({point2._x}, {point2._y}) é: {dist:.2f}")

    @staticmethod
    def print_update(old_x, old_y, new_x, new_y):
        print(f"\n-> Atualizando o ponto de ({old_x}, {old_y}) para ({new_x}, {new_y})")

