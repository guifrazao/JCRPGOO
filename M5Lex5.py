class SocialNetwork:
    __users = []
    __posts = []
    def __init__(self, current_user):
        self.__user = current_user
        self.addUser(self.__user)
    
    """A friend request requires someone to send the request and someone to receive the request"""
    def addFriend(self, user):
        self.getCurrUser().addFriend(user)
        print(self.__newFriendMsg(user))

    def makePost(self, msg):
        post = Post(self.__user, msg)
        self.addPost(post)
        print(post)
    
    def makeComment(self, post, comm):
        post.addComment(comm)
        print(post)

    def getCurrUser(self):
        return self.__user
    def setCurrUser(self, user):
        self.__user = user  
    """TESTE, IGNORAR"""
    def getPost(self, id):
        for post in self.__posts:
            if post.getID() == id:
                return post
        return "NOT FOUND"
    
    @classmethod
    def addPost(cls, post):
        cls.__posts.append(post)

    @classmethod
    def addUser(cls, user):
        cls.__users.append(user)
   
    def __newFriendMsg(self, user):
        return f"New friend {user.getName()} added"
    

        
class User:
    def __init__(self, name):
        self.__name = name
        self.__friends = []
    
    def addFriend(self, user):
        self.__friends.append(user)

    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name
    def getFriends(self):
        return self.__friends
    
class Post:
    __id = 0
    def __init__(self, poster, content):
        self.__incrementID()
        self.__id = self.__id
        self.__poster = poster
        self.__content = content
        self.__comments = []
    
    def __str__(self):
        return f"ID: {self.getID()}{self.getPoster().getName()}: {self.getContent()}\nComments: {self.getComments()}"
    
    def addComment(self, comment):
        self.__comments.append(comment)


    def getID(self):
        return self.__id
    def setID(self, id):
        self.__id = id
    def getPoster(self):
        return self.__poster
    def getContent(self):
        return self.__content
    def getComments(self):
        return self.__comments
    
    """ACESSO DIRETO A UM ATRIBUTO, COISA DE COMPUTEIRO, APENAS PARA TESTE"""
    @classmethod
    def __incrementID(cls):
        cls.__id += 1

conta_teste = User("IRAN FERREIRA")
teste = SocialNetwork(conta_teste)
teste.makePost("TESTE")
teste.makePost("TESTE2")