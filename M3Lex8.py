"""
8. Crie uma classe chamada Employee que inclui três variáveis de instância: um nome
(string), um sobrenome (string) e um salário mensal (float). Sua classe deve ter um
construtor que inicializa as três variáveis. Forneça um método get e set para cada
variável. Se o salário mensal fornecido pelo usuário não for positivo, configure-o
como 0.0. Teste a classe implementada e seus métodos. Crie dois objetos Employee e
exiba o salário anual de cada objeto. Depois, dê 10% de aumento para cada
empregado e exiba novamente os salários.
"""
class Employee:
    def __init__(self, nome, sobrenome, salario_mes):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__salario_mes = salario_mes if salario_mes > 0 else 0
        
    """A variável 'aumento' é o aumento em porcentagem, não em valor decimal"""
    def aumentarSalario(self, aumento):
        self.__salario_mes += self.__salario_mes * aumento/100
    def getSalarioAnual(self):
        return self.salario * 12
    
        
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

print(f"Salário anual de {iran.getNome()} {iran.getSobrenome()}: R${iran.getSalarioAnual():.2f}")
print(f"Salário anual de {ronaldo.getNome()} {ronaldo.getSobrenome()}: R${ronaldo.getSalarioAnual():.2f}")

iran.aumentarSalario(10.0)
ronaldo.aumentarSalario(10.0)

print(f"Salário anual de {iran.getNome()} {iran.getSobrenome()} após aumento: R${iran.getSalarioAnual():.2f}")
print(f"Salário anual de {ronaldo.getNome()} {ronaldo.getSobrenome()} após aumento: R${ronaldo.getSalarioAnual():.2f}")
