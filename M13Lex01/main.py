from corrente import Corrente
from poupanca import Poupanca
from investimento import Investimento
from cliente import Cliente

def main():
    # Criando clientes
    cliente1 = Cliente("Alice", "123.456.789-00")
    cliente2 = Cliente("Bob", "987.654.321-00")

    # Criando contas e associando titularidade automaticamente
    conta_corrente = Corrente("123", cliente1.get_nome(), saldo=500)
    conta_poupanca = Poupanca("456", cliente2.get_nome(), saldo=1000)
    conta_investimento = Investimento("789", cliente2.get_nome(), saldo=1500)

    # Adicionando contas aos clientes
    cliente1.adicionar_conta(conta_corrente)  # Alice tem uma conta corrente
    cliente2.adicionar_conta(conta_poupanca)  # Bob tem uma conta poupança
    cliente2.adicionar_conta(conta_investimento)  # Bob também tem uma conta investimento

    # Operações nas contas
    print("Operações na Conta Corrente:")
    conta_corrente.depositar(200)
    conta_corrente.exibir_saldo()
    conta_corrente.sacar(300)
    conta_corrente.exibir_saldo()

    print("\nOperações na Conta Poupança:")
    conta_poupanca.aplicar_juros()
    conta_poupanca.exibir_saldo()
    conta_poupanca.depositar(500)
    conta_poupanca.exibir_saldo()
    conta_poupanca.sacar(200)
    conta_poupanca.exibir_saldo()

    print("\nOperações na Conta de Investimento:")
    conta_investimento.investir()
    conta_investimento.exibir_saldo()
    conta_investimento.depositar(500)
    conta_investimento.exibir_saldo()
    conta_investimento.sacar(700)
    conta_investimento.exibir_saldo()

    # Exibindo informações dos clientes e suas contas
    print("\nDados do Cliente 1:")
    cliente1.mostrar_dados_cliente()

    print("\nDados do Cliente 2:")
    cliente2.mostrar_dados_cliente()

main()

