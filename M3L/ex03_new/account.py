from owner import Owner

class Account:
    '''Represents a bank account'''

    def __init__(self, bank_balance, owner: Owner):
        '''Initializes a new Account object.'''
        self.__bank_balance = bank_balance  # bank_balance = saldo bancário
        self.__owner = owner  

    def debit(self, amount):
        '''Debits a specified amount from the account if sufficient funds are available'''
        if amount <= self.__bank_balance:
            self.__bank_balance -= amount  # amount = quantia
        else:
            return "\nDebit amount exceeds account balance"

    def get_bank_balance(self):
        '''Returns the bank balance of the account'''
        return "\nThe account balance is R$" + str(self.__bank_balance)

    def get_owner_name(self):
        '''Returns the name of the account owner'''
        return "The account owner is " + self.__owner.get_name()

    def view_account_data(self):
        '''Displays the account's data.'''
        print(self.get_bank_balance())
        print(self.get_owner_name())
