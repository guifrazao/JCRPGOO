from item_collection import ItemCollection

class Book(ItemCollection):  
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author

    def get_details(self):  
        return f"📚 {self.title} ({self.year}) - Autor: {self.author}"
