from .estudante import Estudante
from interfaces import IEntregaTrabalho, IEnviaParaBanca

class Mestrado(Estudante, IEntregaTrabalho, IEnviaParaBanca):
    def __init__(self, nome, matricula, idade, numero_notas):
        super().__init__(nome, matricula, idade, numero_notas)

    def entregarTrabalho(self):
        print(f"O estudante de mestrado {self._nome}, matrícula: {self._matricula} entregou a Tese para ser avaliada")
        self.enviarParaBanca()

    def enviarParaBanca(self):
        print(f"A banca está avaliando o trabalho")