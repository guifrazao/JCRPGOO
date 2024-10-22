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
        self.__current_speed = current_speed
        self.__direction = direction
        self.__owner = owner

    def get_current_speed(self):
        '''Returns the vehicle's speed(Kilometers per hour).'''
        return self.__current_speed + "km/h"
    
    def set_current_speed(self, current_speed):
        '''Change the vehicle's speed.'''
        self.__current_speed = current_speed

    def get_direction(self):
        '''Returns the steering angle of the tires.'''
        return self.__direction + "°"
    
    def set_direction(self, direction):
        '''Change the steering angle of the tires.'''
        self.__direction = direction

    def get_owner(self):
        '''Returns the name of the vehicle owner.'''
        return "The owner is " + self.__owner
    
    def set_owner(self, owner):
        '''Change the name of the vehicle owner.'''
        self.__owner = owner

    def type_vehicle(self, opcao):
        if opcao == 1:
            self.car()
        elif opcao == 2:
            self.motorcycle()
        else:
            print("Invalid option")

    def car(self):
        print("This vehicle is a car")

    def motorcycle(self):
        print("This vehicle is a motorcycle")




    