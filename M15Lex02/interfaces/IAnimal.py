from abc import ABC, abstractmethod

class IAnimal(ABC):
    @abstractmethod
    def fazerTruque(self):
        pass

    @abstractmethod
    def imprimirInformacoes(self):
        pass
