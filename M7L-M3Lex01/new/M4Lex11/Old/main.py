"""
Implemente a classe Bank considerando os métodos listados abaixo e acrescentando
métodos que considerar conveniente.
"""

from Bank import Bank

def main():
    banco = Bank() 

    while True:
        try:
            print("=-"*30)
            print("\nMenu:")
            print("1. Criar nova conta")
            print("2. Deletar conta")
            print("3. Depositar")
            print("4. Sacar")
            print("5. Ver todas as contas")
            print("6. Transferir")
            print("7. Ver informações da conta")
            print("8. Consultar saldo")
            print("9. Calcular juros")
            print("0. Sair")
            print("=-"*30)
            opcao = int(input("Escolha uma opção: "))
            print("=-"*30)

            if opcao == 1:
                nome = input("Digite o nome: ")
                pin = int(input("Digite o PIN: "))
                saldo = float(input("Digite o saldo inicial (opcional): R$") or 0)
                banco.add_conta(nome, pin, saldo)

            elif opcao == 2:
                nome = input("Digite o nome: ")
                pin = int(input("Digite o PIN: "))
                banco.deletar_conta(nome, pin)

            elif opcao == 3:
                nome = input("Digite o nome: ")
                pin = int(input("Digite o PIN: "))
                quantia = float(input("Digite o valor a ser depositado: R$"))
                banco.depositar(nome, pin, quantia)

            elif opcao == 4:
                nome = input("Digite o nome: ")
                pin = int(input("Digite o PIN: "))
                quantia = float(input("Digite o valor a ser sacado: R$"))
                banco.sacar(nome, pin, quantia)

            elif opcao == 5:
                print(banco)

            elif opcao == 6:
                de_nome = input("Digite o nome (Quem irá transferir): ")
                de_pin = int(input("Digite o PIN (Quem vai transferir): "))
                para_nome = input("Digite o nome (Quem irá receber): ")
                para_pin = int(input("Digite o PIN (Quem vai receber): "))
                quantia = float(input("Digite o valor a ser transferido: R$"))
                banco.transferir(de_nome, de_pin, para_nome, para_pin, quantia)

            elif opcao == 7:
                nome = input("Digite o nome: ")
                pin = int(input("Digite o PIN: "))
                banco.getInfoConta(nome, pin)

            elif opcao == 8:
                nome = input("Digite o nome: ")
                pin = int(input("Digite o PIN: "))
                banco.getBalance(nome, pin)

            elif opcao == 9:
                nome = input("Digite o nome: ")
                pin = int(input("Digite o PIN: "))
                banco.calcularJuros(nome, pin)

            elif opcao == 0:
                print("Saindo...")
                break

            else:
                print("Opção inválida. Tente novamente.")

        except ValueError as ve:
            print(f"ERRO! Valor inválido: {ve}")
            print("=-"*30)
        except KeyError as ke:
            print(f"ERRO! Chave não encontrada: {ke}")
            print("=-"*30)
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            print("=-"*30)


main()
