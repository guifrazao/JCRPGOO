'''
M10L-ex02. Considere, como subclasse da classe Person, a classe Supplier, para representar um 
fornecedor. Considere que cada instância da classe Supplier tem, para além dos
atributos que caracterizam a classe Person, os atributos valueCredit (correspondente 
ao crédito máximo atribuído ao fornecedor) e valueDebt (montante da dívida para com 
o fornecedor). Implemente na classe Supplier, para além dos usuais métodos 
seletores e modificadores, um método getBalance() que devolve a diferença entre os 
valores dos atributos valueCredit e valueDebt. Depois de implementada a classe 
Supplier, altere o main para que você possa verificar o funcionamento dos métodos 
implementados na classe Supplier e os herdados da classe Person. 
'''

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

        
