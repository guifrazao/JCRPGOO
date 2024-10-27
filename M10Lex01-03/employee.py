'''
M10L-ex03. Considere, como subclasse da classe Person, a classe Employee. Considere que 
cada instância da classe Employee tem, para além dos atributos que caracterizam a 
classe Person, os atributos sectorCode (inteiro), baseSalary (vencimento base) e tax 
(porcentagem retida dos impostos). Implemente a classe Employee com métodos 
seletores e modificadores e um método calculateSalary. Altere o main para que você 
possa verificar o funcionamento dos métodos implementados na classe Employee e 
os herdados da classe Person. 
'''

from pessoa import Pessoa

class Employee(Pessoa):
    def __init__(self, nome, endereço, cpf, rg, telefone, sectorCode, baseSalary, tax):
        super().__init__(nome, endereço, cpf, rg, telefone)
        self.__sectorCode = sectorCode
        self.__baseSalary = baseSalary
        self.__tax = tax

    def get_sectorCode(self):
        return self.__sectorCode

    def set_sectorCode(self, sectorCode):
        self.__sectorCode = sectorCode

    def get_baseSalary(self): # salário bruto
        return self.__baseSalary

    def set_baseSalary(self, baseSalary):
        self.__baseSalary = baseSalary

    def get_tax(self):
        return self.__tax

    def set_tax(self, tax):
        self.__tax = tax

    def calculateSalary(self): # salário líquido
        return self.__baseSalary * (1 - self.__tax / 100)
