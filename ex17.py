'''Em um Estado, os comerciantes com faturamento anual de até R$ 100.000,00 pagam
10% de ICMS sobre o faturamento e aqueles com faturamento superior pagam 15%.
Faça um programa que leia o faturamento de um comerciante e imprima o valor do
ICMS devido. Declare como constantes simbólicas o limite e os percentuais de
imposto.'''
LIMITE_FATURAMENTO = 100000
ICMS_BAIXO = 0.10
ICMS_ALTO = 0.15


def calculo_faturamento(faturamento):
    if faturamento <= LIMITE_FATURAMENTO:
        resultado_calc = faturamento * ICMS_BAIXO
    else: 
        resultado_calc = faturamento * ICMS_ALTO
    
    return resultado_calc


def main():
    while True:
        try:
            faturamento = float(input("Insira aqui seu faturamento anual para calcular o ICMS(ou digite 00 para sair): "))
            icms = calculo_faturamento(faturamento)

            if faturamento < 0:
                print("Valor inserido não pode ser negativo ou nulo")

            elif faturamento == 0:
                break

            else:
                print(f"O ICMS devido é de R$ {icms:.2f}")
            
        except ValueError:
            print("Valor inserido é inválido, insira apenas números positivos")

    
main()

