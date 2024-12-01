from conta import Conta

class Corrente(Conta):
    def depositar(self, valor):
        if valor > 0:
            self._adicionar_saldo(valor)
        else:
            print("O depósito deve ser um valor positivo.")

    def sacar(self, valor):
        if valor > 0 and self.obter_saldo() >= valor:
            self._subtrair_saldo(valor)
        else:
            print("Saldo insuficiente ou valor inválido.")
