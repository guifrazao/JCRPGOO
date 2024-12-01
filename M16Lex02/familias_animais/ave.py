from interfaces import IAnimal

class Ave(IAnimal):
    def __init__(self, nome, cor, envergadura):
        self._nome = nome
        self._tipo = "Ave"
        self._cor = cor
        self._envergadura = envergadura

    def fazerTruque(self):
        print(f"{self._nome} está empoleirando")

    def imprimirInformacoes(self):
        print(f"Nome: {self._nome}\nTipo: {self._tipo}\nCor: {self._cor}\nEnvergadura: {self._envergadura}")

    def getEnvergadura(self):
        return self._envergadura
    
    def setEnvergadura(self, envergadura):
        self._envergadura = envergadura
