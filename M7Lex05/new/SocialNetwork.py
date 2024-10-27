"""
M5L-ex05. Crie uma classe chamada SocialNetwork que represente uma rede social online. Essa
classe deve ter funcionalidades para adicionar amigos, publicar mensagens,
comentar em posts e buscar por usuários.
"""

class SocialNetwork:
    __users = []
    __posts = []
    def __init__(self):
        pass
    
    """Adds sender as receiver's friend and prints a message to inform that a friend was added"""
    def addFriend(self, sender, receiver):
        receiver.addFriend(sender)
        print(self.__newFriendMsg(sender))

    """Creates Post object, adds it to the posts class attribute and prints the post"""
    def post(self, post):
        self.addPost(post)
        print(f"{post}\n")

    """Creates a dictionary to represent the comment which contains who posted the comment and its content, adds it to the post's comment list and prints the post(?)"""
    def makeComment(self, post, poster, msg):
        comm = {"poster":poster.getName(), "msg":msg}
        post.addComment(comm)
        print(f"{post}\n")

    def findUser(self, name):
        user = self.getUser(name)
        if user is None:
            print(self.__userNotFoundMsg())
            exit()
        return f"{user}"
        
    def getUser(self, name):
        for user in self.__users:
            if user.getName() == name:
                return user
        return None 

    def getPost(self, poster):
        for post in self.__posts:
            if post.getPoster() == poster:
                return post
        return None
    
    @classmethod
    def addPost(cls, post):
        cls.__posts.append(post)

    @classmethod
    def addUser(cls, user):
        cls.__users.append(user)
   
    def __newFriendMsg(self, user):
        return f"New friend {user.getName()} added"
    
    def __userNotFoundMsg(self):
        return "User not found"
