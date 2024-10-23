# Escreva uma classe Point descrito por coordenadas reais x, y. Crie métodos get e set
# e faça um programa de teste para a sua classe. A seguir, crie e teste os seguintes
# métodos para a classe Ponto:
# a. O método que recebe como parâmetros um deslocamento dx e outro dy para
# movimentar o Ponto.
# b. O método que retorna a distância entre este ponto e outro dado como
# parâmetro.
# Crie e teste um construtor para a classe Point, que inicialize x e y em 1, mas que
# também possa receber valores dados.

import math

class Point:
    def __init__(self, x=1, y=1):
        # Inicializa o ponto e imprime a coordenada inicial
        self._x = x
        self._y = y

    def move(self, dx, dy):
        # Movimenta o ponto e imprime a nova posição
        print(f"\nMovendo o ponto de ({self._x}, {self._y}) para ({self._x + dx}, {self._y + dy})")
        self._x += dx
        self._y += dy

    def distance(self, other_point):
        # Calcula a distância entre dois pontos e imprime o resultado
        dx = self._x - other_point._x
        dy = self._y - other_point._y
        dist = math.sqrt(dx**2 + dy**2)
        print(f"\nDistância entre os pontos ({self._x}, {self._y}) e ({other_point._x}, {other_point._y}) é: {dist:.2f}")
        return dist 
    
    def get_values(self):
        print(f"Coordenada atual do ponto: ({self._x}, {self._y})")
    
    def set_values(self, x, y):
        # Define novos valores para o ponto e imprime a atualização
        print(f"\nAtualizando o ponto de ({self._x}, {self._y}) para ({x}, {y})")
        self._x = x
        self._y = y
        print(f"Ponto atualizado: ({self._x}, {self._y})")
