from .animal import Animal

class Anfibio(Animal):
    def __init__(self, nome, cor, orgao_respiratorio):
        super().__init__(nome, cor, orgao_respiratorio)
        self._tipo = "Anfíbio"

    def fazerTruque(self):
        print(f"{self._nome} está fazendo o que quer que anfíbios façam")

    def imprimirInformacoes(self):
        print(f"Nome: {self._nome}\nTipo: {self._tipo}\nCor: {self._cor}\nOrgão Respiratório: {self._orgao_respiratorio.getNome()}")