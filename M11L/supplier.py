from pessoa import Pessoa

class Supplier(Pessoa):
    def __init__(self, nome, endereço, cpf, rg, telefone, valueCredit, valueDebt):
        super().__init__(nome, endereço, cpf, rg, telefone)
        self.__valueCredit = valueCredit
        self.__valueDebt = valueDebt

    def get_valueCredit(self):
        return self.__valueCredit

    def set_valueCredit(self, valueCredit):
        self.__valueCredit = valueCredit

    def get_valueDebt(self):
        return self.__valueDebt

    def set_valueDebt(self, valueDebt):
        self.__valueDebt = valueDebt

    def getBalance(self):
        return self.__valueCredit - self.__valueDebt

        