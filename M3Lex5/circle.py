'''
Escreva uma classe Circle composta de um ponto para indicar o centro e o tamanho 
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
    """Representa um círculo."""

    def __init__(self, center=Point(), radius=1):
        """Construtor da classe Circle."""
        self.__center = center
        self.__radius = radius if radius >= 0 else 0

    def get_radius(self):
        """Retorna o valor do raio do círculo."""
        return self.__radius

    def set_radius(self, value):
        """Atualiza o raio do círculo, desde que seja um valor não negativo."""
        self.__radius = self.verify_radius(value)
        
    def verify_radius(self, value):
        """Verifica se o raio é menor que zero."""
        if value >= 0:
            return value
        else:
            print("Aviso: O raio não pode ser menor que zero. O raio não foi alterado.")
            return self.__radius 

    def area(self):
        """Calcula e retorna a área do círculo."""
        return math.pi * self.__radius ** 2

    def move(self, dx, dy):
        """Move o círculo pela distância especificada nos parâmetros dx e dy."""
        self.__center.move(dx, dy)

    def __str__(self):
        """Retorna uma string descrevendo o círculo, incluindo seu centro e raio."""
        return f"Círculo com centro em ({self.__center._x}, {self.__center._y}) e raio {self.__radius}"
