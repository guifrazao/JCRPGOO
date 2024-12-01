from item_collection import ItemCollection

class Magazine(ItemCollection):  
    def __init__(self, title, year, issue):
        self.title = title
        self.year = year
        self.issue = issue

    def get_details(self):  
        return f"📰 {self.title} ({self.year}) - Edição: {self.issue}"
