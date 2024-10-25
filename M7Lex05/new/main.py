"""
5. Crie uma classe chamada SocialNetwork que represente uma rede social online. Essa
classe deve ter funcionalidades para adicionar amigos, publicar mensagens,
comentar em posts e buscar por usuários.
"""
from SocialNetwork import SocialNetwork
from TextPost import TextPost
from ImagePost import ImagePost
from User import User

iran = User("IRAN FERREIRA")
ronaldo = User("RONALDO FENOMENO")
network = SocialNetwork()

network.addUser(iran)
network.addUser(ronaldo)
network.addFriend(ronaldo, iran)
network.post(TextPost(iran, "RECEBA"))
network.post(ImagePost(ronaldo, "IMG38581958.png"))

post1 = network.getPost(iran)
post2 = network.getPost(ronaldo)
network.makeComment(post1, ronaldo, "RONALDO")
network.makeComment(post2, iran, "MELHOR DO MUNDO")

name = iran.getName()
print(network.findUser(name))