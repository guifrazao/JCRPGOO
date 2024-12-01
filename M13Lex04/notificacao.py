from abc import ABC, abstractmethod

class ServicoNotificacao(ABC):
    @abstractmethod
    def notificar(self, nome_funcionario, mensagem):
        pass
