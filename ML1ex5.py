"""
5. Fazer um programa que calcule e escreva o número de grãos de milho que podem ser
colocados em um tabuleiro de xadrez, colocando 1 no primeiro quadro e nos quadros
seguintes o dobro do quadro anterior. Obs.: esse número cresce muito rápido, tenha
o cuidado de testar se ele não sofre um overflow.
"""
def calcular_milho_tabuleiro(qtd_milho, n_quadros):
    #tentei deixar isso recursivo mas nao tava querendo funcionar nao
    for i in range(n_quadros-1, 0, -1):
        qtd_milho += pow(2, i)
    return qtd_milho

def main():
    
    milho = calcular_milho_tabuleiro(1, 64)
    print(milho)
main()
