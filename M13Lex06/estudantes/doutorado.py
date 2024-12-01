from .estudante import Estudante

class Doutorado(Estudante):
    def __init__(self, nome, matricula, idade, numero_notas):
        super().__init__(nome, matricula, idade, numero_notas)

    def entregarTrabalho(self):
        print(f"O estudante de doutorado {self._nome}, matrícula: {self.getMatricula()} entregou a Tese para ser avaliada")