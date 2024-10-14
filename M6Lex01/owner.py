class Owner:
    def __init__(self, name, age, cpf):
        if not self.verifyName(name):
            raise Exception("INVALID NAME")
        if not self.verifyAge(age):
            raise Exception("INVALID AGE")
        if not self.verifyCPF(cpf):
            raise Exception("INVALID CPF")
        
        self.__name = name
        self.__age = age
        self.__cpf = cpf
    
    def __str__(self):
        return f"\nName = {self.__name}\nAge = {self.__age}\nCPF = {self.__cpf}"

    def getName(self):
        return self.__name
    
    def setName(self, name):
        if not self.verifyName(name):
            self.__invalidDataMessage("name")
        else:
            self.__name = name

    def getAge(self):
        return self.__age
    
    def setAge(self, age):
        if not self.verifyAge(age):
            self.__invalidDataMessage("age")
        else:
            self.__age = age

    def getCPF(self):
        return self.__cpf
    
    def setCPF(self, cpf):
        if not self.verifyCPF(cpf):
            self.__invalidDataMessage("CPF")
        else:
            self.__cpf = cpf

    @staticmethod
    def verifyCPF(cpf):
        return len(cpf) == 11 and cpf.isnumeric()
    
    @staticmethod
    def verifyAge(age):
        return age >= 16
    
    @staticmethod
    def verifyName(name):
        return len(name) >= 3

    @staticmethod
    def __invalidDataMessage(err):
        print(f"Error: Invalid {err}")
