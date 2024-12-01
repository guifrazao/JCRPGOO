from familias_animais import Mamifero
from mix_ins import VoadorMixIn

class MamiferoVoador(VoadorMixIn, Mamifero):
    def __init__(self, nome, cor, envergadura):
        super().__init__(nome, cor)
        self._envergadura = envergadura
        self._tipo = "Mamífero Voador"

    def getEnvergadura(self):
        return self.__envergadura
    
    def setEnvergadura(self, envergadura):
        self.__envergadura = envergadura