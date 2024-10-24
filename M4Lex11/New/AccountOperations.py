class AccountOperations:
    def deposit(self, account, amount):
        account.deposit(amount)
        print(f"Depósito de R${amount} realizado com sucesso!")

    def withdraw(self, account, amount):
        account.withdraw(amount)
        print(f"Saque de R${amount} realizado com sucesso!")

    def transfer(self, from_account, to_account, amount):
        if from_account.get_balance() < amount:
            raise ValueError("Saldo insuficiente para a transferência")
        from_account.withdraw(amount)
        to_account.deposit(amount)
        print("Transferência realizada com sucesso!")
