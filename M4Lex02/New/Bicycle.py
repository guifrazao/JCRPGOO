class Bicycle:
    MIN_MARCHA = 1
    MAX_MARCHA = 18
    SERIE_MIN = 1000
    def __init__(self,velocidade,cadencia,marcha,serie):
        self.__velocidade = velocidade
        self.__cadencia = cadencia
        self.__marcha = marcha
        self.__serie = serie

    def getVelocidade(self):
        return self.__velocidade
    
    def getCadencia(self):
        return self.__cadencia
    
    def getMarcha(self):
        return self.__marcha
    
    def getSerie(self):
        return self.__serie
    
    def set_velocidade(self, velocidade):
        if velocidade >= 0:
            self.__velocidade = velocidade
        else:
            raise ValueError("Velocidade deve ser maior ou igual a 0")

    def set_cadencia(self,cadencia):
        if cadencia >= 0:
            self.__cadencia = cadencia
        else:
            raise ValueError("Cadência dos pedais deve ser maior ou igual a 0")
        
    def set_marcha(self,marcha):
        if Bicycle.MIN_MARCHA <= marcha <= Bicycle.MAX_MARCHA:
            self.__marcha = marcha
        else:
            raise ValueError(f"Marcha inválida! Deve estar entre {Bicycle.MIN_MARCHA} e {Bicycle.MAX_MARCHA}")
    
    def set_serie(self,serie):
        if serie >= 1000:
            self.__serie = serie
        else:
            raise ValueError(f"Número de série deve ser maior que {Bicycle.SERIE_MIN}")

    def velocidade_relativa(self,bike2):
        return abs(self.__velocidade - bike2.__velocidade)

    def __str__(self):
        return (f"Velocidade: {self.__velocidade}\n"
                f"Cadência: {self.__cadencia}\n"
                f"Marcha: {self.__marcha}\n"
                f"Número de série: {self.__serie}")

