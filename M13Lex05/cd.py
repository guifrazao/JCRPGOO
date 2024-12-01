from item_collection import ItemCollection

class CD(ItemCollection):  
    def __init__(self, title, year, artist):
        self.title = title
        self.year = year
        self.artist = artist

    def get_details(self):  
        return f"🎵 {self.title} ({self.year}) - Artista: {self.artist}"
