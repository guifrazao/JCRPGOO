from noughts_and_crosses import NoughtsAndCrosses

def main():
    game = NoughtsAndCrosses()
    winner = None

    while winner is None:
        game.print_board(game.board)
        game.make_move()
        winner = game.check_winner()

    game.print_board(game.board)
    if winner == "Draw":
        print("It's a draw!")
    else:
        print(f"The winner is {winner}!")

main()