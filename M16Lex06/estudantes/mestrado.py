
from interfaces import IEntregaTrabalho, IEnviaParaBanca, IEstudante

class Mestrado(IEstudante, IEntregaTrabalho, IEnviaParaBanca):
    def __init__(self, nome, matricula, idade, numero_notas):
        self._nome = nome
        self._matricula = matricula
        self._idade = idade
        self._notas = []

        for _ in range(numero_notas):
            self._notas.append(0)

    def getNome(self):
        return self._nome
    
    def setNome(self, nome):
        self._nome = nome

    def getMatricula(self):
        return self._matricula
    
    def setMatricula(self, matricula):
        self._matricula = matricula

    def getIdade(self):
        return self._idade
    
    def setIdade(self, idade):
        self._idade = idade

    def getNota(self, index):
        return self._notas[index]
    
    def getNotas(self):
        return self._notas
    
    def setNota(self, nota, index):
        self._notas[index] = nota

    def imprimirInformacoes(self):
        print(f"Nome: {self._nome}\nMatrícula: {self._matricula}\nIdade: {self._idade}\nNotas = {self._notas}\n")

    def entregarTrabalho(self):
        print(f"O estudante de mestrado {self._nome}, matrícula: {self._matricula} entregou a Tese para ser avaliada")
        self.enviarParaBanca()

    def enviarParaBanca(self):
        print(f"A banca está avaliando o trabalho")