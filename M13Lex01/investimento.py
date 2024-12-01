from account import Account

class Investimento(Account):
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

    def invest(self):
        risk_factor = 0.10  # 10% de retorno sobre o investimento
        investment_return = self.get_balance() * risk_factor
        self._add_balance(investment_return)
        print(f"Retorno de investimento de ${investment_return:.2f} aplicado à conta investimento.")
