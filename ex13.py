"""
A série de Fibbonacci é gerada da seguinte forma: os dois primeiros termos são 1, os
demais são dados pela soma dos dois anteriores. Faça um programa que imprima os
“n” primeiros termos da série, sendo “n” dado pelo usuário.
"""
def calcular_termos(n):
    termo1 = 0
    termo2 = 1
    if n <= 0:
        print("Não foi exigido nenhum número de termos válidos")
        print("Portanto, termo: {}")
    elif n == 1:
        print(termo1)
    else:
        print(termo1,termo2,end=" ")
        for i in range(3,n+1):
            termo3 = termo1 + termo2
            termo1 = termo2
            termo2 = termo3
            print(termo3, end=" ")

def verificar_inteiro(menssagem):
    while True:
        try:
            n = int(input(menssagem))
            return n
        except ValueError:
            print("ERROR! Insira um número inteiro!")

def main():
    n = verificar_inteiro("Digite o número de termos desejado: ")
    calcular_termos(n)

main()
        