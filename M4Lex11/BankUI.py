from SavingsAccount import SavingsAccount
from AccountOperations import AccountOperations

class BankUI:
    def __init__(self, bank):
        self.bank = bank
        self.operations = AccountOperations() 

    def create_account(self):
        name = input("Digite o nome: ")
        pin = int(input("Digite o PIN: "))
        balance = float(input("Digite o saldo inicial (opcional): R$") or 0)
        if balance < 0:
            balance = 0
        account = SavingsAccount(name, pin, balance)
        self.bank.add_account(account)
        print(f"Conta para {name} criada com sucesso!")

    def delete_account(self):
        name = input("Digite o nome: ")
        pin = int(input("Digite o PIN: "))
        self.bank.delete_account(name, pin)
        print("Conta removida com sucesso!")

    def deposit(self):
        name = input("Digite o nome: ")
        pin = int(input("Digite o PIN: "))
        account = self.bank.find_account(name, pin)
        if account:
            amount = float(input("Digite o valor a ser depositado: R$"))
            self.operations.deposit(account, amount)
        else:
            print("Conta não encontrada.")

    def withdraw(self):
        name = input("Digite o nome: ")
        pin = int(input("Digite o PIN: "))
        account = self.bank.find_account(name, pin)
        if account:
            amount = float(input("Digite o valor a ser sacado: R$"))
            self.operations.withdraw(account, amount)
        else:
            print("Conta não encontrada.")

    def transfer(self):
        from_name = input("Digite o nome de quem irá transferir: ")
        from_pin = int(input("Digite o PIN: "))
        to_name = input("Digite o nome de quem irá receber: ")
        to_pin = int(input("Digite o PIN: "))
        from_account = self.bank.find_account(from_name, from_pin)
        to_account = self.bank.find_account(to_name, to_pin)
        if from_account and to_account:
            amount = float(input("Digite o valor a ser transferido: R$"))
            self.operations.transfer(from_account, to_account, amount)
        else:
            print("Conta não encontrada.")

    def list_accounts(self):
        print("Contas no banco:")
        print(self.bank)

    def get_account_info(self):
        name = input("Digite o nome: ")
        pin = int(input("Digite o PIN: "))
        account = self.bank.find_account(name, pin)
        if account:
            print(account)
        else:
            print("Conta não encontrada.")

    def check_balance(self):
        name = input("Digite o nome: ")
        pin = int(input("Digite o PIN: "))
        account = self.bank.find_account(name, pin)
        if account:
            print(f"Saldo: R${account.get_balance():.2f}")
        else:
            print("Conta não encontrada.")

    def calculate_interest(self):
        name = input("Digite o nome: ")
        pin = int(input("Digite o PIN: "))
        account = self.bank.find_account(name, pin)
        if account:
            interest = account.compute_interest()
            print(f"Juros calculados: R${interest:.2f}")
        else:
            print("Conta não encontrada.")