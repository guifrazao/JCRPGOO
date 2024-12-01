from abc import ABC, abstractmethod

class IEnviaParaBanca(ABC):
    @abstractmethod
    def enviarParaBanca(self):
        pass