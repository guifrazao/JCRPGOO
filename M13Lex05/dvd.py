from item_collection import ItemCollection

class DVD(ItemCollection):  
    def __init__(self, title, year, director):
        self.title = title
        self.year = year
        self.director = director

    def get_details(self):  
        return f"📀 {self.title} ({self.year}) - Diretor: {self.director}"
