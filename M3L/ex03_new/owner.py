class Owner:
    '''Represents a person (owner)'''

    def __init__(self, name, age, cpf):
        '''Initializes a new Owner object.'''
        self.__name = name
        self.__age = age
        self.__cpf = cpf

    def get_name(self):
        '''Returns the owner's name.'''
        return self.__name

    def set_name(self, name):
        '''Change the owner's name.'''
        self.__name = name

    def get_age(self):
        '''Returns the owner's age.'''
        return self.__age

    def set_age(self, age):
        '''Change the owner's age.'''
        self.__age = age

    def get_cpf(self):
        '''Returns the owner's CPF.'''
        return self.__cpf

    def set_cpf(self, cpf):
        '''Change the owner's CPF.'''
        self.__cpf = cpf

    def view_owner_data(self):
        '''Displays the owner's data.'''
        print(f"\nOwner's Name: {self.get_name()}")
        print(f"Owner's Age: {self.get_age()}")
        print(f"Owner's CPF: {self.get_cpf()}")
