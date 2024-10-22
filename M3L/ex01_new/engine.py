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
