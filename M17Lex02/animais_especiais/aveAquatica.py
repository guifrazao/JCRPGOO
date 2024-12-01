from familias_animais import Ave
from interfaces import INadador


class AveAquatica(Ave, INadador):
    def __init__(self, nome, cor, envergadura):
        super().__init__(nome, cor, envergadura)
        self._tipo = "Ave Aquática"

    def nadar(self):
        print(f"{self._nome} está nadando")

    
