from game_actions import PrintGrade, MakeMove, CheckWinner, UndoMove
from noughts_and_crosses import NoughtsAndCrosses

def main():
    game = NoughtsAndCrosses()
    winner = None

    while winner is None:
        game.perform_action(PrintGrade())
        action = input("Enter 'm' to make a move or 'u' to undo the last move: ").strip().lower()
        if action == 'm':
            game.perform_action(MakeMove())
        elif action == 'u':
            game.perform_action(UndoMove())
        else:
            print("Invalid input.")
            continue
        winner = game.perform_action(CheckWinner())

    game.perform_action(PrintGrade())
    if winner == "Draw":
        print("It's a draw!")
    else:
        print(f"The winner is {winner}!")

main()