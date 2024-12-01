from account import Account

class Corrente(Account):
    def deposit(self, amount):
        if amount > 0:
            self._add_balance(amount)
        else:
            print("Depósito deve ser um valor positivo.")

    def withdraw(self, amount):
        if amount > 0 and self.get_balance() >= amount:
            self._subtract_balance(amount)
        else:
            print("Saldo insuficiente ou valor inválido.")

