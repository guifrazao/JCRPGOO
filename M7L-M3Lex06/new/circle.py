'''
M3L-ex06. Escreva uma classe Circle composta de um ponto para indicar o centro e o tamanho 
do raio, que não deve ser menor que zero. Utilize a classe Point criada anteriormente. 
Crie métodos get e set para testar sua classe. A seguir crie:  
a. Um método que retorne a área do círculo. 
b. Um método move que movimente o centro do círculo (utilize o método move 
da classe ponto). 
Crie e teste um construtor para a classe Circle com todos os valores zerados, mas 
que também possa receber valores dados.
'''

from point import Point
import math

class Circle:
    def __init__(self, center=Point(), radius=0):
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

    def perform_extra_action(self, action):
        return action.execute()
