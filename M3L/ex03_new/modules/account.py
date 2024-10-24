class Account:
    def __init__(self, bank_balance):
        self.__bank_balance = bank_balance  # bank_balance = saldo bancário
        self.__owner = None

    def debit(self, amount):
        if amount <= self.__bank_balance:
            self.__bank_balance -= amount  # amount = quantia
        else:
            return "Debit amount exceeds account balance"

    def get_bank_balance(self):
        return "The account balance is R$" + str(self.__bank_balance)

    def get_owner(self):
        return self.__owner

    def set_owner(self, owner:any):
        self.__owner = owner
