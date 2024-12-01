from .animal import Animal

class Reptil(Animal):
    def __init__(self, nome, cor, orgao_respiratorio):
        super().__init__(nome, cor, orgao_respiratorio)
        self._tipo = "Réptil"

    def fazerTruque(self):
        print(f"{self._nome} está tomando banho de sol")

    def imprimirInformacoes(self):
        print(f"Nome: {self._nome}\nTipo: {self._tipo}\nCor: {self._cor}\nOrgão Respiratório: {self._orgao_respiratorio.getNome()}")