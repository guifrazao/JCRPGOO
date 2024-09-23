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