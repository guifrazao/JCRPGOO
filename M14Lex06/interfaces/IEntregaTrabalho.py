from abc import ABC, abstractmethod

class IEntregaTrabalho(ABC):
    @abstractmethod
    def entregarTrabalho(self):
        pass

    @abstractmethod
    def enviarParaBanca(self):
        pass