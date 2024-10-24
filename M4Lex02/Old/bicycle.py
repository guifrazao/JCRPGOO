class Bicycle:
    def __init__(self, velocidade, cadencia, marcha, serie):
        self.__velocidade = velocidade  
        self.__cadencia = cadencia    
        self.__marcha = marcha          
        self.__serie = serie   

    def get_velocidade(self):
        return self.__velocidade

    def get_cadencia(self):
        return self.__cadencia

    def get_marcha(self):
        return self.__marcha

    def get_serie(self):
        return self.__serie

    def set_velocidade(self, velocidade):
        self.__velocidade = velocidade

    def set_cadencia(self, cadencia):
        self.__cadencia = cadencia

    def set_marcha(self, marcha):
        self.__marcha = marcha

    def set_serie(self, serie):
        self.__serie = serie
        
    def __str__(self):
        return (f"Velocidade: {self.__velocidade}\n"
                f"Cadência: {self.__cadencia}\n"
                f"Marcha: {self.__marcha}\n"
                f"Número de série: {self.__serie}")