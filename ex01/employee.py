'''
1. Implemente a classe Employee com nome, número de matrícula e salário. 
a. Crie um método para exibir os dados. 
b. Crie as classes AdministrativeAssistant e TecnicalAssistent, herdando de 
Employee. 
c. Sabendo que os assistentes técnicos possuem um bônus salarial e que os 
assistentes administrativos possuem um turno (dia ou noite) e um adicional 
noturno, sobrescreva o método que exibe os dados. 
'''

class Employee:
    def __init__(self, nome, numero_matricula, salario):
        self.nome = nome
        self.numero_matricula = numero_matricula
        self.salario = salario

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Número de Matrícula: {self.numero_matricula}")
        print(f"Salário Inicial: R${self.salario:.2f}")

class AdministrativeAssistant(Employee):
    def __init__(self, nome, numero_matricula, salario, turno, adicional_noturno):
        super().__init__(nome, numero_matricula, salario)
        self.turno = turno
        self.adicional_noturno = adicional_noturno
        self.salario_final = self.salario  

    def atualizar_salario(self):
        if self.turno.lower() == "noite":
            self.salario_final = self.salario * (1 + self.adicional_noturno / 100)
        else:
            self.salario_final = self.salario

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Salário Final: R${self.salario_final:.2f}")
        print(f"Turno: {self.turno}")
        if self.turno.lower() == "noite":
            print(f"Adicional Noturno: R${((self.salario * self.adicional_noturno) / 100):.2f}")

class TechnicalAssistant(Employee):
    def __init__(self, nome, numero_matricula, salario, bonus_salarial):
        super().__init__(nome, numero_matricula, salario)
        self.bonus_salarial = bonus_salarial
        self.salario_final = salario
    
    def atualizar_salario(self):
        self.salario_final = self.salario + self.bonus_salarial
    
    def exibir_dados(self):
        super().exibir_dados()
        print(f"Salário Final: R${self.salario_final:.2f}")
        print(f"Bônus Salarial: R${self.bonus_salarial:.2f}")











