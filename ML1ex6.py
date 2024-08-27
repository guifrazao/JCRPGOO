"""
6. Faça um programa que calcule a nota que um aluno deve tirar na terceira prova para
obter média 7, quaisquer que sejam as notas das duas primeiras provas.
"""

def calcular_nota3(nota1, nota2):
    return (7*3) - nota1 - nota2

def main():
    nota3 = calcular_nota3(7.6, 8.4)
    print(nota3)
main()
