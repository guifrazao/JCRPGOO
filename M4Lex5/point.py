import math

class Point:
    def __init__(self, x=1, y=1):
        self._x = x
        self._y = y
        print(f"\n-> Ponto inicializado em: ({self._x}, {self._y})")

    def move(self, dx, dy):
        print(f"\n-> Movendo o ponto de ({self._x}, {self._y}) para ({self._x + dx}, {self._y + dy})")
        self._x += dx
        self._y += dy
        print(f"   Novo ponto: ({self._x}, {self._y})")

    def distance(self, other_point):
        dx = self._x - other_point._x
        dy = self._y - other_point._y
        dist = math.sqrt(dx**2 + dy**2)
        print(f"\n-> Distância entre os pontos ({self._x}, {self._y}) e ({other_point._x}, {other_point._y}) é: {dist:.2f}")
        return dist

    def set_values(self, x, y):
        print(f"\n-> Atualizando o ponto de ({self._x}, {self._y}) para ({x}, {y})")
        self._x = x
        self._y = y
        print(f"   Ponto atualizado: ({self._x}, {self._y})")
