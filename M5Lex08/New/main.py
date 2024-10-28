"""
Refazer as listas M3L e M5L, aplicando o Princípio Aberto-Fechado e mostrar as diferenças
de seu código, antes e depois.

Implemente uma classe chamada GuessingGame que represente um jogo de
adivinhação. Essa classe deve gerar um número aleatório, permitir que o jogador faça
palpites e informar se o palpite está correto, informando se é maior ou menor que o
número gerado.
"""

from GuessingGame import GuessingGame
import random

def custom_number_generator():
    return random.randint(1, 100) 

def custom_guess_validator(guess):
    if not isinstance(guess, int):
        raise ValueError("O palpite deve ser um número inteiro.")
    if guess < 1 or guess > 100:
        raise ValueError("O palpite deve ser um número entre 01 e 100.")


def main():
    game = GuessingGame.create_game(custom_number_generator, custom_guess_validator)

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
