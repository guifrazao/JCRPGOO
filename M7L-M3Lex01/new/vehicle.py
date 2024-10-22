'''
Escreva uma classe chamada Vehicle que possua campos para a velocidade atual em 
km/h, a direção em graus dos pneus e o nome do proprietário. Crie métodos de 
acesso e impressão para esta classe e faça um programa de teste. 
'''

class Vehicle:
    def __init__(self, current_speed, direction, owner):
        self.__current_speed = current_speed
        self.__direction = direction
        self.__owner = owner

    def get_current_speed(self):
        return self.__current_speed + "km/h"
    
    def set_current_speed(self, current_speed):
        self.__current_speed = current_speed

    def get_direction(self):
        return self.__direction + "°"
    
    def set_direction(self, direction):
        self.__direction = direction

    def get_owner(self):
        return "The owner is " + self.__owner
    
    def set_owner(self, owner):
        self.__owner = owner
    
    def show_type_vehicle(self, vehicle: any):
        vehicle.type_vehicle()
        






    
