"""
Uma equação do segundo grau é escrita:
ax² + bx + c = 0
e a sua solução é dada em
função dos valores de a, b e c. Podendo ter duas raízes, uma ou nenhuma. Escreva
uma função que resolva a equação do segundo grau, retornando o número de raízes
encontradas. Os valores dessas raízes devem ser retornados em parâmetros.
"""
from math import sqrt

def verificar_entrada(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("ENTRADA INVÁLIDA! Insira um número")

def verificar_a(mensagem):
    while True:
        entrada = input(mensagem)
        try:
            valor_a = float(entrada)
            if valor_a == 0:
                print("""ERROR! O valor de "a" não pode ser igual a 0 para uma equação de 2º grau.""")
            else:
                return valor_a
        except ValueError:
            print("ERROR! Valor inválido, digite um valor numérico.")

def resolver_equacao_2grau(a, b, c):

    if a == 0:
        raise ValueError("""ERROR! o valor de "a" não pode ser igual a 0 para uma equação de 2º grau""")
    
    delta = b**2 - 4 * a * c

    if delta > 0:
        raiz1 = (-b + sqrt(delta)) / (2 * a)
        raiz2 = (-b - sqrt(delta)) / (2 * a)
        return 2, raiz1, raiz2
    elif delta == 0:
        raiz1 = raiz2 = -b / (2 * a)
        return 1,raiz1,raiz2
    else:
        return 0,0,0
    
def main():
    a = verificar_a("Insira o valor de a: ")
    b = verificar_entrada("Insira o valor de b: ")
    c = verificar_entrada("Insira o valor de c: ")

    try:
        numero_raizes,raiz1,raiz2 = resolver_equacao_2grau(a, b, c)

        print(f"Número de raízes: {numero_raizes}")
        if numero_raizes > 0:
            print(f"Raízes encontradas: {raiz1:.2f},{raiz2:.2f}")
        else:
            print("A equação não possuí raízes reais")
    except ValueError as e:
        print(e)

main()