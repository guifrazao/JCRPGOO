"""
Implemente uma classe chamada GuessingGame que represente um jogo de
adivinhação. Essa classe deve gerar um número aleatório, permitir que o jogador faça
palpites e informar se o palpite está correto, informando se é maior ou menor que o
número gerado.
"""

import random

class GuessingGame:
    def __init__(self):
        self._number_to_guess = self._generate_random_number()
        self._attempts = 0

    @staticmethod
    def _generate_random_number():
        return random.randint(1, 100)

    @classmethod
    def create_game(cls):
        return cls()

    def make_guess(self, guess):
        self._validate_guess(guess)
        self._attempts += 1
        
        if guess < self._number_to_guess:
            return "Seu palpite é menor que o número gerado."
        elif guess > self._number_to_guess:
            return "Seu palpite é maior que o número gerado."
        else:
            return f"Parabéns! Você acertou o número secreto *{self._number_to_guess}* em {self._attempts} tentativas!"

    @staticmethod
    def _validate_guess(guess):
        if not isinstance(guess, int):
            raise ValueError("O palpite deve ser um número inteiro.")
        if guess < 1 or guess > 100:
            raise ValueError("O palpite deve ser um número entre 1 e 100.")
