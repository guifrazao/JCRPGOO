"""
Elabore um programa que:
• Mostre um menu de opções de conversão entre moedas (1 – dólar americano,
2 – euro, 3 – libra esterlina e 4 – yuan;
• Leia a escolha do usuário;
• Leia o custo em R$ (reais) da operação;
• Imprima o valor da transação na moeda escolhida, de acordo com os fatores
de conversão da tabela abaixo.

Moeda             Valor (R$)

Dólar americano - 3,258
Euro ------------ 4,095
Libra esterlina - 4,529
Yuan ------------ 0,515
"""

def menu():
    opcao = -1
    while opcao < 1 or opcao > 5:
        print("=" *45)
        print(
            '''
    Conversor de moedas
--------------------------------------
[1] Dólar americano
[2] Euro
[3] Libra esterlina
[4] Yuan
[5] Sair
        '''
        )
        print("=" *45)

        try:

            opcao = int(input("Digite a sua opção: "))
            print("-="*30)

            if opcao < 1 or opcao > 5:
                print("Opção Inválida")
        except ValueError:
            print("Entrada INVÁLIDA! Por favor, escolha uma das opções acima.")
    return opcao

def conversor_dolar(reais):
    DOLAR = 3.258
    return reais / DOLAR

def conversor_euro(reais):
    EURO = 4.095
    return reais / EURO

def conversor_libra(reais):
    LIBRA = 4.529
    return reais / LIBRA

def conversor_yuan(reais):
    YUAN = 0.515
    return reais / YUAN

def verificar_float(mensagem):
    while True:
        try:
            reais = float(input(mensagem))
            return reais
        except ValueError:
            print("Entrada INVÁLIDA! Por favor, insira um número inteiro positivo")

def main():
    while True:
        escolha = menu()

        if escolha == 5:
            print("Saindo...")
            break

        reais = verificar_float("Digite o valor a ser convertido: R$")
        if reais < 0:
            print("ERRO! Digite um valor positivo")
        else:

            if escolha == 1:
                resultado = conversor_dolar(reais)
                print(f"O valor R${reais} convertido em DÓLAR é: {resultado}")
            elif escolha == 2:
                resultado = conversor_euro(reais)
                print(f"O valor R${reais} convertido em EURO é: {resultado}")
            elif escolha == 3:
                resultado = conversor_libra(reais)
                print(f"O valor R${reais} convertido em LIBRA é: {resultado}")
            else:
                resultado = conversor_yuan(reais)
                print(f"O valor R${reais} convertido em YUAN é: {resultado :.2f}") 
                
main()






