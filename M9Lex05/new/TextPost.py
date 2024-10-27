class TextPost:
    __id = 0
    def __init__(self, poster, content):
        self.__incrementID()
        self.__id = self.__id
        self.__poster = poster
        self.__content = content
        self.__comments = []
    
    def __str__(self):
        return f"{self.__poster.getName()}: {self.getContent()}\nComments: {self.getComments()}"
    
    def addComment(self, comment):
        self.__comments.append(comment)

    def getID(self):
        return self.__id
    
    @classmethod
    def setID(cls, id):
        cls.__id = id
    
    def getPoster(self):
        return self.__poster
    
    def getContent(self):
        return self.__content
    
    def getComments(self):
        teste = ""
        for comment in self.__comments:
            teste += "\n" + comment.getPoster().getName() + ": " + comment.getContent()
        return teste
    
    @classmethod
    def __incrementID(cls):
        cls.setID(cls.__id+1)
