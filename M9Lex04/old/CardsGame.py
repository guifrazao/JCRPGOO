"""
4. Implemente uma classe chamada CardsGame que represente um jogo de cartas
simples, como o Uno. Essa classe deve ter métodos para embaralhar as cartas,
distribuir as cartas aos jogadores e permitir jogadas.
"""
import random
class CardsGame:
    """Chosen cards game is Blackjack"""
    __cards = [{"A":1}, {"2":2}, {"3":3}, {"4":4}, {"5":5}, {"6":6}, {"7":7}, {"8":8}, {"9":9}, {"10":10}] * 4
    def __init__(self):
        self.__players = []
        #the current deck (changes when cards are played)
        self.__curr_cards = []

    """Shuffles the cards, gives them to the players and plays the turns in a loop until a player wins"""
    def playGame(self):
        players = self.getPlayers()
        cards = self.shuffleCards()
        self.giveCards(players, cards)
        while True:
            for player in players:
                self.playTurn(player, cards)  
            
    """The player gets the choice of taking a card or passing. If the player takes a card, adds the value of the card to the player's points and updates the deck"""
    def playTurn(self, player, cards):
        if len(self.getPlayers()) == 1:
            self.__awardVictory(player) 

        print(f"{player['name']}'s turn [{player['points']} points]")
        if input("Do you wish to take a card from the deck? [y/n]").lower() == "y":
            self.addPoints(player, cards)
            print(f"{player['name']}'s points changed to {player['points']}")
            
        if self.__checkForWinner(player) == "LOST":
            self.__eliminatePlayer(player)   
            print()            
        elif self.__checkForWinner(player) == "WON":
            self.__awardVictory(player)
        else:
            print("Next round") 
            print()

    """Gets the game's cards, uses the shuffle() method from the random library for shuffling and returns the shuffled deck"""
    def shuffleCards(self):
        cards_shuffled = self.__getCards()
        random.shuffle(cards_shuffled)
        return cards_shuffled
    
    """Gives every player 2 cards. In blackjack, only the card values matter"""
    def giveCards(self, players, cards):
        for player in players:
            for i in range(2):
                self.addPoints(player, cards)
        self.setCurrCards(cards)

    """Points is the sum of the values of the cards the player currently has"""
    def addPlayer(self, player):
        self.__players.append({"name":player, "points":0})

    """Line 58 example: cards = [{'A': 1}], cards[0].values() = dict_values([1]), list(cards[0].values()) = [1], list(cards[0].values())[0] = 1"""
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

    """If the player's points is equal to 21, the player wins. If their points are over 21, they lose. Otherwise, the game continues"""
    def __checkForWinner(self, player):
        if player["points"] == 21:
            return "WON"
        elif player["points"] > 21:
            return "LOST"
        return "CONTINUE"

    def __awardVictory(self, player):
        print(f"{player['name']} won, end of game")
        exit()
    
    def __eliminatePlayer(self, player):
        print(f"{player['name']} eliminated, points are over 21")
        players = self.getPlayers()
        players.remove(player)           
        self.setPlayers(players)
    
    @classmethod
    def __getCards(cls):
        return cls.__cards

