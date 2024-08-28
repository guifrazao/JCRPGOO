"""
22. Calcule e mostre o imposto de renda de um grupo de contribuintes considerando que
os dados de cada contribuinte (número do CPF, número de dependentes e renda
mensal) são valores fornecidos pelo usuário. Para cada contribuinte será feito um
desconto no imposto de 5% do salário mínimo (R$136,00) para cada dependente (o
salário mínimo e o desconto são designados por constantes simbólicas). Os valores
da alíquota para cálculo do imposto são:

    até R$900,00 - isento
    900,01 até 1500,00 - 5%
    1500,01 até 1900,00 - 10%
    1900,01 até 2200,00 - 15%
    acima de 2200,01 - 20%

O último valor, que não será considerado, terá o número do CPF igual a zero. Ao final,
devem ser impressos:
a. Para cada contribuinte, o total a pagar.
b. O número de contribuintes.
c. O total de contribuintes isentos e não isentos.
d. O total de impostos que serão arrecadados desse grupo de contribuintes.
e. O número do CPF e o valor da contribuição daquele contribuinte que for pagar
o maior imposto.


"""

SALARIO_MINIMO = 1412.00
DESCONTO_IMPOSTO = 136.00

def calcular_IR(renda_mes, n_dep):
    aliquota = definir_aliquota(renda_mes)
    return (renda_mes - n_dep * DESCONTO_IMPOSTO) * aliquota

def definir_aliquota(renda_mes):
    if renda_mes < 900.00:
        return 0.00
    elif renda_mes < 1500.00:
        return 1.05
    elif renda_mes < 1900.00:
        return 1.10
    elif renda_mes < 2200.00:
        return 1.15
    return 1.20

def verificacao_cpf_lista(dados):
    for i in range(0, len(dados)):
        if dados[i][0] == dados[i-1][0] and i > 0:
            return False
    return True



def main():
    dados_contribuintes = []  
    n_contribuintes = 0
    qtd_isento = 0
    qtd_nao_isento = 0
    total_impostos = 0.00
    maior_contribuicao = -1.00
    cpf_maior = 0
    try:
        while True:
            cpf = -1
            n_dep = -1
            renda_mes = -1
            
            while cpf < 0:
                cpf = int(input("Digite o CPF do contribuinte (sem pontos nem traços) (digite 0 para sair): "))
            if cpf == 0:
                break   
            while len(str(cpf)) != 11:
                 cpf = int(input("Formato de CPF inválido, redigite (sem pontos nem traços) (digite 0 para sair): "))                     
            while n_dep < 0:
                n_dep = int(input("Digite o número de dependentes do contribuinte: "))
            while renda_mes < 0:
                renda_mes = float(input("Digite a renda mensal do contribuinte: "))

            imposto_renda = calcular_IR(renda_mes, n_dep)     
            dados_contribuintes.append([cpf, n_dep, renda_mes, imposto_renda]) 
            if not verificacao_cpf_lista(dados_contribuintes):
                raise Exception("CPFs iguais detectados")     
            total_impostos += imposto_renda
            n_contribuintes += 1
            
            if imposto_renda == 0:
                qtd_isento += 1
            else:
                qtd_nao_isento += 1       

            if imposto_renda > maior_contribuicao:
                maior_contribuicao = imposto_renda
                cpf_maior = cpf

        print("=" * 80)
        print("Total a pagar para cada contribuinte, por ordem de cadastro: ")  
        for i in range(len(dados_contribuintes)):
            print(f"{i+1}° contribuinte: R${dados_contribuintes[i][3]:.2f}")
        print("")
        print(f"Número de contribuintes: {n_contribuintes}")
        print(f"Total de contribuintes isentos: {qtd_isento}")
        print(f"Total de contribuintes não isentos: {qtd_nao_isento}")
        print(f"Total de impostos arrecadados: R${total_impostos:.2f}")
        print(f"Maior contribuição: R${maior_contribuicao:.2f}, vinda do dono do CPF {cpf_maior}")
    except Exception as e:
        print(f"Erro fatal: {e}")

main()
