from interfaces import IAnimal

class Reptil(IAnimal):
    def __init__(self, nome, cor):
        self._nome = nome
        self._tipo = "Réptil"
        self._cor = cor

    def fazerTruque(self):
        print(f"{self._nome} está tomando banho de sol")

    def imprimirInformacoes(self):
        print(f"Nome: {self._nome}\nTipo: {self._tipo}\nCor: {self._cor}")
