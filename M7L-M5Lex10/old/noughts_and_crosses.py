class NoughtsAndCrosses:
    def __init__(self):
        self.player_X = "X"
        self.player_O = "O"
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.current_player = self.player_X

    @staticmethod
    def print_board(board):
        print("     0     1     2")
        print("   _________________ ")
        print(f"  |     |     |     |")
        print(f"0 |  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}  |")
        print(f"  |_____|_____|_____|")
        print(f"  |     |     |     |")
        print(f"1 |  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}  |")
        print(f"  |_____|_____|_____|")
        print(f"  |     |     |     |")
        print(f"2 |  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}  |")
        print(f"  |_____|_____|_____|")
        print()

    def make_move(self):
        print(f"{self.current_player}'s turn")
        row = col = -1
        while (row < 0 or row > 2) or (col < 0 or col > 2):
            row = int(input("Enter the row: "))
            col = int(input("Enter the column: "))
            print()
            if (row < 0 or row > 2) or (col < 0 or col > 2):
                print("Invalid input! Row and column must be between 0 and 2.\n")
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.switch_player()
        else:
            print("That spot is already taken. Try again.\n")

    def check_winner(self):
        # checking rows
        for rows in self.board:
            if rows[0] == rows[1] == rows[2] != " ":
                return rows[0]
        # checking columns
        for c in range(3):
            if self.board[0][c] == self.board[1][c] == self.board[2][c] != " ":
                return self.board[0][c]
        # checking diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[2][0] == self.board[1][1] == self.board[0][2] != " ":
            return self.board[2][0]
        # checking draw
        for row in self.board:
            for square in row:
                if square == " ":
                    return None
        return "Draw"

    def switch_player(self):
        if self.current_player == self.player_X:
            self.current_player = self.player_O
        else:
            self.current_player = self.player_X
