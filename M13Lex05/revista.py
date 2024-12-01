from collection import Collection

class Magazine(Collection):
    def __init__(self, title, year, issue_number, category):
        super().__init__(title, year)
        self.issue_number = issue_number
        self.category = category

    def get_info(self):
        return f"Revista: {self.title}, Ano: {self.year}, Edição: {self.issue_number}, Categoria: {self.category}"