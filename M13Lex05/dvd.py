from collection import Collection

class DVD(Collection):  
  
    def __init__(self, title, year, director):
        super().__init__(title, year)
        self.director = director

    def get_details(self):  
        return f"📀 {self.title} ({self.year}) - Diretor: {self.director}"
