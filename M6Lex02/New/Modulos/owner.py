class Proprietario:
    def __init__(self, nome):
        self.__nome = nome
        self.__bicicleta = None

    def subir_na_bicicleta(self, bicicleta):
        bicicleta.iniciar_pedal()

    def mostrar_velocidade_relativa(self, bicicleta1, bicicleta2):
        velocidade_relativa = bicicleta1.calcular_velocidade_relativa(bicicleta2)
        print(f"A diferença de velocidade entre as bicicletas é {velocidade_relativa:.2f} km/h.")

    def se_apresentar(self):
        print(f"Olá, eu sou {self.__nome}")

    def obter_bicicleta(self):
        return self.__bicicleta

    def definir_bicicleta(self, bicicleta):
        self.__bicicleta = bicicleta
