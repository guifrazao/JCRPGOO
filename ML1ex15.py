"""
15. Elabore um programa que calcule e mostre a soma dos 10 primeiros termos da série: 100/0! + 99/1! + 98/2! + 97/3!...
"""
def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def calcular_serie(n_inicial, qtd_termos):
    if qtd_termos == 0:
        return n_inicial/factorial(100-n_inicial)
    return n_inicial/factorial(100-n_inicial) + calcular_serie(n_inicial-1, qtd_termos-1)

def main():
    dez_primeiros = calcular_serie(100, 10)
    print(f"Soma dos números da série é: {dez_primeiros}")
main()
