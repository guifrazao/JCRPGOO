"""
5. Crie uma classe chamada SocialNetwork que represente uma rede social online. Essa
classe deve ter funcionalidades para adicionar amigos, publicar mensagens,
comentar em posts e buscar por usuários.
"""
from SocialNetwork import SocialNetwork
from TextPost import TextPost
from User import User

iran = User("IRAN FERREIRA")
ronaldo = User("RONALDO FENOMENO")
teste = User("ADRIANO")
network = SocialNetwork()

network.addUser(iran)
network.addUser(ronaldo)
network.addUser(teste)

network.addFriend(iran, ronaldo)
network.addFriend(teste, ronaldo)
print()

network.post(TextPost(iran, "RECEBA"))

post1 = network.getPost(1)
network.makeComment(post1, ronaldo, "RONALDO")
network.makeComment(post1, ronaldo, "SORRISO RONALDO")
network.makeComment(post1, iran, "MELHOR DO MUNDO")

name = ronaldo.getName()
print(network.findUser(name))
print()

network.printUserCommentHistory(ronaldo)