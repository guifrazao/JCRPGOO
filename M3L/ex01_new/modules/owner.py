class Owner:
    def __init__(self, name):
        self.__name = name
        self.__vehicle = None
    
    def enter_the_vehicle(self, vehicle: any):
        vehicle.turn_on_vehicle()
    
    def indicate_the_vehicle_speed(self, vehicle: any):
        print(f"{vehicle.get_current_speed()} km/h")
    
    def introduce_yourself(self):
        print(f"Hi, I am {self.__name}")

    def get_vehicle(self):
        return self.__vehicle
    
    def set_vehicle(self, vehicle: any):
        self.__vehicle = vehicle