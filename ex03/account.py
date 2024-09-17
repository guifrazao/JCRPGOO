'''
Crie uma classe Account que representa uma conta bancária. A classe deve fornecer 
um método chamado debit para retirar dinheiro da conta. Assegure que a quantia de 
débito não exceda o saldo de Account. Se exceder, o saldo deve ser deixado 
inalterado e o método deve imprimir uma mensagem que indica “Quantia de débito 
excedeu o saldo da conta”. Teste a classe implementada e seus métodos.
'''

'''File:account.py
Features for managing a bank account'''
class Account:
    '''Represents a bank account'''
    def __init__(self, bank_balance):
        '''Initializes a new Account object.'''
        self.__bank_balance = bank_balance #bank_balance = saldo bancário

    def debit(self, ammount):
        ''' Debits a specified amount from the account if sufficient funds are available'''
        if ammount <= self.__bank_balance:
            self.__bank_balance -= ammount #ammount = quantia
        else:
            return "Debit ammount exceeds account balance"
        
    def get_bank_balance(self):
        '''Returns the bank balance of the account'''
        return "The account balance is R$" + str(self.__bank_balance)
    '''
    def set_bank_balance(self, bank_balance):
        #Change the bank balance of the account
        if bank_balance >= 0:
            self.__bank_balance = bank_balance
        else:
            return "Bank balance cannot be negative"
    '''

