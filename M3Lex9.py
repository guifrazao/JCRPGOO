class Date:
    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
    
    def formatarData(self):
        return f"{self.__dia:02}/{self.__mes:02}/{self.__ano:04}"
        
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
    
    
teste = Date(10, 10, 2010)
print(teste.formatarData())
