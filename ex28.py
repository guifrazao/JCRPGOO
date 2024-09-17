"""
Em uma loja de eletrodomésticos, os funcionários da seção de TVs recebem,
mensalmente um salário fixo mais comissão. Essa comissão é calculada em relação
ao tipo e número de televisores vendidos, de acordo com a tabela abaixo:

Tipo       Quantidade vendida                     Comissões
8 K     |        10 ou mais          |          R$ 550 por TV vendida
________|        Menos que 10        |          R$ 350 por TV vendida
4 K     |        10 ou mais          |          R$ 420 por TV vendida
        |        Menos que 10        |          R$ 250 por TV vendida

Sabe-se ainda, que ele tem um desconto de 8% do salário total para pagamento do
INSS e se o seu salário total for superior a R$ 950,00 ele ainda tem um desconto de
5% do salário para fins de imposto de renda. Faça um programa que leia os dados de
vários funcionários e, para cada funcionário, calcule e imprima o salário líquido (já
com os descontos). Além disso, no final, o programa deve:
a. Imprimir o número de funcionários.
b. Imprimir o total de salários pagos.
c. Imprimir a média das comissões.
d. Imprimir o valor da maior e da menor comissão paga pelo departamento.
"""

def verificar_entrada(mensagem, tipo):
    while True:
        try:
            if tipo == "int":
                valor = int(input(mensagem))
                if valor < 0:
                    print("ERROR! O valor não pode ser negativo.")
                    continue
                return valor
            elif tipo == "float":
                valor = float(input(mensagem))
                if valor < 0:
                    print("ERROR! O valor não pode ser negativo.")
                    continue
                return valor
            else:
                continue
        except ValueError:
            print("ERROR! Insira um valor válido.")

def calcular_comissao(qtd_4K,qtd_8K):
    if qtd_4K >= 10:
        comissao_4k = qtd_4K * 420
    else:
        comissao_4k = qtd_4K * 250
    
    if qtd_8K >= 10:
        comissao_8k = qtd_8K * 550
    else:
        comissao_8k = qtd_8K * 350

    return comissao_4k, comissao_8k

def calcular_salario(salario,comissao_4k,comissao_8k):
    salario += (comissao_8k + comissao_4k)
    salario_liquido = salario * 0.92
    if salario_liquido > 950:
        salario_liquido *= 0.95
    return salario_liquido

def exibir_resultados(qtd_funcionarios, salario_total,comissao_lista):
    print("--"*30)
    print(f"Número de funcionários: {qtd_funcionarios}")
    print("--"*30)
    print(f"Total de salários pagos: R${salario_total:.2f}")
    print("--"*30)
    if comissao_lista:
        print(f"Média das comissões: {sum(comissao_lista)/len(comissao_lista):.2f}")
        print("--"*30)
        print(f"Maior comissão: {max(comissao_lista)} || Menor comissão: {min(comissao_lista)}")
        print("-="*30)

def main():
    qtd_funcionarios = salario_total = 0
    comissao_lista = []

    while True:
        salario = verificar_entrada("Digite o salário do funcionário: R$","float")
        print("--"*30)
        qtd_4K = verificar_entrada("Quantidade de TV's 4K vendidas: ","int")
        print("--"*30)
        qtd_8K = verificar_entrada("Quantidade de TV's 8K vendidas: ","int")
        print("--"*30)

        comissao_4k,comissao_8k = calcular_comissao(qtd_4K,qtd_8K)
        salario_liquido = calcular_salario(salario, comissao_4k, comissao_8k)

        print(f"Salário líquido: R${salario_liquido:.2f}")  
        print("=-"*30)
        qtd_funcionarios += 1
        salario_total += salario

        if comissao_4k > 0:
            comissao_lista.append(comissao_4k)
        if comissao_8k > 0:
            comissao_lista.append(comissao_8k)
        
        while True:
            continuar = input("Deseja inserir mais funcionários? [S/N] ").strip().upper()
            if continuar in ["S","N"]:
                break
            else:
                print("Entrada inválida! Por favor, digite 'S' para Sim ou 'N' para Não.")
            
        if continuar == "N":
            print("=-"*30)
            break 

    exibir_resultados(qtd_funcionarios,salario_total,comissao_lista)

main()











