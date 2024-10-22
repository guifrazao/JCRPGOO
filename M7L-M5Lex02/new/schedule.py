class Schedule:
    def __init__(self):
        self.phone_book = []

    def perform_action(self, action:any):
        return action.execute(self.phone_book)



