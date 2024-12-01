from collection import Collection

class CD(Collection):  
  
    def __init__(self, title, year, artist):
        super().__init__(title, year)
        self.artist = artist

    def get_details(self):  
        return f"🎵 {self.title} ({self.year}) - Artista: {self.artist}"
