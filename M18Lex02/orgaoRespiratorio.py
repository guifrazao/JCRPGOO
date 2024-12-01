class OrgaoRespiratorio:
    def __init__(self, nome):
        self._nome = nome

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome