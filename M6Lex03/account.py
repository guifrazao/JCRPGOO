from client import Client

class Account:
    def __init__(self, bank_balance, client: Client):
        if not self.__verify_bank_balance(bank_balance):
            raise Exception("INVALID BANK BALANCE!")
        self.__bank_balance = bank_balance #bank_balance = saldo bancário
        self.__client = client

    def debit(self, ammount):
        if self.__verify_debit_ammount(ammount, self.__bank_balance):
            self.__debit_msg()
            self.__set_bank_balance(self.__bank_balance - ammount) 
        else:
            self.__debit_error_msg()

    def deposit(self, ammount):
        if self.__verify_deposit_ammount(ammount):
            self.__deposit_msg()
            self.__set_bank_balance(self.__bank_balance + ammount)
        else:
            self.__deposit_error_msg()
        
    def get_bank_balance(self):
        return self.__bank_balance
    
    def __set_bank_balance(self, bank_balance):
        if self.__verify_bank_balance(bank_balance):
            self.__bank_balance = bank_balance
        else:
            self.__bank_balance_error_msg()

    def get_client(self):
        print(self.__client)
    
    @staticmethod
    def __verify_bank_balance(bank_balance):
        if bank_balance > 0:
            return True
        return False
    
    @staticmethod
    def __verify_debit_ammount(ammount, bank_balance):
        if ammount <= bank_balance:
            return True
        return False
    
    @staticmethod
    def __verify_deposit_ammount(ammount):
        if ammount > 0:
            return True
        return False
    
    @staticmethod
    def __debit_msg():
        print("Debit successfully completed!")
    
    @staticmethod
    def __deposit_msg():
        print("Deposit successfully completed!")
    
    @staticmethod
    def __debit_error_msg():
        print("Debit ammount exceeds account balance!")

    @staticmethod
    def __deposit_error_msg():
        print("Deposit amount must be positive!")
    
    @staticmethod
    def __bank_balance_error_msg():
        print("Bank balance must be positive!")
    


   