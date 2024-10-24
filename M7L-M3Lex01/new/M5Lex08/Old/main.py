"""
Implemente uma classe chamada GuessingGame que represente um jogo de
adivinhação. Essa classe deve gerar um número aleatório, permitir que o jogador faça
palpites e informar se o palpite está correto, informando se é maior ou menor que o
número gerado.
"""

from GuessingGame import GuessingGame

def main():
    game = GuessingGame.create_game()

    print("--------JOGO DA ADIVINHAÇÂO--------")
    print()
    
    while True:
        try:
            user_input = int(input("Faça um palpite (1-100): "))
            print("=-"*30)
            result = game.make_guess(user_input)
            print(result)
            print("--"*30)
            if "Parabéns" in result:
                break
        except ValueError as e:
            print(e)
    
main()