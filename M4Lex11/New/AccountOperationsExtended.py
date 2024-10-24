from AccountOperations import AccountOperations

class AccountOperationsExtended:
    def __init__(self):
        self.operations = AccountOperations()

    def deposit(self, account, amount):
        self.operations.deposit(account, amount)

    def withdraw(self, account, amount):
        self.operations.withdraw(account, amount)

    def transfer(self, from_account, to_account, amount):
        self.operations.transfer(from_account, to_account, amount)

    def pay_bill(self, account, amount):
        if account.get_balance() < amount:
            raise ValueError("Saldo insuficiente para pagar a conta")
        account.withdraw(amount)
        print(f"Conta de R${amount} paga com sucesso!")
