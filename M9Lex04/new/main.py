from CardsGame import CardsGame
from Blackjack import Blackjack

blackjack = Blackjack()
game = CardsGame(blackjack)
blackjack.setCardsGame(game)

game.addPlayer("IRAN")
game.addPlayer("RONALDO")
game.addPlayer("GARRINCHA")

game.playGame()
