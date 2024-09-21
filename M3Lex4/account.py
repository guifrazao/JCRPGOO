'''Crie uma versão nova da classe Account com um método chamado displayAccount,
que exiba o name e o balance de uma conta passada como parâmetro. Altere também
o main para, ao invés de imprimir diretamente o name e o balance da conta, use o
método displayAccount, passando a conta como parâmetro.'''

class Account:
    '''Represents a bank account'''
    def __init__(self, owner, bank_balance):
        '''Initializes a new Account object.'''
        self.__owner = owner
        self.__bank_balance = bank_balance #bank_balance = saldo bancário

    def debit(self, ammount):
        ''' Debits a specified amount from the account if sufficient funds are available'''
        if ammount <= self.__bank_balance:
            self.__bank_balance -= ammount #ammount = quantia
            return f"A debit of {ammount} was made"
        else:
            return "Debit ammount exceeds account balance"
        
    def get_bank_balance(self):
        '''Returns the bank balance of the account'''
        return "The account balance is R$" + str(self.__bank_balance)
    
    def displayAccount(self, account):
        
        return (f"Account Owner: {account.__owner} \nAccount Balance: R$ {account.__bank_balance:.2f}")


