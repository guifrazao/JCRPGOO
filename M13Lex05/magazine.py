from collection import Collection

class Magazine(Collection):  

    def __init__(self, title, year, issue):
        super().__init__(title, year)
        self.issue = issue

    def get_details(self):  
        return f"📰 {self.title} ({self.year}) - Edição: {self.issue}"
