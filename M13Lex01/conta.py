from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, numero_conta, titular, saldo=0):
        self.__numero_conta = numero_conta
        self.__titular = titular
        self.__saldo = saldo

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

    def obter_saldo(self):
        return self.__saldo

    def obter_numero_conta(self):
        return self.__numero_conta

    def obter_titular(self):
        return self.__titular

    def __str__(self):
        return f"Número da Conta: {self.__numero_conta}, Titular: {self.__titular}, Saldo: R${self.__saldo:.2f}"

    def _adicionar_saldo(self, valor):
        self.__saldo += valor

    def _subtrair_saldo(self, valor):
        self.__saldo -= valor

    def exibir_saldo(self):
        print(f"Saldo: R${self.__saldo:.2f}")
