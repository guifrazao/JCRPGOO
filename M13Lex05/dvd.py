from collection import Collection

class DVD(Collection):
    def __init__(self, title, year, director, duration):
        super().__init__(title, year)
        self.director = director
        self.duration = duration  # duração em minutos

    def get_info(self):
        return f"DVD: {self.title}, Ano: {self.year}, Diretor: {self.director}, Duração: {self.duration} minutos"