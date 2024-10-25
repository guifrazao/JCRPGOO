from CardsGame import CardsGame
from Blackjack import Blackjack
from Uno import Uno

blackjack = Blackjack()
game = CardsGame()
game.addPlayer("IRAN")
game.addPlayer("RONALDO")
game.addPlayer("GARRINCHA")

game.playGame(Uno())
game.playGame(Blackjack())