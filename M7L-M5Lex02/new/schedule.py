'''
M5L-ex02. Implemente uma classe chamada Schedule que represente uma agenda telefônica. 
Essa classe deve permitir adicionar, editar e remover contatos, além de buscar por 
contatos a partir de um nome ou número de telefone.
'''

class Schedule:
    def __init__(self):
        self.phone_book = []

    def perform_action(self, action:any):
        return action.execute(self.phone_book)



