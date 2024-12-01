from abc import ABC,abstractmethod

class Account(ABC):
    def __init__(self, account_number, holder_name, balance=0):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def get_holder_name(self):
        return self.__holder_name

    def __str__(self):
        return f"Account Number: {self.__account_number}, Holder: {self.__holder_name}, Balance: ${self.__balance:.2f}"

    def _add_balance(self, amount):
        self.__balance += amount

    def _subtract_balance(self, amount):
        self.__balance -= amount

    def show_balance(self):
        print(f"Balance: ${self.__balance:.2f}")
