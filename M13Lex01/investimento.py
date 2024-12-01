from account import Conta

class Investimento(Conta):
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

    def investir(self):
        fator_risco = 0.10  # 10% de retorno sobre o investimento
        retorno_investimento = self.obter_saldo() * fator_risco
        self._adicionar_saldo(retorno_investimento)
        print(f"Retorno de investimento de R${retorno_investimento:.2f} aplicado à conta de investimento.")
