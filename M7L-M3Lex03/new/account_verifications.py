# Conta corrente (permite saldo negativo até -500)
class CheckingAccountVerification:
    def verify(self, bank_balance, amount):
        return (bank_balance - amount) >= -500

# Conta poupança (não permite saldo negativo)
class SavingsAccountVerification:
    def verify(self, bank_balance, amount):
        return amount <= bank_balance