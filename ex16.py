'''
16. Sendo S = 1 - 1/2 + 1/3 - 1/4 + 1/5 - ... + 1/N , construa um programa que leia N, calcule e mostre o valor da série S. 
'''

def soma_serie(n):
    soma = 0
    sinal = 1
    for c in range(1, n + 1):
        soma += sinal * (1 / c)
        sinal *= (-1)   
    return soma

def main():
    n = -1
    while n <= 0:
        n = int(input("Informe N: "))
        if n > 0:
            break
    
    resultado = soma_serie(n)
    print(f"\nA soma dos N primeiros termos da série é igual a {resultado:.2f}")

main()
