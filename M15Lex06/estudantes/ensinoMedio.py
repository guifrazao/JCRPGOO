from .estudante import Estudante
from interfaces import IEntregaTrabalho

class EnsinoMedio(Estudante):
    def __init__(self, nome, matricula, idade, numero_notas):
        super().__init__(nome, matricula, idade, numero_notas)
        self.__disciplinas = []

    def adicionarDisciplina(self, disciplina):
        self.__disciplinas.append(disciplina.upper())

    def getDisciplina(self, index):
        return self.__disciplinas[index]
    
    def setDisciplina(self, disciplina, index):
        self.__disciplinas[index] = disciplina
