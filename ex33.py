'''
33. O valor aproximado de pi pode ser calculado a partir da série: pi = 4/1 - 4/3 + 4/5 - 4/7 + ...
Escreva uma função que calcule o valor de pi, com precisão dada como parâmetro.

OBS: À medida que você vai somando mais e mais termos dessa série, o resultado vai se aproximando cada vez mais do valor real de pi.
'''

def calcular_pi(precisao):
    pi = 0
    sinal = 1
    for c in range(0, precisao):
        pi += (sinal * (4 / (1 + 2 * c)))
        sinal *= (-1)
    
    return pi

def main():
    n_termos = 1000000
    resultado = calcular_pi(n_termos)
    print(f"A aproximação com {n_termos} termos da série é igual a {resultado}")

main()