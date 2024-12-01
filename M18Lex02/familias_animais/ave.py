from .animal import Animal
from orgaoRespiratorio import OrgaoRespiratorio

class Ave(Animal):
    def __init__(self, nome, cor, envergadura, orgao_respiratorio):
        super().__init__(nome, cor, orgao_respiratorio)
        self._tipo = "Ave"
        self._envergadura = envergadura

    def getEnvergadura(self):
        return self.__envergadura
    
    def setEnvergadura(self, envergadura):
        self.__envergadura = envergadura

    def fazerTruque(self):
        print(f"{self._nome} está empoleirando")

    def imprimirInformacoes(self):
        print(f"Nome: {self._nome}\nTipo: {self._tipo}\nEnvergadura: {self._envergadura}\nCor: {self._cor}\nOrgão Respiratório: {self._orgao_respiratorio.getNome()}")


    