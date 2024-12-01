# projeto.py
class Projeto:
    def __init__(self, nome, descricao):
        self.__nome = nome
        self.__descricao = descricao
        self.__equipes = []

    def adicionar_equipe(self, equipe):
        self.__equipes.append(equipe)

    def listar_equipe(self):
        print(f"Equipe(s) do projeto {self.__nome}:")
        for equipe in self.__equipes:
            print(f"{equipe.get_nome()}")  # Agora estamos chamando o método get_nome() do Departamento, que retorna apenas o nome

    def __str__(self):
        return f"Projeto: {self.__nome}\nDescrição: {self.__descricao}"
