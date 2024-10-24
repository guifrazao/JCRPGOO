"""
Refazer a Lista M3L, aplicando o Princípio da Responsabilidade Única e mostrar as
diferenças de seu código, antes e depois.

Implemente a classe Bank considerando os métodos listados abaixo e acrescentando
métodos que considerar conveniente.
"""

from BankUI import BankUI
from Bank import Bank

def menu():
    print("""
    Opções:
----------------------------------------
[1] Criar Conta
[2] Deletar Conta
[3] Depositar Dinheiro
[4] Sacar Dinheiro
[5] Transferir Dinheiro
[6] Listar Contas
[7] Obter Informações de uma conta
[8] Consultar Saldo
[9] Calcular Juros da Conta
[10] Pagar Conta
[11] Sair
""")
    print("=-"*30)

    try:
        opcao = int(input("Escolha uma opção: "))
        print("=-"*30)
        if opcao < 1 or opcao > 11:
            print("ERRO! Opção Inválida")
        return opcao
    except ValueError:
        print("ERRO! Você deve digitar um número válido.")
        return None

def main():
    bank = Bank()
    ui = BankUI(bank)
    while True:
        print("=-"*30)
        if input("Pressione ENTER para ir ao MENU. ") == "":
            opcao = menu()
            if opcao is None:
                continue
        try:
            if opcao == 1:
                ui.create_account()
            elif opcao == 2:
                ui.delete_account()
            elif opcao == 3:
                ui.deposit()
            elif opcao == 4:
                ui.withdraw()
            elif opcao == 5:
                ui.transfer()
            elif opcao == 6:
                ui.list_accounts()
            elif opcao == 7:
                ui.get_account_info()
            elif opcao == 8:
                ui.check_balance()
            elif opcao == 9:
                ui.calculate_interest()
            elif opcao == 10:
                ui.pay_bill()
            elif opcao == 11:
                print("Saindo...")
                break
            else:
                print("ERRO! Opção Inválida")
        except ValueError as ve:
            print(f"Erro de valor: {ve}")
        except KeyError as ke:
            print(f"Erro de chave: {ke}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

main()

