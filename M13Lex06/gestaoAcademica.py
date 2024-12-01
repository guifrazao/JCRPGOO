from estudantes import Estudante

class GestaoAcademica:
    def __init__(self):
        self.__estudantes = []

    def adicionarEstudante(self, estudante: Estudante):
        self.__estudantes.append(estudante)

    def removerEstudante(self, estudante):
        if self.buscarEstudantePorMatricula(estudante.getMatricula()):
            self.__estudantes.remove(estudante)
            return True
        return False
    
    def consultarEstudantes(self):
        for estudante in self.__estudantes:
            print(f"Nome: {estudante.getNome()}\nMatrícula: {estudante.getMatricula()}\nIdade: {estudante.getIdade()}\nNotas = {estudante.getNotas()}\n")

    def receberEntregaTrabalhos(self):
        if len(self.__estudantes) == 0:
            print("Nenhum estudante no sistema")
            
        for estudante in self.__estudantes:
            print(f"O trabalho de {estudante.getNome()}, matrícula: {estudante.getMatricula()} está sendo avaliado")

    def seEstudanteExiste(self, matricula):
        for estudante in self.__estudantes:
            if estudante.getMatricula() == matricula:
                return True
        return False

    def buscarEstudantePorMatricula(self, matricula):
        for estudante in self.__estudantes:
            if estudante.getMatricula() == matricula:
                return estudante
        return None

    