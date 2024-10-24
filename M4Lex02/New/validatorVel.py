class VelocidadeValidator:
    def validar(self, velocidade):
        if velocidade < 0:
            raise ValueError("Velocidade deve ser maior ou igual a 0")