'''Um shopping está fazendo uma promoção na qual o cliente que fizer compras de
valor até R$ 1000,00 ganha um cupom para concorrer a um carro e se ele comprar
acima de R$ 1000,00 ganha dois cupons e um vale-desconto no total de 10% da
compra. Faça um programa que leia do teclado o total de compras e imprima se o
cliente tem direito a 1 cupom, ou a 2 cupons e o vale-desconto (nesse caso, imprima
o valor do desconto). Declare como constantes simbólicas o limite e o percentual do
desconto.'''

LIMITE_COMPRA = 1000
VALE_DESCONTO = 0.10

def inserir_compras():
    valor_total = 0

    # Obtém o número de compras
    while True:
        try:
            n = int(input("Quantas compras deseja inserir: "))
            if n < 0:
                print("Insira um número positivo.")
            else:
                break  # Sai do loop se n for positivo
        except ValueError:
            print("Por favor, insira um número válido.")

    # Insere os valores das compras
    for i in range(n):
        valor = -1  # Inicializa o valor como inválido

        while valor < 0:  # Fica no loop até que um valor positivo seja inserido
            try:
                valor = float(input(f"Insira o valor da compra {i + 1}: "))

                if valor < 0:
                    print("Valor inválido, insira valores positivos.")
            except ValueError:
                print("Por favor, insira um número válido.")
        
        valor_total += valor  # Somente adiciona se o valor for positivo

    return valor_total

def calculo_desconto (valor_total):
    resultado_calc = valor_total * VALE_DESCONTO

    return resultado_calc

def main ():

    compras_total = inserir_compras()
    
    if compras_total > LIMITE_COMPRA:
        vale_desc = calculo_desconto(compras_total)
        print(f"Você tem direito a 2 cupons e um vale-desconto de R$ {vale_desc:.2f}.")
    else:
        print("Você tem direito a 1 cupom")

    print(f"Você fez um total de compras no valor de R$ {compras_total:.2f}")

main()



    









