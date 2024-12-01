from interfaces import IAnimal
from .animal import Animal

class Anfibio(Animal, IAnimal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
        self._tipo = "Anfíbio"

    def fazerTruque(self):
        print(f"{self._nome} está fazendo o que quer que anfíbios façam")

    def imprimirInformacoes(self):
        print(f"Nome: {self._nome}\nTipo: {self._tipo}\nCor: {self._cor}")
