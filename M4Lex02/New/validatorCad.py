class CadenciaValidator:
    def validar(self, cadencia):
        if cadencia < 0:
            raise ValueError("Cadência dos pedais deve ser maior ou igual a 0")