'''
14. Construa um programa que calcule e mostre a soma dos 30 primeiros termos da 
série: 450/10 + 445/11 + 440/12 + 435/13 + ...
'''

def soma_serie():
    soma = 0
    for c in range(0, 29 + 1):
        soma +=  (450 - 5 * c) / (10 + c)
    
    return soma

def main():
    resultado = soma_serie()
    print(f"\nA soma dos 30 primeiros termos da série é igual a {resultado}")

main()

