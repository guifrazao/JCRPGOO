"""
15. Elabore um programa que calcule e mostre a soma dos 10 primeiros termos da série: 100/0! + 99/1! + 98/2! + 97/3!...
"""
from math import factorial
def calcular_serie(n_inicial, qtd_series):
    if qtd_series == 0:
        return n_inicial/factorial(100-n_inicial)
    return n_inicial/factorial(100-n_inicial) + calcular_serie(n_inicial-1, qtd_series-1)

def main():
    dez_primeiros = calcular_serie(100, 10)
    print(f"Soma dos números da série é: {dez_primeiros}")
main()
