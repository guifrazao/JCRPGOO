"""
4. Implemente uma classe chamada CardsGame que represente um jogo de cartas
simples, como o Uno. Essa classe deve ter métodos para embaralhar as cartas,
distribuir as cartas aos jogadores e permitir jogadas.
"""
import random
from Blackjack import Blackjack
class CardsGame:
    """Chosen cards game is Blackjack"""
    __cards = [{"A":1}, {"2":2}, {"3":3}, {"4":4}, {"5":5}, {"6":6}, {"7":7}, {"8":8}, {"9":9}, {"10":10}] * 4
    def __init__(self, game=None):
        self.__players = []
        #the current deck (changes when cards are played)
        self.__curr_cards = []
        self.__game = game

    """Shuffles the cards, gives them to the players and plays the turns in a loop until a player wins"""
    def playGame(self):
        players = self.getPlayers()
        cards = self.shuffleCards()
        self.giveCards(players, cards)

        if self.hasGame():
            self.__game.playGame(players, cards) 

    """Gets the game's cards, uses the shuffle() method from the random library for shuffling and returns the shuffled deck"""
    def shuffleCards(self):
        cards_shuffled = self.__getCards()
        random.shuffle(cards_shuffled)
        return cards_shuffled
    
    """Gives every player 2 cards. In blackjack, only the card values matter"""
    def giveCards(self, players, cards):
        for player in players:
            for _ in range(2):
                self.addPoints(player, cards)
        self.setCurrCards(cards)

    """Points is the sum of the values of the cards the player currently has"""
    def addPlayer(self, player):
        self.__players.append({"name":player, "points":0})

    """Line 45 example: cards = [{'A': 1}], cards[0].values() = dict_values([1]), list(cards[0].values()) = [1], list(cards[0].values())[0] = 1"""
    def addPoints(self, player, cards):
        player["points"] += list(cards[0].values())[0]
        cards.remove(cards[0])
        self.setCurrCards(cards) 
    
    def getPlayers(self):
        return self.__players
    
    def setPlayers(self, players):
        self.__players = players
    
    def getCurrCards(self):
        return self.__curr_cards
    
    def setCurrCards(self, curr_cards):
        self.__curr_cards = curr_cards

    def getGame(self):
        return self.__game
    
    def setGame(self, game):
        self.__game = game

    def hasGame(self):
        return self.__game is None

    @classmethod
    def __getCards(cls):
        return cls.__cards


