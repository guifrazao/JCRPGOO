class Owner:

    def __init__(self, name, age, cpf):
        self.__name = name
        self.__age = age
        self.__cpf = cpf

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def view_owner_data(self):
        print(f"\nOwner's Name: {self.get_name()}")
        print(f"Owner's Age: {self.get_age()}")
        print(f"Owner's CPF: {self.get_cpf()}")
