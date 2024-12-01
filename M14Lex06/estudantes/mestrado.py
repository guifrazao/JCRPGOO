from .estudante import Estudante
from interfaces import IEntregaTrabalho

class Mestrado(Estudante, IEntregaTrabalho):
    def __init__(self, nome, matricula, idade, numero_notas):
        super().__init__(nome, matricula, idade, numero_notas)

    def entregarTrabalho(self):
        self.enviarParaBanca()
        print(f"O estudante de mestrado {self._nome}, matrícula: {self.getMatricula()} entregou a Tese para ser avaliada")

    def enviarParaBanca(self):
        print(f"A banca está avaliando o trabalho")