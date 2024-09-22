class SavingsAccount:
    RATE = 0.02

    def __init__(self, name, pin, balance=0.0):
        self.__name = name
        self.__pin = pin
        self.__balance = balance

    def get_name(self):
        return self.__name

    def get_pin(self):
        return self.__pin

    def get_balance(self):
        return self.__balance

    def set_name(self, name):
        self.__name = name

    def set_pin(self, pin):
        self.__pin = pin

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            raise ValueError("O saldo deve ser >= 0")

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("O valor a depositar deve ser >= 0")
        self.__balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("O valor a sacar deve ser >= 0")
        if self.__balance < amount:
            raise ValueError("Saldo insuficiente")
        self.__balance -= amount

    def compute_interest(self):
        interest = self.__balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest

    def __str__(self):
        return f"Nome: {self.__name}\nPIN: {self.__pin}\nSaldo: R${self.__balance:.2f}"

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        if (account.get_name(), account.get_pin()) in self.accounts:
            raise ValueError("Conta já existente.")
        self.accounts[(account.get_name(), account.get_pin())] = account

    def delete_account(self, name, pin):
        if (name, pin) in self.accounts:
            del self.accounts[(name, pin)]
        else:
            raise ValueError("Conta não encontrada.")

    def find_account(self, name, pin):
        return self.accounts.get((name, pin))

    def __str__(self):
        if not self.accounts:
            return "Nenhuma conta cadastrada."
        return "\n".join(f"{account}\n{'-'*30}" for account in self.accounts.values())

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
