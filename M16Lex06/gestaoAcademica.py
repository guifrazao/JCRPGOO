
from interfaces import IEntregaTrabalho, IEstudante

class GestaoAcademica:
    def __init__(self):
        self.__estudantes = []

    def adicionarEstudante(self, estudante: IEstudante):
        self.__estudantes.append(estudante)

    def removerEstudante(self, estudante):
        if self.buscarEstudantePorMatricula(estudante.getMatricula()):
            self.__estudantes.remove(estudante)
            return True
        return False
    
    def consultarEstudantes(self):
        for estudante in self.__estudantes:
            estudante.imprimirInformacoes()

    def receberEntregaTrabalhos(self):
        if len(self.__estudantes) == 0:
            print("Nenhum estudante no sistema")
            
        for estudante in self.__estudantes:
            if self.seEntregaTrabalho(estudante):
                estudante.entregarTrabalho()

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

    @staticmethod
    def seEntregaTrabalho(estudante):
        return isinstance(estudante, IEntregaTrabalho)
    