'''
31. A multiplicação entre dois números inteiros pode ser definida como uma repetição da 
adição de um deles. Exemplo: 3 x 4 = 4 + 4 + 4 
Escreva uma função que multiplique dois números inteiros utilizando esse método. A 
seguir, escreva um programa que peça ao usuário um número inteiro e imprima a 
tabuada para aquele número (de 1 à 10) utilizando a função construída.
''' 

def multiplicação(x, y):
    soma = 0
    print(f"{x:>2} x {y} = ", end='')
    for c in range(1, x + 1):
        soma += y
        if c < x:
            print(y, end=' + ')
        else:
            print(f'{y} = {soma}')
    print()

def tabuada(t):
    for c in range(1, 10 + 1):
        multiplicação(c, t)

def main():
    print("\tMultiplicação e Tabuada")
    while True:
        try:
            t = int(input("\nInforme um número inteiro maior que 0: "))
            if t > 0:
                tabuada(t)
                break  
        except ValueError:
            print("Entrada inválida")
    
main()