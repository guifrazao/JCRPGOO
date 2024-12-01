from abc import ABC, abstractmethod

class IVoador(ABC):
    @abstractmethod
    def voar(self):
        pass