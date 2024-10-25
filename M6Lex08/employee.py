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