from SavingsAccount import SavingsAccount

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_conta(self, nome, pin, saldo_inicial=0):
        if (nome, pin) in self.accounts:
            print("Conta já existente.")
        else:
            nova_conta = SavingsAccount(nome, pin, saldo_inicial)  
            self.accounts[(nome, pin)] = nova_conta  
            print(f"Conta para {nome} com saldo de {saldo_inicial} criada com sucesso")

    def deletar_conta(self, nome, pin):
        if (nome, pin) in self.accounts:
            del self.accounts[(nome, pin)] 
            print("Conta removida com sucesso!")
        else:
            print("Conta não encontrada")

    def encontrar_conta(self, nome, pin):
        return self.accounts.get((nome, pin), None) 
    
    def depositar(self, nome, pin, quantia):
        conta = self.encontrar_conta(nome, pin)
        if conta:
            erro = conta.deposit(quantia)
            if erro:
                print(erro)
            else:
                print(f"Depósito de {quantia} realizado com sucesso!")
        else:
            print("Conta não encontrada.")

    def sacar(self, nome, pin, quantia):
        conta = self.encontrar_conta(nome, pin)
        if conta:
            erro = conta.withdraw(quantia)
            if erro:
                print(erro)
            else:
                print(f"Saque de {quantia} realizado com sucesso!")
        else:
            print("Conta não encontrada")

    def transferir(self, de_nome, de_pin, para_nome, para_pin, quantia):
        conta_de = self.encontrar_conta(de_nome, de_pin)
        conta_para = self.encontrar_conta(para_nome, para_pin)
        if conta_de and conta_para:
            if conta_de.getBalance() >= quantia:
                erro = conta_de.withdraw(quantia)
                if erro:
                    print(erro)
                else:
                    conta_para.deposit(quantia)
                    print("Transferência realizada com sucesso")
            else:
                print("Saldo insuficiente para a transferência")
        else:
            print("Uma das contas não foi encontrada")

    def getBalance(self, nome, pin):
        account = self.encontrar_conta(nome, pin)
        if account:
            print("Saldo:", account.getBalance())
        else:
            print("Conta não encontrada")

    def getInfoConta(self, nome, pin):
        account = self.encontrar_conta(nome, pin) 
        if account:
            print(account)
        else:
            print("Conta não encontrada")

    def calcularJuros(self, nome, pin):
        conta = self.encontrar_conta(nome, pin)
        if conta:
            juros = conta.computeInterest() 
            print("Juros:", juros)
        else:
            print("Conta não encontrada.")

    def __str__(self):
        if not self.accounts:
            return "Nenhuma conta cadastrada no banco."
        accounts_info = [f"Nome: {account.getName()} | PIN: {account.getPin()} | Saldo: {account.getBalance():.2f}" for _, account in self.accounts.items()]
        return "Banco:\n" + "\n".join(accounts_info)