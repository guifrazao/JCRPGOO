from validator import Validator

class Owner:
    def __init__(self, name, cpf, tel):
        self.__name = Validator.verify_name(name)
        self.__cpf = Validator.verify_cpf(cpf)
        self.__tel = Validator.verify_tel(tel)

    def __str__(self):
        return f"\nName: {self.__name}\nCPF: {self.__cpf}\nTel: {self.__tel}"

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = Validator.verify_name(name)

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = Validator.verify_cpf(cpf)

    def get_tel(self):
        return self.__tel

    def set_tel(self, tel):
        self.__tel = Validator.verify_tel(tel)
