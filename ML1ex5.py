"""
5. Faça um programa que calcule a média de um aluno, quaisquer que sejam as suas
duas notas.
"""

def calcular_media(nota1, nota2):
    return (nota1 + nota2)/2

def main():
    media = calcular_media(7.6, 8.4)
    print(media)
main()
