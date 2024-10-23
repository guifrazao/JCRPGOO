import math

class Point:
    def __init__(self, x=1, y=1):
        # Construtor que inicializa x e y em 1, mas pode receber valores
        self._x = x
        self._y = y

    # Métodos get e set para x e y
    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

    # Método para movimentar o ponto
    def move(self, dx, dy):
        self._x += dx
        self._y += dy
        print(f"Movido para nova posição: ({self._x}, {self._y})")

    # Método que retorna a distância entre este ponto e outro ponto
    def distance(self, other_point):
        dx = self._x - other_point.get_x()
        dy = self._y - other_point.get_y()
        dist = math.sqrt(dx**2 + dy**2)
        return dist
