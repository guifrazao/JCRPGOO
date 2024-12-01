class Projeto:
    def __init__(self, titulo):
        self._titulo = titulo

    def detalhes(self):
        return f"Tese: {self._titulo}"
