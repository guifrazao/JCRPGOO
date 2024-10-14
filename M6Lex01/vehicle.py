from owner import Owner
class Vehicle:
    def __init__(self, current_speed, direction, owner: Owner):
        if not self.verifyCurrentSpeed(current_speed):
            raise Exception("INVALID CURRENT SPEED")
        if not self.verifyDirection(direction):
            raise Exception("INVALID TIRE DIRECTION")
        
        self.__current_speed = current_speed
        self.__direction = direction
        self.__owner = owner

    def __str__(self):
        return f"\nCurrent Speed = {self.__current_speed}km/h\nTire Direction = {self.__direction}°\nOwner = {self.__owner.getName()}"
    
    def getCurrentSpeed(self):
        return self.__current_speed
    
    def setCurrentSpeed(self, current_speed):
        if self.verifyCurrentSpeed(current_speed):
            self.__current_speed = current_speed
        else:
            self.__invalidDataMessage("speed")

    def getDirection(self):
        return self.__direction
    
    def setDirection(self, direction):
        if self.verifyDirection(direction):
            self.__direction = direction
        else:
            self.__invalidDataMessage("tire direction ")

    def getOwner(self) -> Owner:
        return self.__owner
    
    def setOwner(self, owner: Owner):
        self.__owner = owner
    
    @staticmethod
    def verifyCurrentSpeed(current_speed):
        return current_speed > 0 and current_speed <= 500

    @staticmethod
    def verifyDirection(direction):
        return direction >= -45 and direction <= 45
    
    @staticmethod
    def __invalidDataMessage(err):
        print(f"Error: Invalid {err}")

