from interfaces import IAnimal

class Anfibio(IAnimal):
    def __init__(self, nome, cor):
        self._nome = nome
        self._tipo = "Anfíbio"
        self._cor = cor

    def fazerTruque(self):
        print(f"{self._nome} está fazendo o que quer que anfíbios façam")

    def imprimirInformacoes(self):
        print(f"Nome: {self._nome}\nTipo: {self._tipo}\nCor: {self._cor}")
