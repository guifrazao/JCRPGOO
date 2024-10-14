class Client:
    def __init__(self, name, cpf, phone_number, cep):
        if not self.__verify_name(name):
            raise Exception("INVALID NAME!")
        
        if not self.__verify_cpf(cpf):
            raise Exception("INVALID CPF!")
        
        if not self.__verify_phone_number(phone_number):
            raise Exception("INVALID PHONE NUMBER!")
        
        if not self.__verify_cep(cep):
            raise Exception("INVALID CEP!")
        
        self.__name = name
        self.__cpf = cpf
        self.__phone_number = phone_number
        self.__cep = cep
    
    def __str__(self):
        return f"\nName = {self.__name}\nCPF = {self.__cpf}\nPhone number = {self.__phone_number}\nCEP = {self.__cep[0:5]}-{self.__cep[5:]}"
    
    def get_name(self):
        return self.__name

    def set_name(self, name):
        if self.__verify_name:
            self.__name = name
        else:
            self.__invalid_data_msg("name")
        
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, cpf):
        if self.__verify_cpf(cpf):
            self.__cpf = cpf
        else:
            self.__invalid_data_msg("cpf")
    
    def get_phone_number(self):
        return self.__phone_number
    
    def set_phone_number(self, phone_number):
        if self.__verify_phone_number(phone_number):
            self.__phone_number = phone_number
        else:
            self.__invalid_data_msg("phone number")

    def get_cep(self):
        return self.__cep
    
    def set_cep(self, cep):
        if self.__verify_cep(cep):
            self.__cep = cep
        else:
            self.__invalid_data_msg("CEP")

    @staticmethod
    def __verify_name(name):
        return len(name) >= 3
    
    @staticmethod
    def __verify_cpf(cpf):
        return len(cpf) == 11 and cpf.isnumeric()
    
    @staticmethod
    def __verify_phone_number(phone_number):
        return (len(phone_number) == 10 or len(phone_number) == 11) and phone_number.isnumeric()
    
    @staticmethod
    def __verify_cep(cep):
        return len(cep) == 8 and cep.isnumeric()
    
    @staticmethod
    def __invalid_data_msg(data):
        print(f"Invalid {data}")
