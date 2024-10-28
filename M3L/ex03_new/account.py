'''
M3L-ex03. Crie uma classe Account que representa uma conta bancária. A classe deve fornecer 
um método chamado debit para retirar dinheiro da conta. Assegure que a quantia de 
débito não exceda o saldo de Account. Se exceder, o saldo deve ser deixado 
inalterado e o método deve imprimir uma mensagem que indica “Quantia de débito 
excedeu o saldo da conta”. Teste a classe implementada e seus métodos. 
'''

from owner import Owner

class Account:

    def __init__(self, bank_balance, owner: Owner):
        self.__bank_balance = bank_balance  # bank_balance = saldo bancário
        self.__owner = owner  

    def debit(self, amount):
        if self.verify_amount(amount):
            self.__bank_balance -= amount  # amount = quantia
        else:
            return "\nDebit amount exceeds account balance"

    def get_bank_balance(self):
        return "\nThe account balance is R$" + str(self.__bank_balance)

    def get_owner_name(self):
        return "The account owner is " + self.__owner.get_name()

    def view_account_data(self):
        print(self.get_bank_balance())
        print(self.get_owner_name())

    @staticmethod
    def verify_amount(amount):
        if amount < 0:
            return False
        return True
