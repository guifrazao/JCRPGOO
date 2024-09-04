'''
21. Faça um programa didático para estudo das raízes quadradas dos números, da 
seguinte forma: o programa gera um número aleatório, eleva ao quadrado e pergunta 
qual a raiz quadrada desse valor para o estudante. O programa deve apresentar as 
mensagens de erro e incentivo e os números de perguntas, acertos e erros de forma 
semelhante aos anteriores.
'''

import random

def raiz_quadrada():
    acertos = erros = perguntas = 0

    while True:
        raiz = random.randint(1, 20)
        pergunta = pow(raiz, 2)

        while True:
            try:
                resposta = int(input(f"√{pergunta} = "))
                perguntas += 1
                if resposta == raiz:
                    print("Parabéns, você acertou!")
                    acertos += 1
                    break
                else:
                    print("Que pena, você errou! Tente novamente!\n")
                    erros += 1
            except:
                print("Entrada inválida. Por favor, digite um número.")
            
        continuar = input("Deseja continuar? [S/N]: ").lower()
        print()
        if continuar != 's':
            break

    print(f"Você respondeu {perguntas} perguntas.")
    print(f"Você acertou {acertos} perguntas.")
    print(f"Você errou {erros} perguntas.")


def main():
    raiz_quadrada()

main()