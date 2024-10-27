from employee import Employee

class Seller(Employee):
    def __init__(self, nome, endereço, cpf, rg, telefone, sectorCode, baseSalary, tax, valueSales, commission):
        super().__init__(nome, endereço, cpf, rg, telefone, sectorCode, baseSalary, tax)
        self.__valueSales = valueSales
        self.__commission = commission

    def get_valueSales(self):
        return self.__valueSales

    def set_valueSales(self, valueSales):
        self.__valueSales = valueSales

    def get_commission(self):
        return self.__commission

    def set_commission(self, commission):
        self.__commission = commission

    # def calculateSalary(self):
    #     base_salary = super().calculateSalary()
    #     commission_amount = self.__valueSales * (self.__commission / 100)
    #     return base_salary + commission_amount
