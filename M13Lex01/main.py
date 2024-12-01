from corrente import Corrente
from poupanca import Poupanca
from investimento import Investimento
from banco import Banco

def main():
    banco = Banco()  # Gerenciador de contas

    # Criando contas
    conta_corrente = Corrente("123", "Alice", saldo=500)
    conta_poupanca = Poupanca("456", "Bob", saldo=1000)
    conta_investimento = Investimento("789", "Carol", saldo=1500)

    # Adicionando contas ao banco
    banco.adicionar_conta(conta_corrente)
    banco.adicionar_conta(conta_poupanca)
    banco.adicionar_conta(conta_investimento)

    # Operações com Conta Corrente
    print("\n[Conta Corrente - Alice]")
    banco.depositar(conta_corrente, 200)
    banco.sacar(conta_corrente, 300)
    banco.exibir_saldo(conta_corrente)

    # Operações com Conta Poupança
    print("\n[Conta Poupança - Bob]")
    conta_poupanca.aplicar_juros()
    banco.depositar(conta_poupanca, 500)
    banco.sacar(conta_poupanca, 200)
    banco.exibir_saldo(conta_poupanca)

    # Operações com Conta Investimento
    print("\n[Conta Investimento - Carol]")
    conta_investimento.investir()
    banco.depositar(conta_investimento, 500)
    banco.sacar(conta_investimento, 700)
    banco.exibir_saldo(conta_investimento)

    # Exibindo todas as contas
    print("\n[Resumo de Contas no Banco]")
    banco.exibir_todas_contas()

main()
