from account import Conta

class Poupanca(Conta):
    def depositar(self, valor):
        if valor > 0:
            self._adicionar_saldo(valor)
        else:
            print("Depósito deve ser um valor positivo.")

    def sacar(self, valor):
        if valor > 0 and self.obter_saldo() >= valor:
            self._subtrair_saldo(valor)
        else:
            print("Saldo insuficiente ou valor inválido.")

    def aplicar_juros(self):
        taxa_juros = 0.05  # 5% de juros
        juros = self.obter_saldo() * taxa_juros
        self._adicionar_saldo(juros)
        print(f"Juros de R${juros:.2f} aplicados à conta poupança.")
