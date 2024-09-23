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
