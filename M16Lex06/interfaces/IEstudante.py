from abc import ABC, abstractmethod

class IEstudante(ABC):
    @abstractmethod
    def imprimirInformacoes(self):
        pass