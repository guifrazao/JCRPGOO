"""
26. Uma empresa está fazendo um estudo de possibilidades de aumento aos seus
funcionários e deseja saber se é mais vantajoso dar um aumento uniforme de 10% à
todos os funcionários ou seguir a seguinte tabela progressiva:
Salário  Percentual de aumento
até R$1000,00      -     15%
até R$2000,00      -     10%
acima de R$2000,00 -     5%

Faça um programa que leia o salário de um número qualquer de funcionários,
imprimindo para cada um o novo salário nos dois casos (aumento uniforme ou
aumento progressivo). Ao final, o programa deve fornecer:
a. O total de funcionários
b. O salário médio dos funcionários
c. O total da folha de pagamentos atual
d. O total da folha de pagamentos futura nos dois casos estudados, indicando
qual o caminho mais econômico para a empresa.
"""

def calcular_aumento_prog(salario):
    progressivo = 0.0

    if salario < 1000.00:
        progressivo = salario * 1.15
    elif salario < 2000.00:
        progressivo = salario * 1.10
    else:
        progressivo = salario * 1.05
    
    return progressivo


def main():
    try:
        n_func = -1
        total_func = 0
        total_folha_atual = 0.0
        total_folha_uni = 0.0
        total_folha_prog = 0.0

        while n_func < 0:
            n_func = int(input("Informe a quantidade de funcionários: "))
        for i in range(n_func):
            salario = -1
            while salario < 0:
                salario = float(input(f"Informe o salário do {i+1}° funcionário: "))
            
            total_func += 1
            total_folha_atual += salario
            total_folha_prog += calcular_aumento_prog(salario)

        total_folha_uni = total_folha_atual * 1.10
        print("=" * 80 + "\n")
        print(f"Total de funcionarios: {total_func}")
        print(f"Salário médio dos funcionários: {total_folha_atual/total_func:.2f}")
        print(f"Total da folha de pagamentos atual: {total_folha_atual}")
        print(f"Total da folha de pagamento no caso de aumento uniforme: {total_folha_uni:.2f}")
        print(f"Total da folha de pagamento no caso de aumento uniforme: {total_folha_prog:.2f}")
    except ValueError:
        print("Dado(s) inválido(s), fim do programa")
    except Exception as e:
        print(f"Erro fatal: {e}")
main()
            


