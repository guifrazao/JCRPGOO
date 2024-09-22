"""
Refazer o exercício aplicando o Princípio da Responsabilidade Única e mostrar as
diferenças de seu código, antes e depois.
"""

class Bicycle:
    def __init__(self, velocidade, cadencia, marcha, serie):
        self.__velocidade = velocidade  
        self.__cadencia = cadencia    
        self.__marcha = marcha          
        self.__serie = serie   

    def get_velocidade(self):
        return self.__velocidade

    def get_cadencia(self):
        return self.__cadencia

    def get_marcha(self):
        return self.__marcha

    def get_serie(self):
        return self.__serie

    def set_velocidade(self, velocidade):
        self.__velocidade = velocidade

    def set_cadencia(self, cadencia):
        self.__cadencia = cadencia

    def set_marcha(self, marcha):
        self.__marcha = marcha

    def set_serie(self, serie):
        self.__serie = serie

    def velocidade_relativa(self, outra_bicicleta):
        return abs(self.__velocidade - outra_bicicleta.get_velocidade())

    def __str__(self):
        return (f"Velocidade: {self.__velocidade}\n"
                f"Cadência: {self.__cadencia}\n"
                f"Marcha: {self.__marcha}\n"
                f"Número de série: {self.__serie}")

    
class BicycleValidator:
    def __init__(self):
        self.MIN_MARCHA = 1
        self.MAX_MARCHA = 18
        self.SERIE_MIN = 1000

    def validar_velocidade(self, velocidade):
        if velocidade < 0:
            raise ValueError("Velocidade deve ser maior ou igual a 0")

    def validar_cadencia(self, cadencia):
        if cadencia < 0:
            raise ValueError("Cadência dos pedais deve ser maior ou igual a 0")

    def validar_marcha(self, marcha):
        if marcha < self.MIN_MARCHA or marcha > self.MAX_MARCHA:
            raise ValueError(f"Marcha inválida! Deve estar entre {self.MIN_MARCHA} e {self.MAX_MARCHA}")

    def validar_serie(self, serie):
        if serie < self.SERIE_MIN:
            raise ValueError(f"Número de série deve ser maior que {self.SERIE_MIN}")

        