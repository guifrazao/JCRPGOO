from employee import Employee
class Company:
    def __init__(self, name, company_type, cnpj):
        if not self.__verifyName(name):
            raise Exception("Invalid name")
        if not self.__verifyCNPJ(cnpj):
            raise Exception("Invalid CNPJ")
        self.__name = name
        self.__type = company_type
        self.__cnpj = cnpj
        self.__employees_list = []
        
    def __str__(self):
        return f"Name: {self.__name}\nType: {self.__type}\nCNPJ: {self.__cnpj}"

    def addEmployee(self, employee: Employee):
        self.__employees_list.append(employee)
    
    def removeEmployee(self, employee):
        if not self.__employeeExists(employee):
            self.__noSuchEmployeeMsg()
        else:
            self.__employees_list.remove(employee)
            self.__successfullyRemovedMsg()

    def searchEmployeesByName(self, name):
        for employee in self.__employees_list:
            if employee.getName() == name:
                return employee
        return None

    def getName(self):
        return self.__name
        
    def setName(self, name):
        if not self.__verifyName(name):
            self.__invalidDataMsg("name")
        else:
            self.__name = name

    def getType(self):
        return self.__type
        
    def setType(self, company_type):
        self.__type = company_type

    def getCNPJ(self):
        return self.__cnpj
    
    def setCNPJ(self, cnpj):
        if not self.__verifyCNPJ(cnpj):
            self.__invalidDataMsg("CNPJ")
        else:
            self.__cnpj = cnpj

    def getEmployees(self):
        employees = ""
        for employee in self.__employees_list:
            employees += f"{employee}\n"
        return employees
    
    def __employeeExists(self, employee):
        if employee in self.__employees_list:
            return True
        return False
    
    @staticmethod
    def verifyType(company_type):
        return company_type > 0 and company_type <= 10

    @staticmethod
    def __verifyName(name):
        return len(name) >= 0
     
    @staticmethod
    def __verifyCNPJ(cnpj):
        return len(cnpj) == 14 and cnpj[8:12] == "0001" and cnpj.isnumeric()
    
    @staticmethod
    def __noSuchEmployeeMsg():
        print("No such employee")

    @staticmethod
    def __successfullyRemovedMsg():
        print("Employee successfully removed")
    
    @staticmethod
    def __invalidDataMsg(data):
        print(f"Invalid {data}")