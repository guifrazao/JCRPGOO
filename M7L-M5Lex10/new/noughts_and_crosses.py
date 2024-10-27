'''
M5L-ex10. Escreva um programa completo para jogar o jogo da velha. Para tanto crie uma 
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

class NoughtsAndCrosses:
    def __init__(self):
        self.player_1 = "X"
        self.player_2 = "O"
        self.grade = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.current_player = self.player_1
        self.move_history = []

    def switch_player(self):
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1

    def perform_action(self, action):
        return action.execute(self)
