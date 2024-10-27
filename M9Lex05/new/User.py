class User:
    def __init__(self, name):
        if not self.verifyName(name):
            self.__invalidNameMsg()
            exit()

        self.__name = name
        self.__friends = []
        self.__comments = []
    
    def __str__(self):
        return f"Username: {self.getName()}\nFriends: {self.listFriends()}"
    
    def addFriend(self, user):
        self.__friends.append(user)

    """Adds comment to the list of comments the user has made"""
    def addComment(self, comment):
        self.__comments.append(comment)

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    def getFriends(self):
        return self.__friends
    
    def listFriends(self):
        str = ""
        for friend in self.__friends:
            str += friend.getName() + ", "
        return str
    
    def printCommentHistory(self):
        str = ""
        for comment in self.__comments:
            str += f"{comment}" + "\n"
        
        print(str)
    
    @staticmethod
    def verifyName(name):
        return len(name) >= 3
    
    @staticmethod
    def __invalidNameMsg():
        print("Invalid name")