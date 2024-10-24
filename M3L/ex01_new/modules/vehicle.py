class Vehicle:
    def __init__(self, current_speed, direction):
        self.__current_speed = current_speed
        self.__direction = direction
        self.__owner = None

    def turn_on_vehicle(self):
        print("Turning on the engine...")

    def get_current_speed(self):
        return self.__current_speed # "km/h"
    
    def set_current_speed(self, current_speed):
        self.__current_speed = current_speed

    def get_direction(self):
        return self.__direction # "°"
    
    def set_direction(self, direction):
        self.__direction = direction

    def get_owner(self):
        return self.__owner
    
    def set_owner(self, owner: any):
        self.__owner = owner

    



    