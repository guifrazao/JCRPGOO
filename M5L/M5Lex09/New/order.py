from owner import Owner

class Order:
    def __init__(self, owner: Owner):
        self.__owner = owner

    def __str__(self):
        return f"\nOwner: {self.__owner}"

    def get_owner(self):
        return self.__owner

