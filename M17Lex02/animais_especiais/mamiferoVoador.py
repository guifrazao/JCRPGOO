from familias_animais import Mamifero
from interfaces import IVoador

class MamiferoVoador(Mamifero, IVoador):
    def __init__(self, nome, cor, envergadura):
        super().__init__(nome, cor)
        self._envergadura = envergadura
        self._tipo = "Mamífero Voador"

    def getEnvergadura(self):
        return self.__envergadura
    
    def setEnvergadura(self, envergadura):
        self.__envergadura = envergadura

    def voar(self):
        print(f"{self._nome} está voando")