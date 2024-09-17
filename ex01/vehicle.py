'''
Escreva uma classe chamada Vehicle que possua campos para a velocidade atual em 
km/h, a direção em graus dos pneus e o nome do proprietário. Crie métodos de 
acesso e impressão para esta classe e faça um programa de teste. 
'''

'''File:vehicle.py
Features for managing a vehicle's speed, tire direction and the owner's name.'''
class Vehicle:
    '''Represents a vehicle'''
    def __init__(self, current_speed, direction, owner):
        '''Initializes a new Vehicle object.'''
        self._current_speed = current_speed
        self._direction = direction
        self._owner = owner

    def get_current_speed(self):
        '''Returns the vehicle's speed(Kilometers per hour).'''
        return self._current_speed + "km/h"
    
    def set_current_speed(self, current_speed):
        '''Change the vehicle's speed.'''
        self._current_speed = current_speed

    def get_direction(self):
        '''Returns the steering angle of the tires.'''
        return self._direction + "°"
    
    def set_direction(self, direction):
        '''Change the steering angle of the tires.'''
        self._direction = direction

    def get_owner(self):
        '''Returns the name of the vehicle owner.'''
        return "The owner is " + self._owner
    
    def set_owner(self, owner):
        '''Change the name of the vehicle owner.'''
        self._owner = owner



    
