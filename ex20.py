# Em uma loja de eletroeletrônicos, um vendedor que consiga vender mais de R$
# 3.000,00 por mês recebe como comissão 5% do valor vendido. Abaixo disso, ele não
# recebe nenhuma comissão. Faça um programa que leia do teclado o total de vendas
# mensais de um vendedor e imprima se ele tem direito a comissão e, se tiver, de
# quanto.

LIMITE_VENDA = 3000
PORCE_COMISSAO = 0.05

def calcular_comissao(total_vendas):
    resultado_calc = total_vendas * PORCE_COMISSAO
    return resultado_calc

def main():
    while True:
        try:
            # Solicita a entrada do valor de vendas
            total_vendas = float(input("Insira o total de vendas no mês para verificar se possui comissão e qual o valor dela: "))
            
            # Verifica se o valor é positivo
            if total_vendas < 0:
                print("O valor das vendas deve ser um número positivo.")
            else:
                break  # Sai do loop se o valor for válido
        except ValueError:
            # Caso o usuário insira um valor não numérico
            print("Por favor, insira um número válido.")

    comissao = calcular_comissao(total_vendas)

    # Verifica se o valor de vendas é maior que o limite para comissão
    if total_vendas > LIMITE_VENDA:
        print(f"Você tem direito a uma comissão de R${comissao:.2f}")
    else:
        print("Você não tem direito a comissão.")

# Executa o programa
main()

