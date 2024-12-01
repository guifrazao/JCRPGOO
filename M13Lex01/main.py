from corrente import Corrente
from poupanca import Poupanca
from investimento import Investimento


def main():
    print("=-"*30)
    print(" --- TIPOS DE CONTA ---")
    print("--"*30,"\n")
    conta_corrente = Corrente("123", "Alice", balance=500)
    print("Conta Corrente:")
    conta_corrente.deposit(200)
    conta_corrente.withdraw(300)
    conta_corrente.show_balance()
    print("=-"*30,"\n")

    conta_poupanca = Poupanca("456", "Bob", balance=1000)
    print("Conta Poupança:")
    conta_poupanca.apply_interest()  
    conta_poupanca.deposit(500)
    conta_poupanca.withdraw(200)
    conta_poupanca.show_balance()
    print("=-"*30,"\n")

    conta_investimento = Investimento("789", "Carol", balance=1500)
    print("Conta Investimento:")
    conta_investimento.invest()  
    conta_investimento.deposit(500)
    conta_investimento.withdraw(700)
    conta_investimento.show_balance()
    print("=-"*30)

main()
