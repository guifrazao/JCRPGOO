from collection import Collection

class Book(Collection):  
    """
    Representa livros no acervo. Extende a classe abstrata Collection.
    """
    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.author = author

    def get_details(self):  
        """
        Implementa o método abstrato para fornecer detalhes específicos de um livro.
        """
        return f"📚 {self.title} ({self.year}) - Autor: {self.author}"
