'''
M3L-ex03. Crie uma classe Account que representa uma conta bancária. A classe deve fornecer 
um método chamado debit para retirar dinheiro da conta. Assegure que a quantia de 
débito não exceda o saldo de Account. Se exceder, o saldo deve ser deixado 
inalterado e o método deve imprimir uma mensagem que indica “Quantia de débito 
excedeu o saldo da conta”. Teste a classe implementada e seus métodos. 
'''

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
