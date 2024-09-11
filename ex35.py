'''
35. Faça um programa que apresente na tela um menu com as seguintes opções: 1. 
Converter um ângulo em graus para radiano; 2. Calcular o seno de um ângulo, 3. 
Calcular o valor de PI. 4. Resolver uma equação do segundo grau; 0. Sair. Depois de 
feita a opção, o programa deve chamar uma função que leia do usuário os parâmetros 
necessários para o cálculo escolhido e a seguir usar uma das funções que você já 
implementou.
'''
from math import pi

def graus_para_rad(graus):
    radianos = graus * (pi / 180)

    return radianos

def factorial(n):
     if n == 1:
          return 1
     return n * factorial(n-1)

def calcular_seno(angulo, acc):
    angulo_rad = graus_para_rad(angulo)
    seno = 0
    sinal = 1
    for i in range(1, acc, 2):
            seno += (pow(angulo_rad, i) / factorial(i)) * sinal 
            sinal *= -1
    return seno

def valor_pi():
    print("\nO valor aproximado de PI pode ser calculado a partir da série: "
          "\nPI = 4/1 - 4/3 + 4/5 - 4/7 ..."
          "\nOBS: Quanto maior o número de termos da série, melhor a aproximação")
    n_termos = int(input("\nCom quantos termos deseja aproximar PI? "))
    aproximacao_pi = 0
    sinal = 1
    for c in range(0, n_termos):
        aproximacao_pi += (sinal * (4 / (1 + 2 * c)))
        sinal *= (-1)
    
    return aproximacao_pi

def equação_segundo_grau(a, b, c):
    delta = pow(b , 2) - (4 * a * c)
    x1 = (- b + pow(delta, 0.5)) / (2 * a)
    x2 = (- b - pow(delta, 0.5)) / (2 * a)

    return delta, x1, x2

def menu():
    opcao = -1

    while opcao < 0 or opcao > 4:
        print("\tMenu")
        print("1. Converter um ângulo em graus para radiano")
        print("2. Calcular o seno de um ângulo [0 à pi/2]")
        print("3. Calcular o valor de PI")
        print("4. Resolver uma equação do segundo grau")
        print("0. Sair")

        opcao = int(input("Digite sua opcao: "))

        if opcao < 0 or opcao > 4:
            print("Você informou um valor invalido\n")
        
    return opcao

def main():
    escolha = -1

    while escolha != 0:
        escolha = menu()
        
        if escolha == 0:
            print("\nSaindo...")
            print("Programa encerrado!")
        if escolha == 1:
            angulo_graus = int(input("\nInforme o ângulo(em graus): "))
            resultado_1 = graus_para_rad(angulo_graus)
            print(f"\nO ângulo de {angulo_graus}° é igual a {resultado_1:.6f} radianos\n")
        elif escolha == 2:
            angulo = int(input("\nInforme um ângulo(em graus): "))
            resultado_2 = calcular_seno(angulo, 50)
            print(f"\nO seno de {angulo}° é igual a {resultado_2}\n")
        elif escolha == 3:
            resultado_3 = valor_pi()
            print(f"A aproximação de PI é igual a {resultado_3:.6f}\n")
        else:
            print('Dada a equação quadrática ax² + bx + c = 0')
            coef_a = int(input('Informe o valor de a:'))
            coef_b = int(input('Informe o valor de b:'))
            coef_c = int(input('Informe o valor de c:'))
            
            resultado_4 = equação_segundo_grau(coef_a, coef_b, coef_c)
            Delta, x_1, x_2 = resultado_4

            if Delta > 0:
                print('\nDelta > 0. Logo, a equação possui duas raízes reais e distintas')
                print(f'x1 = {x_1:.2f}, x2 = {x_2:.2f}\n')
            elif Delta == 0:
                print('\nDelta = 0. Logo, a equação possui duas raízes reais e iguais')
                print(f'x1 = {x_1:.2f}, x2 = {x_2:.2f}\n')
            else:
                print('\nDelta < 0. Logo, a equação não possui raízes reais\n')

main()