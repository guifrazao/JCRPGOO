"""
5. Fazer um programa que calcule e escreva o número de grãos de milho que podem ser
colocados em um tabuleiro de xadrez, colocando 1 no primeiro quadro e nos quadros
seguintes o dobro do quadro anterior. Obs.: esse número cresce muito rápido, tenha
o cuidado de testar se ele não sofre um overflow.
"""
def calcular_milho_tabuleiro(n_quadros):
    qtd_milho = 1
    for i in range (0, n_quadros):
        qtd_milho += pow(2, i)
    return qtd_milho

def main():
    milho = calcular_milho_tabuleiro(64)
    print(milho)
main()
