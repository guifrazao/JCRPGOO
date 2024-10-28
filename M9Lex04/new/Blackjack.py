"""
4. Implemente uma classe chamada CardsGame que represente um jogo de cartas
simples, como o Uno. Essa classe deve ter métodos para embaralhar as cartas,
distribuir as cartas aos jogadores e permitir jogadas.
"""

class Blackjack:
    def __init__(self): #CardsGame é inicializado como None
        self.__cards_game = None

    def playGame(self, players, cards):
        while True:
            self.playTurn(players, cards)

    def playTurn(self, players, cards):
        for player in players:
            if len(players) == 1:
                self.__awardVictory(player) 

            print(f"{player['name']}'s turn [{player['points']} points]")
            if input("Do you wish to take a card from the deck? [y/n]").lower() == "y":
                self.addPoints(player, cards)
                print(f"{player['name']}'s points changed to {player['points']}")
                
            if self.__checkForWinner(player) == "LOST":
                self.__eliminatePlayer(players, player)   
                print()            
            elif self.__checkForWinner(player) == "WON":
                self.__awardVictory(player)
            else:
                print("Next round") 
                print()

    """Line 36 example: cards = [{'A': 1}], cards[0].values() = dict_values([1]), list(cards[0].values()) = [1], list(cards[0].values())[0] = 1"""
    def addPoints(self, player, cards):
        player["points"] += list(cards[0].values())[0]
        cards.remove(cards[0])

    def getCardsGame(self):
        return self.__cards_game

    def setCardsGame(self, cards_game): #Associação pelo método setter
        self.__cards_game = cards_game

    def __checkForWinner(self, player):
        if player["points"] == 21:
            return "WON"
        elif player["points"] > 21:
            return "LOST"
        return "CONTINUE"

    def __awardVictory(self, player):
        print(f"{player['name']} won, end of game")
        exit()
    
    def __eliminatePlayer(self, players, player):
        print(f"{player['name']} eliminated, points are over 21")
        players.remove(player)
