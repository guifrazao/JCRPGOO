'''
Escreva um programa completo para jogar o jogo da velha. Para tanto crie uma 
classe NoughtsAndCrosses (jogo da velha): 
• a classe deve conter como dados privados um array bidimensional 3x3 para 
representar a grade do jogo 
• crie uma enumeração para representar as possibilidades de ocupação de uma 
casa na grade (vazia, jogador 1 ou jogador 2) 
• o construtor deve inicializar a grade como vazia 
• forneça um método para exibir a grade 
• permita dois jogadores humanos 
• forneça um método para jogar o jogo; todo movimento deve ocorrer em uma 
casa vazia; depois de cada movimento, determine se houve uma derrota ou um 
empate. 
'''

from noughtsandcrosses import NoughtsAndCrosses

game = NoughtsAndCrosses()

def main():
    while True:
        game.print_grade()
        game.make_move()
        checking_winner = game.check_winner()
        if checking_winner:
            if checking_winner == "Draw":
                print("Draw\n")
            else:
                print(f"The winner is {checking_winner}\n")   
            game.print_grade()
            exit()

main()