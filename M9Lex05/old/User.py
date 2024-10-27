class User:
    def __init__(self, name):
        self.__name = name
        self.__friends = []
    
    def __str__(self):
        return f"Username: {self.getName()}\nFriends: {self.printFriends()}"
    
    def addFriend(self, user):
        self.__friends.append(user)

    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name
    def getFriends(self):
        return self.__friends
    def printFriends(self):
        str = ""
        for friend in self.__friends:
            str += friend.getName() + " "
        return str