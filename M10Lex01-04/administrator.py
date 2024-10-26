from employee import Employee

class Administrator(Employee):
    def __init__(self, nome, endereço, cpf, rg, telefone, sectorCode, baseSalary, tax, subsistenceAllowance):
        super().__init__(nome, endereço, cpf, rg, telefone, sectorCode, baseSalary, tax)
        self.__subsistenceAllowance = subsistenceAllowance

    def get_subsistenceAllowance(self):
        return self.__subsistenceAllowance

    def set_subsistenceAllowance(self, subsistenceAllowance):
        self.__subsistenceAllowance = subsistenceAllowance

    def calculateSalary(self):
        base_salary = super().calculateSalary()
        return base_salary + self.__subsistenceAllowance
