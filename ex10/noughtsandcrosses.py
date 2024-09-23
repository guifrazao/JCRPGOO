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

class NoughtsAndCrosses:
    def __init__(self):
        self.player_1 = "X"
        self.player_2 = "O"
        self.grade = [[" "," "," "],[" "," "," "],[" "," "," "]]
        self.current_player = self.player_1

    def print_grade(self):
        print("     0     1     2")  
        print("   _________________ ")
        print(f"  |     |     |     |")
        print(f"0 |  {self.grade[0][0]}  |  {self.grade[0][1]}  |  {self.grade[0][2]}  |")
        print(f"  |_____|_____|_____|")
        print(f"  |     |     |     |")
        print(f"1 |  {self.grade[1][0]}  |  {self.grade[1][1]}  |  {self.grade[1][2]}  |")
        print(f"  |_____|_____|_____|")
        print(f"  |     |     |     |")
        print(f"2 |  {self.grade[2][0]}  |  {self.grade[2][1]}  |  {self.grade[2][2]}  |")       
        print(f"  |_____|_____|_____|")
        print()
    
    def make_move(self):
        print(f"{self.current_player}'s turn")
        row = col = -1
        while ((row < 0 or row > 2) or (col < 0 or col > 2)): 
            row = int(input("Enter the row: "))
            col = int(input("Enter the column: "))
            print()
            if ((row < 0 or row > 2) or (col < 0 or col > 2)):
                print("Invalid input! Row and column must be between 0 and 2.\n")
        if self.grade[row][col] == " ":
            self.grade[row][col] = self.current_player
            self.switch_player()
        else:
            print("That spot is already taken. Try again.\n")
        
    def check_winner(self):
        # checking rows
        for rows in self.grade:
            if (rows[0] == rows[1] == rows[2] != " "):
                return rows[0]

        # checking columns
        for c in range(3):
            if self.grade[0][c] == self.grade[1][c] ==  self.grade[2][c] != " ":
                return self.grade[0][c]
        
        # checking diagonals
        if (self.grade[0][0] == self.grade[1][1] == self.grade[2][2] != " "): 
            return self.grade[0][0]
        
        if (self.grade[2][0] == self.grade[1][1] == self.grade[0][2] != " "): 
            return self.grade[2][0]

        for row in self.grade:
            for square in row:
                if square == " ":
                    return None
        return "Draw"

    def switch_player(self):
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1

            
    
    
