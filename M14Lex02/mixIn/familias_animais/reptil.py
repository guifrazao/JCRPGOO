from .animal import Animal

class Reptil(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
        self._tipo = "Réptil"

    def fazerTruque(self):
        print(f"{self._nome} está tomando banho de sol")

    def imprimirInformacoes(self):
        print(f"Nome: {self._nome}\nTipo: {self._tipo}\nCor: {self._cor}")