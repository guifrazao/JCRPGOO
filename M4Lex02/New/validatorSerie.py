class SerieValidator:
    def __init__(self, serie_min=1000):
        self.SERIE_MIN = serie_min

    def validar(self, serie):
        if serie < self.SERIE_MIN:
            raise ValueError(f"Número de série deve ser maior que {self.SERIE_MIN}")