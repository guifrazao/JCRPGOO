from M5Lex08 import GuessingGame

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