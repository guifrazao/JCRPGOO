class Contact:
    def __init__(self, name, phone_number):
        if not self.__verify_phone_number(phone_number):
            raise Exception("INVALID PHONE NUMBER")
        
        self.__phone_number = phone_number
        self.__name = name

    def __str__(self):
        return f"{self.__name:<10}|{self.__phone_number:<15}"
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_phone_number(self):
        return self.__phone_number
    
    def set_phone_number(self, phone_number):
        if self.__verify_phone_number(phone_number):
            self.__phone_number = phone_number
        else:
            self.__invalid_data_msg("phone number")

    @staticmethod
    def __verify_phone_number(phone_number):
        return len(phone_number) == 10 and phone_number.isnumeric()
    
    @staticmethod
    def __invalid_data_msg(data):
        print(f"Invalid {data}")