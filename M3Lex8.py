class Employee:
    def __init__(self, nome, sobrenome, salario_mes):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__salario_mes = salario_mes if salario_mes > 0 else 0
        
    """A variável 'aumento' é o aumento em porcentagem, não em valor decimal"""
    def aumentarSalario(self, aumento):
        self.__salario_mes += self.__salario_mes * aumento/100
    
        
    def getNome(self):
        return self.__nome
    def setNome(self, nome):
        self.__nome = nome
    def getSobrenome(self):
        return self.__sobrenome
    def setSobrenome(self, sobrenome):
        self.__sobrenome = sobrenome
    def getSalario(self):
        return self.__salario_mes
    def setSalario(self, salario_mes):
        self.__salario_mes = salario_mes
        
iran = Employee("Iran", "Ferreira", 300.42)
ronaldo = Employee("Ronaldo", "Fenômeno", 11276.65)

print(f"Salário anual de {iran.getNome()} {iran.getSobrenome()}: R${iran.getSalario()*12:.2f}")
print(f"Salário anual de {ronaldo.getNome()} {ronaldo.getSobrenome()}: R${ronaldo.getSalario()*12:.2f}")

iran.aumentarSalario(10.0)
ronaldo.aumentarSalario(10.0)

print(f"Salário anual de {iran.getNome()} {iran.getSobrenome()} após aumento: R${iran.getSalario()*12:.2f}")
print(f"Salário anual de {ronaldo.getNome()} {ronaldo.getSobrenome()} após aumento: R${ronaldo.getSalario()*12:.2f}")
