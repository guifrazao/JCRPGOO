class Comment:
    __id = 0
    def __init__(self, post, poster, content):
        self.__incrementID()
        self.__id = self.__id
        self.__post = post
        self.__poster = poster
        self.__content = content
    
    def __str__(self):
        return f"{self.__poster.getName()}: {self.getContent()}"

    def getID(self):
        return self.__id
    
    @classmethod
    def setID(cls, id):
        cls.__id = id
    
    def getPost(self):
        return self.__post
    
    def setPost(self, post):
        self.__post = post

    def getPoster(self):
        return self.__poster
    
    def getContent(self):
        return self.__content
    
    def printContent(self):
        return "\n" + self.getPoster().getName() + ": " + self.getContent()
    
    @classmethod
    def __incrementID(cls):
        cls.setID(cls.__id+1)