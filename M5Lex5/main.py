from SocialNetwork import SocialNetwork
from Post import Post
from User import User

iran = User("IRAN FERREIRA")
ronaldo = User("RONALDO FENOMENO")
teste = SocialNetwork()

teste.addUser(iran)
teste.addUser(ronaldo)
teste.addFriend(ronaldo, iran)
teste.makePost(iran, "RECEBA")
teste.makePost(ronaldo, "SORRISO RONALDO")

post1 = teste.getPost(1)
post2 = teste.getPost(2)
teste.makeComment(post1, ronaldo, "RONALDO")
teste.makeComment(post2, iran, "MELHOR DO MUNDO")

nome = iran.getName()
print(teste.findUser(nome))