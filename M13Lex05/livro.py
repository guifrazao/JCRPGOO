from collection import Collection

class Book(Collection):
    def __init__(self, title, year, author, genre):
        super().__init__(title, year)
        self.author = author
        self.genre = genre

    def get_info(self):
        return f"Livro: {self.title}, Ano: {self.year}, Autor: {self.author}, Gênero: {self.genre}"

    