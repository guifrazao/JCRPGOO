from .animal import Animal

class Ave(Animal):
    def __init__(self, nome, cor, envergadura):
        super().__init__(nome, cor)
        self._tipo = "Ave"
        self._envergadura = envergadura

    def getEnvergadura(self):
        return self.__envergadura
    
    def setEnvergadura(self, envergadura):
        self.__envergadura = envergadura

    def fazerTruque(self):
        print(f"{self._nome} está empoleirando")

    def imprimirInformacoes(self):
        print(f"Nome: {self._nome}\nTipo: {self._tipo}\nEnvergadura: {self._envergadura}\nCor: {self._cor}")


    