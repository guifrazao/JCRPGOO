class SavingsAccount:
    RATE = 0.02

    def __init__(self, name, pin, balance=0.0):
        self.__name = name
        self.__pin = pin
        self.__balance = balance

    def get_name(self):
        return self.__name

    def get_pin(self):
        return self.__pin

    def get_balance(self):
        return self.__balance

    def set_name(self, name):
        self.__name = name

    def set_pin(self, pin):
        self.__pin = pin

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            raise ValueError("O saldo deve ser >= 0")

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("O valor a depositar deve ser >= 0")
        self.__balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("O valor a sacar deve ser >= 0")
        if self.__balance < amount:
            raise ValueError("Saldo insuficiente")
        self.__balance -= amount

    def compute_interest(self):
        interest = self.__balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest

    def __str__(self):
        return f"Nome: {self.__name}\nPIN: {self.__pin}\nSaldo: R${self.__balance:.2f}"

