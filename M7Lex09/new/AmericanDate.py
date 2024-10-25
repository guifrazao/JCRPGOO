"""
9. Crie uma classe chamada Date que inclui três variáveis de instância: dia (int), mês
(int) e ano (int). Sua classe deve ter um construtor que inicializa as três variáveis de
instância e assume que os valores fornecidos são corretos. Forneça um método get e
um set para cada variável. Forneça um método que exibe o dia, o mês e o ano
separados por barras “/”. Teste a classe implementada e seus métodos.
"""
class AmericanDate:
    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
    
    def formatarData(self):
        return f"{self.__mes:02}/{self.__dia:02}/{self.__ano:04}"
        
    def getDia(self):
        return self.__dia
    def setDia(self, dia):
        self.__dia = dia
    def getMes(self):
        return self.__mes
    def setMes(self, mes):
        self.__mes = mes
    def getAno(self):
        return self.__ano
    def setAno(self, ano):
        self.__ano = ano
    
    