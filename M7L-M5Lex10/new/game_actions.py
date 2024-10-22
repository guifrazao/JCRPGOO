class PrintGrade:
    def execute(self, game):
        print("     0     1     2")
        print("   _________________ ")
        print(f"  |     |     |     |")
        print(f"0 |  {game.grade[0][0]}  |  {game.grade[0][1]}  |  {game.grade[0][2]}  |")
        print(f"  |_____|_____|_____|")
        print(f"  |     |     |     |")
        print(f"1 |  {game.grade[1][0]}  |  {game.grade[1][1]}  |  {game.grade[1][2]}  |")
        print(f"  |_____|_____|_____|")
        print(f"  |     |     |     |")
        print(f"2 |  {game.grade[2][0]}  |  {game.grade[2][1]}  |  {game.grade[2][2]}  |")
        print(f"  |_____|_____|_____|")
        print()

class MakeMove:
    def execute(self, game):
        print(f"{game.current_player}'s turn")
        row = col = -1
        while (row < 0 or row > 2) or (col < 0 or col > 2):
            row = int(input("Enter the row: "))
            col = int(input("Enter the column: "))
            print()
            if (row < 0 or row > 2) or (col < 0 or col > 2):
                print("Invalid input! Row and column must be between 0 and 2.\n")
        if game.grade[row][col] == " ":
            game.grade[row][col] = game.current_player
            game.move_history.append((row, col))
            game.switch_player()
        else:
            print("That spot is already taken. Try again.\n")

class CheckWinner:
    def execute(self, game):
        # checking rows
        for rows in game.grade:
            if rows[0] == rows[1] == rows[2] != " ":
                return rows[0]
        # checking columns
        for c in range(3):
            if game.grade[0][c] == game.grade[1][c] == game.grade[2][c] != " ":
                return game.grade[0][c]
        # checking diagonals
        if game.grade[0][0] == game.grade[1][1] == game.grade[2][2] != " ":
            return game.grade[0][0]
        if game.grade[2][0] == game.grade[1][1] == game.grade[0][2] != " ":
            return game.grade[2][0]
        # checking draw
        for row in game.grade:
            for square in row:
                if square == " ":
                    return None
        return "Draw"

class UndoMove:
    def execute(self, game):
        if not game.move_history:
            print("No moves to undo.")
            return
        row, col = game.move_history.pop()
        game.grade[row][col] = " "
        game.switch_player()
        print("Last move undone.")
