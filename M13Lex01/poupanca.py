from account import Account

class Poupanca(Account):
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

    def apply_interest(self):
        interest_rate = 0.05  # 5% de juros
        interest = self.get_balance() * interest_rate
        self._add_balance(interest)
        print(f"Juros de ${interest:.2f} aplicados à conta poupança.")
