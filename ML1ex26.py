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
    
def processar_dados(folha_pagamento):
    total_folha_atual = total_folha_prog = total_folha_uni = 0.0   

    total_folha_atual += sum(folha_pagamento)
    total_folha_prog += calcular_aumento_prog(total_folha_atual)
    total_folha_uni += calcular_aumento_uni(total_folha_atual)

    return total_folha_atual, total_folha_prog, total_folha_uni

def calcular_aumento_prog(salario):
    progressivo = 0.0

    if salario < 1000.00:
        progressivo = salario * 1.15
    elif salario < 2000.00:
        progressivo = salario * 1.10
    else:
        progressivo = salario * 1.05
    return progressivo

def calcular_aumento_uni(salario):
    return salario * 1.10

def main():
    try:
        n_func = -1
        aumento_uni = aumento_prog = total_folha_atual = total_folha_prog = total_folha_uni = 0.0
        folha_pagamento = []

        while n_func < 0:
            n_func = int(input("Informe a quantidade de funcionários: "))

        for i in range(n_func):
            salario = -1
            print("=" * 80)

            while salario < 0:
                salario = float(input(f"Informe o salário do {i+1}° funcionário: "))
                
            folha_pagamento.append(salario)
            aumento_uni, aumento_prog = calcular_aumento_uni(salario), calcular_aumento_prog(salario)
            print(f"Salário em caso de aumento uniforme: R${aumento_uni:.2f}\nSalário em caso de aumento progressivo: R${aumento_prog:.2f}")

        total_folha_atual, total_folha_prog, total_folha_uni = processar_dados(folha_pagamento)
            
        print("=" * 80 + "\n")
        print(f"Total de funcionarios: {n_func}")
        print(f"Salário médio dos funcionários: R${total_folha_atual/n_func:.2f}")
        print(f"Total da folha de pagamentos atual: R${total_folha_atual:.2f}")
        print(f"Total da folha de pagamento no caso de aumento uniforme: R${total_folha_uni:.2f}")
        print(f"Total da folha de pagamento no caso de aumento progressivo: R${total_folha_prog:.2f}")
    except ValueError:
        print("Dado(s) inválido(s), fim do programa")
    except Exception as e:
        print(f"Erro fatal: {e}")
main()
            


