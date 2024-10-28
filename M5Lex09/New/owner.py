from validator import Validator_Owner
from validator import invalidDataMessage

class Owner:
    
    def __init__(self,name,cpf,tel):
        if not Validator_Owner.verifyName(name):
            raise Exception("Name")
        if not Validator_Owner.verifyCPF(cpf):
            raise Exception("CPF")
        if not Validator_Owner.verifyTel(tel):
            raise Exception("Tel")

        self.__name = name
        self.__cpf = cpf
        self.__tel = tel

    def __str__(self):
        return f"\nName: {self.__name}\nCPF: {self.__cpf}\nTel: {self.__tel}"

    def getName(self):
        return self.__name
    
    def setName(self,name):
        if not Validator_Owner.verifyName(name):
            invalidDataMessage("name")
        else:
            self.__name = name

    def getCPF(self):
        return self.__cpf
    
    def setCPF(self,cpf):
        if not Validator_Owner.verifyCPF(cpf):
            invalidDataMessage("CPF")
        else:
            self.__cpf = cpf

    def getTel(self):
        return self.__tel
    
    def setTel(self,tel):
        if not Validator_Owner.verifyTel(tel):
            invalidDataMessage("Tel")
        else:
            self.__tel = tel
