class NoughtsAndCrosses:
    def __init__(self):
        self.player_1 = "X"
        self.player_2 = "O"
        self.grade = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.current_player = self.player_1
        self.move_history = []

    def switch_player(self):
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1

    def perform_action(self, action):
        return action.execute(self)
