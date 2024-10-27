'''
M3L-ex01. Escreva uma classe chamada Vehicle que possua campos para a velocidade atual em 
km/h, a direção em graus dos pneus e o nome do proprietário. Crie métodos de 
acesso e impressão para esta classe e faça um programa de teste.
'''

from engine import Engine

class Vehicle:
    '''Represents a vehicle'''
    def __init__(self, current_speed, direction, owner, engine: Engine):
        '''Initializes a new Vehicle object.'''
        self.__current_speed = current_speed
        self.__direction = direction
        self.__owner = owner
        self.__engine = engine  

    def get_current_speed(self):
        '''Returns the vehicle's speed(Kilometers per hour).'''
        return f"{self.__current_speed} km/h"

    def set_current_speed(self, current_speed):
        '''Change the vehicle's speed.'''
        self.__current_speed = current_speed

    def get_direction(self):
        '''Returns the steering angle of the tires.'''
        return f"{self.__direction}°"

    def set_direction(self, direction):
        '''Change the steering angle of the tires.'''
        self.__direction = direction

    def get_owner(self):
        '''Returns the name of the vehicle owner.'''
        return f"The owner is {self.__owner}"

    def set_owner(self, owner):
        '''Change the name of the vehicle owner.'''
        self._owner = owner

    def get_engine_info(self):
        '''Returns the engine type and horsepower.'''
        return f"Engine Type: {self.__engine.get_type()}, Horsepower: {self.__engine.get_horsepower()}"

'''
Engine Types
Internal Combustion Engine (ICE): Inclui motores a gasolina e diesel.
Electric Motor: Usado em veículos elétricos (EVs).
Hybrid Engine: Combina motor de combustão interna com um motor elétrico.
'''
