# owner.py

from validator import Validator_Owner
from validator import invalidDataMessage

class Owner:
    def __init__(self, name, cpf):
        if not Validator_Owner.verifyName(name):
            raise ValueError("Nome inválido")
        if not Validator_Owner.verifyCPF(cpf):
            raise ValueError("CPF inválido")

        self.__name = name
        self.__cpf = cpf

    def __str__(self):
        # Formatação do CPF para o formato ###.###.###-##
        cpf_formatado = f"{self.__cpf[:3]}.{self.__cpf[3:6]}.{self.__cpf[6:9]}-{self.__cpf[9:]}"
        return f"\nNome: {self.__name}\nCPF: {cpf_formatado}"

    def getName(self):
        return self.__name

    def setName(self, name):
        if not Validator_Owner.verifyName(name):
            invalidDataMessage("Nome")
        else:
            self.__name = name

    def getCPF(self):
        # Retorna o CPF já formatado
        return f"{self.__cpf[:3]}.{self.__cpf[3:6]}.{self.__cpf[6:9]}-{self.__cpf[9:]}"

    def setCPF(self, cpf):
        if not Validator_Owner.verifyCPF(cpf):
            invalidDataMessage("CPF")
        else:
            self.__cpf = cpf

