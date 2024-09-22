"""
5. Crie uma classe chamada SocialNetwork que represente uma rede social online. Essa
classe deve ter funcionalidades para adicionar amigos, publicar mensagens,
comentar em posts e buscar por usuários.
"""
from SocialNetwork import SocialNetwork
from Post import Post
from User import User

iran = User("IRAN FERREIRA")
ronaldo = User("RONALDO FENOMENO")
network = SocialNetwork()

network.addUser(iran)
network.addUser(ronaldo)
network.addFriend(ronaldo, iran)
network.makePost(iran, "RECEBA")
network.makePost(ronaldo, "SORRISO RONALDO")

post1 = network.getPost(1)
post2 = network.getPost(2)
network.makeComment(post1, ronaldo, "RONALDO")
network.makeComment(post2, iran, "MELHOR DO MUNDO")

name = iran.getName()
print(network.findUser(name))
