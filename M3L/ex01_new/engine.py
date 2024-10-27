class Engine:
    '''Represents a engine of a vehicle'''

    def __init__(self, type, horsepower):
        '''Initializes a new Engine object.'''
        self.__type = type
        self.__horsepower = horsepower

    def get_type(self):
        '''Returns the engine type.'''
        return self.__type

    def set_type(self, type):
        '''Change the engine type.'''
        self.__type = type

    def get_horsepower(self):
        '''Returns the engine's horsepower.'''
        return f"{self.__horsepower} HP"

    def set_horsepower(self, horsepower):
        '''Change the engine's horsepower.'''
        self.__horsepower = horsepower
        
'''
Motores de Combustão Interna (MCI): Carros, caminhões, motos, tratores, barcos de pequeno porte.
Motores de Combustão Externa: Locomotivas históricas, navios antigos, máquinas industriais clássicas.
Motores Elétricos: Carros elétricos, ônibus elétricos, trens, veículos industriais.
Motores Híbridos: Carros híbridos (como Toyota Prius, Chevrolet Volt), veículos utilitários.
Motores a Hidrogênio: Carros a hidrogênio (Toyota Mirai), ônibus de emissão zero.
Motores de Turbina a Gás: Aviões comerciais, helicópteros, veículos militares, barcos de alta velocidade.
Motores Pneumáticos: Veículos experimentais, bicicletas de ar comprimido, veículos de curta distância em indústrias.
'''
