class Bicicleta:
    def __init__(self, velocidade_atual, cadencia, marcha):
        self.__velocidade_atual = velocidade_atual
        self.__cadencia = cadencia
        self.__marcha = marcha
        self.__proprietario = None

    def iniciar_pedal(self):
        print("Iniciando a pedalada...")

    def obter_velocidade_atual(self):
        return self.__velocidade_atual  # km/h

    def definir_velocidade_atual(self, velocidade_atual):
        self.__velocidade_atual = velocidade_atual

    def obter_cadencia(self):
        return self.__cadencia  # rpm

    def definir_cadencia(self, cadencia):
        self.__cadencia = cadencia

    def obter_marcha(self):
        return self.__marcha

    def definir_marcha(self, marcha):
        self.__marcha = marcha

    def obter_proprietario(self):
        return self.__proprietario

    def definir_proprietario(self, proprietario):
        self.__proprietario = proprietario

    def calcular_velocidade_relativa(self, outra_bicicleta):
        return abs(self.__velocidade_atual - outra_bicicleta.obter_velocidade_atual())
