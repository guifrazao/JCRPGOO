import math

class Point:
    def __init__(self, x=1, y=1):
        self._x = x
        self._y = y

    def move(self, dx, dy):
        self._x += dx
        self._y += dy

    def get_coordinates(self):
        return self._x, self._y


class PointPrinter:
    def print_initial(self, point):
        print(f"\n-> Ponto inicializado em: {point.get_coordinates()}")

    def print_move(self, point, dx, dy):
        original_coords = point.get_coordinates()
        new_coords = (original_coords[0] + dx, original_coords[1] + dy)
        print(f"\n-> Movendo o ponto de {original_coords} para {new_coords}")
        print(f"   Novo ponto: {new_coords}")

    def print_distance(self, point1, point2, distance):
        print(f"\n-> Distância entre os pontos {point1.get_coordinates()} e {point2.get_coordinates()} é: {distance:.2f}")

    def print_update(self, point, x, y):
        original_coords = point.get_coordinates()
        print(f"\n-> Atualizando o ponto de {original_coords} para ({x}, {y})")
        print(f"   Ponto atualizado: ({x}, {y})")


class PointOperations:
    def calculate_distance(self, point1, point2):
        dx = point1._x - point2._x
        dy = point1._y - point2._y
        return math.sqrt(dx**2 + dy**2)

