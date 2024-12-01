from abc import ABC, abstractmethod
from orgaoRespiratorio import OrgaoRespiratorio

class Animal(ABC):
    def __init__(self, nome, cor, orgao_respiratorio):
        self._nome = nome
        self._tipo = None
        self._cor = cor
        self._orgao_respiratorio = OrgaoRespiratorio(nome=orgao_respiratorio)

    def getNome(self):
        return self.__nome
    
    def setNome(self, nome):
        self.__nome = nome

    def getTipo(self):
        return self.__tipo
    
    def setTipo(self, tipo):
        self.__tipo = tipo  

    def getCor(self):
        return self.__cor
    
    def setCor(self, cor):
        self.__cor = cor
    
    @abstractmethod
    def fazerTruque(self):
        pass

    @abstractmethod
    def imprimirInformacoes(self):
        pass

    