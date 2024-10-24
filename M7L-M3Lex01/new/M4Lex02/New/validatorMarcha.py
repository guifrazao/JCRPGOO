class MarchaValidator:
    def __init__(self, min_marcha=1, max_marcha=18):
        self.MIN_MARCHA = min_marcha
        self.MAX_MARCHA = max_marcha

    def validar(self, marcha):
        if marcha < self.MIN_MARCHA or marcha > self.MAX_MARCHA:
            raise ValueError(f"Marcha inválida! Deve estar entre {self.MIN_MARCHA} e {self.MAX_MARCHA}")