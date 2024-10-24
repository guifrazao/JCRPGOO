import random

class GuessingGame:
    def __init__(self):
        self.__number_to_guess = self.__generate_random_number() 
        self.__attempts = 0 

    @staticmethod
    def __generate_random_number():  
        return random.randint(1, 100)

    @classmethod
    def create_game(cls):
        return cls()

    def make_guess(self, guess):
        self.__validate_guess(guess) 
        self.__attempts += 1
        
        if guess < self.__number_to_guess:
            return "Seu palpite é menor que o número gerado."
        elif guess > self.__number_to_guess:
            return "Seu palpite é maior que o número gerado."
        else:
            return f"Parabéns! Você acertou o número secreto *{self.__number_to_guess}* em {self.__attempts} tentativas!"

    @staticmethod
    def __validate_guess(guess):
        if not isinstance(guess, int):
            raise ValueError("O palpite deve ser um número inteiro.")
        if guess < 1 or guess > 100:
            raise ValueError("O palpite deve ser um número entre 1 e 100.")

