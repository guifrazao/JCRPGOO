'''
19. Faça um programa didático para estudo de tabuadas de 1 até 10, onde: 
a. A criança escolhe a tabuada a ser estudada. 
b. O programa gera um número aleatório e pergunta à criança qual o valor dele 
multiplicado pela tabuada escolhida. Se a criança errar, o programa pergunta 
novamente, se acertar o programa pergunta à criança se ela deseja continuar 
respondendo. 
c. Ao final, o programa deve imprimir o número de perguntas respondidas, o 
número de acertos e o número de erros cometidos pela criança. 
'''
import random

def validar_entrada(msg):
    while True:
        try:
            valor_str = input(msg)
            valor_int = int(valor_str)
            return valor_int
        except ValueError:
            print(50*"=")
            print("ERRO! Informe um inteiro válido.")
            print(50*"=")


def tabuada(tabuada_escolhida):
    acertos = erros = perguntas = 0

    while True:
        numero_aleatorio = random.randint(1, 10)
        gabarito = numero_aleatorio * tabuada_escolhida

        while True:
            resposta = validar_entrada(f"{numero_aleatorio} x {tabuada_escolhida} = ")
            perguntas += 1
            if resposta == gabarito:
                print("Parabéns, você acertou!")
                acertos += 1
                break
            else:
                erros += 1
            
        continuar = input("Deseja continuar? [S/N]: ").lower()
        print()
        if continuar != 's':
            break

    print(f"Você respondeu {perguntas} perguntas.")
    print(f"Você acertou {acertos} perguntas.")
    print(f"Você errou {erros} perguntas.")


def main():
    t = 0
    while t <= 0 or t > 10:
        t = validar_entrada("Qual tabuada deseja estudar? [1-10] ")
        if t >= 1 and t <= 10:
            tabuada(t)
        else:
            print(50*"=")
            print("ERRO! Informe um número entre 1 e 10.")
            print(50*"=")

main()