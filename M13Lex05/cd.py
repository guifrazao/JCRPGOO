from collection import Collection

class CD(Collection):
    def __init__(self, title, year, artist, track_count):
        super().__init__(title, year)
        self.artist = artist
        self.track_count = track_count  # número de faixas

    def get_info(self):
        return f"CD: {self.title}, Ano: {self.year}, Artista: {self.artist}, Faixas: {self.track_count}"