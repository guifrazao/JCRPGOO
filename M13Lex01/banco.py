class Banco:
    def __init__(self):
        self.contas = []  # Armazena objetos do tipo Conta (abstração)

    def adicionar_conta(self, conta):
        """Adiciona uma conta ao banco. A conta deve ser uma subclasse de Conta."""
        self.contas.append(conta)

    def depositar(self, conta, valor):
        """Deposita um valor em uma conta."""
        conta.depositar(valor)
        print(f"Depósito de R${valor:.2f} realizado na conta {conta.obter_numero_conta()}.")

    def sacar(self, conta, valor):
        """Saca um valor de uma conta."""
        conta.sacar(valor)
        print(f"Saque de R${valor:.2f} realizado na conta {conta.obter_numero_conta()}.")

    def exibir_saldo(self, conta):
        """Exibe o saldo de uma conta."""
        conta.exibir_saldo()

    def exibir_todas_contas(self):
        """Exibe informações de todas as contas registradas no banco."""
        print("\n--- Todas as Contas ---")
        for conta in self.contas:
            print(conta)
        print("------------------------")
