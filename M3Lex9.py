class Date:
    def __init__(self, dia, mes, ano):
        self._dia = dia
        self._mes = mes
        self._ano = ano
    
    def formatarData(self):
        return f"{self._dia:02}/{self._mes:02}/{self._ano:04}"
        
    def getDia(self):
        return self._dia
    def setDia(self, dia):
        self._dia = dia
    def getMes(self):
        return self._mes
    def setMes(self, mes):
        self._mes = mes
    def getAno(self):
        return self._ano
    def setAno(self, ano):
        self._ano = ano
    
    
teste = Date(4, 7, 1988)
print(teste.formatarData())
