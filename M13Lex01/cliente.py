from account import Conta
from corrente import Corrente
from poupanca import Poupanca
from investimento import Investimento

class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome  # Atributo privado
        self.__cpf = cpf
        self.__contas = []

    def adicionar_conta(self, conta):
        self.__contas.append(conta)

    def get_nome(self):  # Método getter para o nome
        return self.__nome

    def get_cpf(self):  # Método getter para o CPF
        return self.__cpf

    def mostrar_dados_cliente(self):
        print(f"Nome: {self.__nome}")
        print(f"CPF: {self.__cpf}")
        for conta in self.__contas:
            print(conta)
