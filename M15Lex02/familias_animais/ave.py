from interfaces import IAnimal
from .animal import Animal

class Ave(Animal, IAnimal):
    def __init__(self, nome, cor, envergadura):
        super().__init__(nome, cor)
        self._envergadura = envergadura
        self._tipo = "Ave"

    def fazerTruque(self):
        print(f"{self._nome} está empoleirando")

    def imprimirInformacoes(self):
        print(f"Nome: {self._nome}\nTipo: {self._tipo}\nCor: {self._cor}\nEnvergadura: {self._envergadura}")

    def getEnvergadura(self):
        return self._envergadura
    
    def setEnvergadura(self, envergadura):
        self._envergadura = envergadura
