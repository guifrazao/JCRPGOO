from familias_animais import Ave
from mix_ins import NadadorMixIn


class AveAquatica(NadadorMixIn, Ave):
    def __init__(self, nome, cor, envergadura):
        super().__init__(nome, cor, envergadura)
        self._tipo = "Ave Aquática"

    
