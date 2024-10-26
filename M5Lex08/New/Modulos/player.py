class Player:
    def __init__(self, name):
        self.__name = name
        self.__game = None

    def __str__(self):
        return f"Player: {self.__name}"

    def set_game(self, game):
        self.__game = game

    def get_game(self):
        return self.__game

    def get_name(self):
        return self.__name
