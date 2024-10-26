from validator import Validator_Owner

class Owner:
    def __init__(self, name, cpf, tel):
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
