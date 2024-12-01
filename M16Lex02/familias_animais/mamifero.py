from interfaces import IAnimal

class Mamifero(IAnimal):
    def __init__(self, nome, cor):
        self._nome = nome
        self._tipo = "Mamífero"
        self._cor = cor

    def fazerTruque(self):
        print(f"{self._nome} está fazendo algo")

    def imprimirInformacoes(self):
        print(f"Nome: {self._nome}\nTipo: {self._tipo}\nCor: {self._cor}")
