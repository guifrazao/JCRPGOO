# factory_worker.py
from employee import Employee

class FactoryWorker(Employee):
    def __init__(self, nome, endereço, cpf, rg, telefone, sectorCode, baseSalary, tax, valueProduction, commission):
        super().__init__(nome, endereço, cpf, rg, telefone, sectorCode, baseSalary, tax)
        self.__valueProduction = valueProduction    
        self.__commission = commission

    def get_valueProduction(self):
        return self.__valueProduction

    def set_valueProduction(self, valueProduction):
        self.__valueProduction = valueProduction

    def get_commission(self):
        return self.__commission

    def set_commission(self, commission):
        self.__commission = commission

    # def calculateSalary(self):
    #     base_salary = super().calculateSalary()
    #     commission_amount = self.__valueProduction * (self.__commission / 100)
    #     return base_salary + commission_amount
