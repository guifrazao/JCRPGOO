'''
M3L-ex08. Crie uma classe chamada Employee que inclui três variáveis de instância: um nome 
(string), um sobrenome (string) e um salário mensal (float). Sua classe deve ter um 
construtor que inicializa as três variáveis. Forneça um método get e set para cada 
variável. Se o salário mensal fornecido pelo usuário não for positivo, configure-o 
como 0.0. Teste a classe implementada e seus métodos. Crie dois objetos Employee e 
exiba o salário anual de cada objeto. Depois, dê 10% de aumento para cada 
empregado e exiba novamente os salários. 
'''

class Employee:
    def __init__(self, name, surname, monthly_salary):
        if not self.__verifyName(name):
            raise Exception("Invalid name")
        if not self.__verifyName(surname):
            raise Exception("Invalid surname")

        self.__name = name
        self.__surname = surname
        self.__monthly_salary = monthly_salary if self.__verifySalary(monthly_salary) else 0

    def __repr__(self):
        return f"Full name: {self.__name} {self.__surname}\nSalary: {self.__monthly_salary}"
        
    """A variável 'aumento' é o aumento em porcentagem, não em valor decimal"""
    def raiseSalary(self, employee_type):
        if employee_type == 1:
            self.__monthly_salary += self.__monthly_salary * 0.10
        elif employee_type == 2:
            self.__monthly_salary += self.__monthly_salary * 0.20
        else:
            print("Employee type does not exist")

    def getAnualSalary(self):
        return self.__monthly_salary * 12
      
    def getName(self):
        return self.__name
    
    def setName(self, name):
        if not self.__verifyName(name):
            self.__invalidDataMsg("name")
        else:
            self.__name = name

    def getSurname(self):
        return self.__surname
    
    def setSurname(self, surname):
        if not self.__verifyName(surname):
            self.__invalidDataMsg("surname")
        else:
            self.__surname = surname

    def getSalary(self):
        return self.__monthly_salary
    
    def setSalary(self, monthly_salary):
        if not self.__verifySalary(monthly_salary):
            self.__invalidDataMsg("salary")
        else:
            self.__monthly_salary = monthly_salary

    @staticmethod
    def __verifyName(name):
        return len(name) >= 3 and name.isalpha()
    
    @staticmethod
    def __verifySalary(salary):
        return salary >= 0
    
    @staticmethod
    def __invalidDataMsg(data):
        print(f"Invalid {data}")
