from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle

vehicle = Vehicle(current_speed="210", direction="0", owner="Gui Frazao")

print(vehicle.get_current_speed())  
print(vehicle.get_direction())      
print(vehicle.get_owner())          

car = Car()
motorcycle = Motorcycle()

vehicle.show_type_vehicle(car)
vehicle.show_type_vehicle(motorcycle)



